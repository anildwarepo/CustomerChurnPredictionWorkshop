from typing import List, Any, Union
import json
import numpy as np
import pandas as pd
import os
from azureml.core.model import Model
import mlflow
import logging
import argparse


arg_parser = argparse.ArgumentParser(description="Argument parser.")
arg_parser.add_argument("--logging_level", type=str, help="logging level")
args, unknown_args = arg_parser.parse_known_args()

logger = logging.getLogger(__name__)
logger.setLevel(args.logging_level.upper())


# Called when the service is loaded
def init():
    global model
    # Get the path to the deployed model file and load it

    model_dir =os.getenv('AZUREML_MODEL_DIR')
    model_file = os.listdir(model_dir)[0]
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), model_file)
    model = mlflow.sklearn.load_model(model_path)
# Called when a request is received
def run1(raw_data):
    try:
        # Get the input data 
        #data=pd.DataFrame(json.loads(raw_data)['data'])
        logger.info( f"anildwa raw_data: {raw_data}")
        logger.info( f"anildwa raw_data: {type(raw_data)}")
        data=raw_data
        #data["Partner"] = data["Partner"].map({"Yes": True, "No": False})
        #data["Dependents"] = data["Dependents"].map({"Yes": True, "No": False})
        #data["PhoneService"] = data["PhoneService"].map({"Yes": True, "No": False})
        #data["PaperlessBilling"] = data["PaperlessBilling"].map({"Yes": True, "No": False})
        logger.info(data.head(10))

        # Get a prediction from the model
        data["predictions"] = model.predict(data)        
        return data
    except Exception as e:
        error= str(e)
        logger.error(error)
        return f"anildwa error: {error}"
    


def run(mini_batch: List[str]) -> Union[List[Any], pd.DataFrame]:
    for file in mini_batch:
        try:
            # Get the input data 
            #data=pd.DataFrame(json.loads(raw_data)['data'])
            logger.info( f"anildwa file: {file}")
            data = pd.read_csv(file)
            #data=raw_data
            #data["Partner"] = data["Partner"].map({"Yes": True, "No": False})
            #data["Dependents"] = data["Dependents"].map({"Yes": True, "No": False})
            #data["PhoneService"] = data["PhoneService"].map({"Yes": True, "No": False})
            #data["PaperlessBilling"] = data["PaperlessBilling"].map({"Yes": True, "No": False})
            print(data.head(10))
            # Get a prediction from the model
            data["predictions"] = model.predict(data)     
            #return pd.DataFrame(results)   
            return data
        except Exception as e:
            error= str(e)
            logger.error(error)
            return f"anildwa error: {error}"


#file_list = [os.path.join("telcocustomerchurn", "batch_scoring_test_data.csv")]

#run(file_list)

    