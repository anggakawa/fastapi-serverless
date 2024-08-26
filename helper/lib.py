import importlib
import os
from typing import Callable, Any

def load_function(function_name: str) -> Callable[[dict, dict], Any]:
    try:
        # Construct the module path
        module_path = f"functions.{function_name}.handler"
        
        # Import the module dynamically
        module = importlib.import_module(module_path)
        
        # Get the handle function from the module
        handle_function = getattr(module, "handle")
        
        # Ensure the handle function is callable
        if not callable(handle_function):
            raise AttributeError(f"The 'handle' attribute in {module_path} is not callable")
        
        return handle_function
    except ImportError as e:
        raise ImportError(f"Could not import module for function '{function_name}': {str(e)}")
    except AttributeError as e:
        raise AttributeError(f"Module for function '{function_name}' does not have a 'handle' function: {str(e)}")
