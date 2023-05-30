import os
import sys
import numpy as np
import pandas as pd
from pymongo import MongoClient
from src.exception import CustomException
import pickle


from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

"""
def export_collection_as_dataframe(collection_name, db_name):
    try:
        mongo_client = MongoClient(os.getenv("mongodb+srv://mohanty:jisoo7@cluster0.ivrmadz.mongodb.net/?retryWrites=true&w=majority"))

        collection = mongo_client[db_name][collection_name]

        df = pd.DataFrame(list(collection.find()))

        if "_id" in df.columns.to_list():
            df = df.drop(columns=["_id"], axis=1)

        df.replace({"na": np.nan}, inplace=True)

        return df

    except Exception as e:
        raise CustomException(e, sys)
"""
def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)