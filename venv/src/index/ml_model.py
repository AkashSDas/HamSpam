import os

import joblib

# Getting the location of 'model.joblib' file, the machine learning model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, 'index/model.joblib')

class ML_Model:
    model = joblib.load(file_path)

    def __init__(self):
        pass

    @classmethod
    def _predict(cls, email_content):
        # To make email_content iterable
        email_content = [email_content]
        
        # Making predictions
        predictions = cls.model.predict(email_content)
        return predictions
