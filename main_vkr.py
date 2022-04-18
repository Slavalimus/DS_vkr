import PyQt5
from sys import exit
from application import Application
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
import tensorflow as tf

from tensorflow import keras
from keras.models import Sequential 
from keras.layers import Dense


model_loaded = keras.models.load_model('models/vz_mod_nn')
model_loaded.summary()
def foo(setup):
    df_setup = pd.DataFrame([setup])
    
    # Нормализация входных данных
    df_setup['density'] = (df_setup['density']-1784.48)/377.09
    df_setup['elasticity'] = (df_setup['elasticity']-2.44)/1646.42
    df_setup['hardener_quantity'] = (df_setup['hardener_quantity']-38.67)/181.83
    df_setup['groups_content'] = (df_setup['groups_content']-15.70)/13.26
    df_setup['temperature'] = (df_setup['temperature']-179.37)/206.70
    df_setup['surf_density'] = (df_setup['surf_density']-0.60)/1290.74    
    df_setup['tensile module'] = (df_setup['tensile module']-64.05)/18.63
    df_setup['tensile_edurance'] = (df_setup['tensile_edurance']-1036.86)/2811.58
    df_setup['consumption'] = (df_setup['consumption']-63.69)/259.36
    df_setup['patch_step'] = (df_setup['patch_step']-0.04)/13.69
    df_setup['patch_density'] = (df_setup['patch_density']-27.27)/58.74
    
    # print(df_setup)
    
    # Прогнозирование нейронной сетью
    predict = model_loaded.predict(df_setup)
    print(predict)
    print(predict*5.2+0.39)
    return predict*5.2+0.39


def debug(data):
    print("=== DEBUGING ===\n")
    
    for key, val in zip(data.keys(), data.values()):
        print(f"{key}: {val}")
        
    print("--------------------------\n")


if __name__ == "__main__":
    app = Application()

    app.mainFunction = foo
    app.start()

    exit(app.core.exec_())
