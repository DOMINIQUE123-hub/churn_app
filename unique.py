import streamlit as st
import time
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle


def predunique():

    st.markdown("<h1 style='text-align: center; color: white;'>Veuillez renseigner le formulaire</h1>", unsafe_allow_html=True)
    model = pickle.load(open('rand_modo.pkl', 'rb'))
    with st.form(key="CARACTERISTIQUES DU CLIENT"):

        col1, col2 = st.columns(2)
        with col1:

            Total_Revolving_Bal = st.number_input("Solde renouvelable",0)
            Total_Trans_Amt = st.number_input("Montant total de la transaction (12 derniers mois)", 0)
            Total_Trans_Ct = st.number_input("Nombre total de transactions (12 derniers mois)", 0)
            Total_Ct_Chng_Q4_Q1 = st.number_input("Changement du nombre de transactions", 0)
        with col2:
            Total_Relationship_Count = st.number_input("Nombre total de produits détenus par le client", 0)
            Avg_Utilization_Ratio = st.number_input("Taux d'utilisation moyen de la carte", 0)
            Total_Amt_Chng_Q4_Q1 = st.number_input("Changement du montant de la transaction ", 0)
            st.image("carte_bank.jpg", width=150)
            soumission = st.form_submit_button(label= "VALIDER")
    data = {"Total_Revolving_Bal": Total_Revolving_Bal,
            "Total_Trans_Amt": Total_Trans_Amt,
            "Total_Trans_Ct": Total_Trans_Ct,
            "Total_Ct_Chng_Q4_Q1": Total_Ct_Chng_Q4_Q1,
            "Total_Relationship_Count": Total_Relationship_Count,
            "Avg_Utilization_Ratio": Avg_Utilization_Ratio,
            "Total_Amt_Chng_Q4_Q1": Total_Amt_Chng_Q4_Q1}
    paramètres_client = pd.DataFrame(data, index=[0])

    prediction = model.predict(paramètres_client)
    #proba = model.predict_proba(paramètres_client)[0,1]

    if soumission:
        # latest_iteration = st.empty()
        # bar = st.progress(0)
        # for i in range(100):
        #     # Update the progress bar with each iteration.
        #     latest_iteration.text(f'Patientez {i + 1}')
        #     bar.progress(i + 1)
        #     time.sleep(0.1)
        if prediction == "Attrited Customer":
            resultat = st.success("### Ce client est susceptible de se désabonner")
            #st.stop()
        else:
            resultat = st.warning("### Ce client n'est pas susceptible de se désabonner")

        resultat




