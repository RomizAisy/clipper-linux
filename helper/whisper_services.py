from faster_whisper import WhisperModel

model = None

def get_model():
    global model
    if model is None:
        model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )
    return model