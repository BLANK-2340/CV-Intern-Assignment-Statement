
from .dino.dino import build_dino

print("Debug: __init__.py loaded")

def build_model(args):
    print("Debug: build_model function called from __init__.py")
    return build_dino(args)

print("Debug: build_model function defined in __init__.py")
