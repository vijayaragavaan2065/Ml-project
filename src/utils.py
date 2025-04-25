import os
import pickle
from src.exception import CustomException
import sys

def save_object(file_path, obj):
    """
    Save a Python object to a file using pickle
    
    Args:
        file_path (str): Path where the object should be saved
        obj: The Python object to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e, sys)