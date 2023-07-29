import pickle
import json
import numpy as np
import pandas as pd

__locations = None
__model = None
__preprocessor = None


def get_estimated_price(location,sqft,bhk,bath):
    df = pd.DataFrame([[location,sqft,bhk,bath]],columns=['location','total_sqft','bath','bhk'])
    scaled_df = __preprocessor.transform(df)
    return round(__model.predict(scaled_df)[0],2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __locations

    with open("./artifacts/locations.json", "r") as f:
        __locations = json.load(f)['location']

    global __model
    if __model is None:
        with open('./artifacts/model.pkl', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

    global __preprocessor
    if __preprocessor is None:
        with open('./artifacts/preprocessor.pkl','rb') as f:
            __preprocessor = pickle.load(f)

def get_location_names():
    return __locations


if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
    get_estimated_price("BTM Layout",76574.3,3,5)