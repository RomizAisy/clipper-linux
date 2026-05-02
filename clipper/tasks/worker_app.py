import os

# 🔥 MUST BE FIRST (before ANY torch import anywhere)
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import torch
torch.cuda.is_available = lambda: False

_app = None

def get_app():
    global _app

    if _app is None:
        from app import create_app
        _app = create_app()

    return _app