import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sqlite3
from st_aggrid import AgGrid

# connexion

def connexion():
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT Total_Revolving_Bal, Total_Trans_Amt, Total_Trans_Ct, "
                "Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio, Total_Relationship_Count,"
                " Total_Amt_Chng_Q4_Q1, Attrition_Flag FROM Dataset")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def tirage(nombre):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT Total_Revolving_Bal, Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1,"
                " Total_Relationship_Count, Avg_Utilization_Ratio, Total_Amt_Chng_Q4_Q1,"
                " Attrition_Flag FROM Dataset ORDER BY RANDOM() LIMIT '{}'".format(nombre))
    data = cur.fetchall()
    return data

def predic_multiple():

    #st.title('Prédiction multiple')
    st.markdown("<h1 style='text-align: center; color: white;'>Prédiction multiple</h1>",
                unsafe_allow_html=True)
    st.image("carte_bank.jpg")
    row = connexion()
    #with st.expander('AFFICHER LE DATASET'):
        #data = pd.DataFrame(row, columns=["Total_Revolving_Bal", "Total_Trans_Amt",
    # "Total_Trans_Ct", "Total_Ct_Chng_Q4_Q1", "Total_Relationship_Count", "Avg_Utilization_Ratio",
    # "Total_Amt_Chng_Q4_Q1", "Attrition_Flag"])
       # st.dataframe(data)

    val = st.number_input("Veuillez saisir le nombre de clients", min_value=2, max_value=10000, step=1)
    button = st.button("PREDICTION")

    if button:
        model = pickle.load(open('rand_modo.pkl', 'rb'))
        result = tirage(val)
        resultat = pd.DataFrame(result, columns = ["Total_Revolving_Bal", "Total_Trans_Amt", "Total_Trans_Ct",
                                                   "Total_Ct_Chng_Q4_Q1", "Total_Relationship_Count",
                                                   "Avg_Utilization_Ratio", "Total_Amt_Chng_Q4_Q1", "Attrition_Flag"])

        liste = []
        for i in range(resultat.shape[0]):
            X = resultat.iloc[i, :-1]
            X = np.array(X).reshape(1,-1)
            prediction = model.predict(X)
            if prediction == "Attrited Customer":
                res = "Attrited Customer"
            else:
                res = "Existing Customer"
            liste.append(res)

            df2 = pd.DataFrame(liste, columns= ["predictions"])
            dd = pd.concat([resultat, df2], axis=1)
        AgGrid(dd)
        #st.dataframe(df2)
       # with st.expander("PREDICTION MULTIPLE"):












