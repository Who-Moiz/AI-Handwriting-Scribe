import os
import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow

# 1. SETUP TENSORFLOW ENVIRONMENT
os.environ['TF_USE_LEGACY_KERAS'] = '1'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 2. INITIALIZE MLFLOW
# This creates a local directory called 'mlruns' to track experiments
mlflow.set_experiment("Handwriting_Synthesis_Project")

# 3. IMPORT HANDWRITING MODULE (Ensuring demo.py is present)
try:
    from demo import Hand
    HAND_MODEL = Hand()
    MODEL_STATUS = "Loaded Successfully"
except Exception as e:
    HAND_MODEL = None
    MODEL_STATUS = f"Failed to load: {str(e)}"

# 4. INITIALIZE FASTAPI
app = FastAPI(
    title="AI Scribe: Text-to-Handwriting API",
    description="FastAPI serving Graves' LSTM Handwriting Synthesis Model",
    version="2.0.0"
)

# Pydantic schema for input validation
class SynthesisRequest(BaseModel):
    text: str
    style_id: int = 0
    bias: float = 0.75

# ==========================================
# ENDPOINT 1: Health Check (Required by Guidelines)
# ==========================================
@app.get("/health")
def health_check():
    """Returns the operational status of the API and DL Model."""
    return {
        "status": "healthy",
        "model_status": MODEL_STATUS,
        "framework": "TensorFlow 1.x (Compat)",
        "pipeline": "Text-to-Handwriting Only"
    }

# ==========================================
# ENDPOINT 2: Prediction/Inference (Required by Guidelines)
# ==========================================
@app.post("/predict")
def predict_handwriting(payload: SynthesisRequest):
    """Accepts text and style ID, logs to MLflow, and synthesizes handwriting."""
    if not HAND_MODEL:
        raise HTTPException(status_code=500, detail="Handwriting model is not loaded on backend.")
    
    if not (0 <= payload.style_id <= 12):
        raise HTTPException(status_code=400, detail="style_id must be between 0 and 12.")

    timestamp = int(time.time())
    filename_base = f"output_style{payload.style_id}_{timestamp}.svg"

    # --- MLFLOW EXPERIMENT TRACKING ---
    # Every time someone hits the API, MLflow logs the run details automatically
    with mlflow.start_run(run_name=f"api_inference_style_{payload.style_id}"):
        # Log Parameters
        mlflow.log_param("style_id", payload.style_id)
        mlflow.log_param("bias_neatness", payload.bias)
        mlflow.log_param("text_length", len(payload.text))
        
        start_time = time.time()
        
        try:
            # Execute actual model inference from demo.py
            generated_svgs = HAND_MODEL.write(
                filename=filename_base,
                lines=payload.text,
                biases=[payload.bias],
                styles=[payload.style_id],
                page_width=1860,
                page_height=3508,
                ruled=True
            )
            
            generation_time = time.time() - start_time
            
            # Log Metrics
            mlflow.log_metric("inference_time_sec", generation_time)
            mlflow.log_metric("generated_pages", len(generated_svgs))
            
            return {
                "message": "Handwriting generated successfully!",
                "status": "success",
                "inference_time_seconds": round(generation_time, 3),
                "generated_files": generated_svgs
            }

        except Exception as e:
            mlflow.log_param("error", str(e))
            raise HTTPException(status_code=500, detail=f"Generation error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    # Run server locally on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)