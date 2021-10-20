import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import numpy as np
import pickle
import sqlite3
import altair as alt
from itertools import cycle
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode


def get_table_download_link():
    model = pickle.load(open('rand_modo.pkl', 'rb'))
    uploaded_file = st.file_uploader("Sélectionner un fichier")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, sep=";")
        st.success("Opération effectuée avec succès. Vous pouvez consulter votre dataset")

        #AgGrid(df)

        use_checkbox = st.checkbox("Cochez des individus")

        #selection_mode = st.radio("Sélection spécifique", ["Sélection spécifique"])

        def fetch_data(samples):
            dummy_data = {
                "Total_Revolving_Bal": df["Total_Revolving_Bal"],
                "Total_Trans_Amt": df["Total_Trans_Amt"],
                "Total_Trans_Ct": df["Total_Trans_Ct"],
                "Total_Ct_Chng_Q4_Q1": df["Total_Ct_Chng_Q4_Q1"],
                "Total_Relationship_Count": df["Total_Relationship_Count"],
                "Avg_Utilization_Ratio": df["Avg_Utilization_Ratio"],
                "Total_Amt_Chng_Q4_Q1": df["Total_Amt_Chng_Q4_Q1"],
                "Attrition_Flag": df["Attrition_Flag"]
            }
            return pd.DataFrame(dummy_data)

        don = fetch_data(use_checkbox)
        gb = GridOptionsBuilder.from_dataframe(don)
        # customize gridOptions
        gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
        gb.configure_column("Total_Revolving_Bal", type=["numericColumn", "numberColumnFilter", "customNumericFormat"])
        gb.configure_column("Total_Trans_Amt", type=["numericColumn", "numberColumnFilter", "customNumericFormat"])
        gb.configure_column("Total_Trans_Ct")
        gb.configure_column("Total_Ct_Chng_Q4_Q1", type=["numericColumn", "numberColumnFilter", "customNumericFormat"])
        gb.configure_column("Total_Relationship_Count",
                            type=["numericColumn", "numberColumnFilter", "customNumericFormat"])
        gb.configure_column("Avg_Utilization_Ratio",
                            type=["numericColumn", "numberColumnFilter", "customNumericFormat"])
        gb.configure_column("Total_Amt_Chng_Q4_Q1", type=["numericColumn", "numberColumnFilter", "customNumericFormat"])
        #update_mode_value = GridOptionsBuilder.from_dataframe(df)
        #gb.configure_selection(use_checkbox, selection_mode = 'multiple')
        if use_checkbox:
             gb.configure_selection(use_checkbox=True, selection_mode='multiple')
             gb.configure_grid_options(domLayout='normal')
        gridOptions = gb.build()

        grid_response = AgGrid(
            don,
            gridOptions=gridOptions,
            #height=grid_height,
            width='100%',
            #data_return_mode=return_mode_value,
            update_mode=GridUpdateMode.MODEL_CHANGED,
            #update_mode_value=GridOptionsBuilder.from_dataframe(df),
            #fit_columns_on_grid_load=fit_columns_on_grid_load,
            allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
            #enable_enterprise_modules=enable_enterprise_modules,
        )
        #grid_response["data"]
        selection = grid_response["selected_rows"]
        resultat = pd.DataFrame(selection)
        #resultat[resultat["Attrition_Flag"] == "Attrited Customer"] = 1
        #resultat[resultat["Attrition_Flag"] == "Existing Customer"] = 0
        liste = []
        for i in range(resultat.shape[0]):
            X = resultat.iloc[i, :-1]
            #st.write(X)
            X = np.array(X).reshape(1,-1)
            prediction = model.predict(X)

            if prediction == "Attrited Customer":
                resul = "Attrited Customer"
            else:
                resul = "Existing Customer"
            liste.append(resul)

        df3 = pd.DataFrame(liste, columns=["predictions"])
        # st.dataframe(df2)
        with st.expander("PREDICTION SPECIFIQUE"):
            donee = pd.concat([resultat, df3], axis=1)
        AgGrid(donee)

        #pred = model.predict(selection_donnee)

        # Afficher les prédictions spécifiques
        #st.write("## PREDICTIONS DES CLIENTS SELECTIONNES")
        #AgGrid(pred)



        #st.write(df)
    # st.title("Prédiction spécifique")
    # model = pickle.load(open('rand_modo.pkl', 'rb'))
    # fichier_csv = st.file_uploader("charger un jeu de données ", type = ["csv", "xlsx", "txt"])
    # if fichier_csv is not None:
    #
    #     details_fichiers = {
    #         "nom du fichier": fichier_csv.name,
    #         "type du fichier": fichier_csv.type,
    #         "taille du fichier": fichier_csv.size
    #     }
    #     #st.write(details_fichiers)
    #
    #     if fichier_csv.type == "application/vnd.ms-excel":
    #         df = pd.read_csv(fichier_csv, na_values=["unknow"], sep = ";")
    #         #model.predict(df)
    #         st.success("Opération effectuée avec succès. Vous pouvez consulter votre dataset")
    #         st.write(df)
    #         #prediction = model.predict(df)
    #         #st.write(prediction)
    #     else:
    #         fichier_csv.type = "text/pain"
    #         df = pd.DataFrame(fichier_csv)
    #         #model.predict(df)
    #         st.write(df)
            #prediction = model.predict(df)
            #st.write(prediction)


