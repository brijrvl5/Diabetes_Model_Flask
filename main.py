import numpy as np
import pandas as pd
#import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
#from numpy.core.multiarray import result_type
def predict_value(preg_count,glu,blood_pre,Skin_thick,insu,bmi,dia_pedegree,age):
    
    dia_df = pd.read_csv('https://raw.githubusercontent.com/Abhayparashar31/Diabetes-prediction/master/diabetes.csv')

    X = dia_df.drop('Outcome', axis=1)
    y = dia_df['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.33,random_state=7)
    #Choosen_RandomForestClassifier
    rfc = RandomForestClassifier(n_estimators=200)
    #Fitting_Model
    rfc.fit(X_train, y_train)
    result = rfc.predict([[preg_count,glu,blood_pre,Skin_thick,insu,bmi,dia_pedegree,age]])
    if (result[0] == 1):
        return True
    else :
        return False