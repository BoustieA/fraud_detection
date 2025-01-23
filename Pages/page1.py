
import streamlit as st
import requests
import numpy as np
import json
import logging

import pandas as pd
import pickle

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger.info('page1')



url_api="http://127.0.0.1:8000/"

df=pd.read_csv("Data/creditcard.csv").drop(columns="Class")

cat_features=df.dtypes.loc[df.dtypes=="object"].index
num_features=df.dtypes.loc[df.dtypes!="object"].index

#Charge les attributs candidats parmis ceux disponible dans la base de donnée
#Donc ceux vu par le modèle

st.title("Prediction de fraud bancaire")
st.text("Selection des attributs du client")
dic={}
for feature in cat_features:
    values=list(df.loc[:,feature].unique())
    dic[feature]=[st.selectbox(feature,values)]   
#requète à l'utilisateur des attributs du véhicule parmis les candidas fourni par l'API
for feature in num_features:
      min_=df.loc[:,feature].min()
      max_=df.loc[:,feature].max()
      dic[feature]=[st.slider(feature,min_,max_)]

# ajoute les options en tant que clé du dictionnaires, avec True si elle a été selectionnée par l'utilisateur, False sinon

jumeau_numerique = pd.DataFrame(dic)
#prédit le prix à partir des attribut si l'utilisateur clique sur le bouton
if st.button("prédire"):
       logger.info('Prédiction')   
       pipeline=pickle.load(open("pipeline.pkl", 'rb'))
       model=pickle.load(open("model.pkl", 'rb'))
       prediction=model.predict(pipeline.transform(jumeau_numerique))[0]
       st.text("Fraude ?")
       if prediction==0:
              st.write("probable")
       else:
             st.write("peu probable")
       st.text("probabilité")
       st.write(str(model.predict_proba(jumeau_numerique)[0][prediction]))
       logger.info("Fraude") 
       logger.info(str(prediction))

    