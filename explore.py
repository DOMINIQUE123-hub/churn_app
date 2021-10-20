import streamlit as st
import pandas as pd
import altair as alt
from itertools import cycle
import numpy as np

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode



def show_explore_page():
    st.title(" Charger les données")

    type_fichier = st.file_uploader(" ", type=["csv", "xls", "txt"])
    if type_fichier is not None:
        with st.beta_expander('Voir les Données'):
            data = pd.read_csv(type_fichier, na_values=["Unknown"], sep=";")
            AgGrid(data)
    use_checkbox = st.checkbox("Selectionnez des clients")

    selection_mode = st.radio("Selection Mode", ['Selection Unique', 'multiple'])


    def fetch_data(samples):
        dummy_data = {
            "Total_Trans_Amt": data['Total_Trans_Amt'],
            "Total_Revolving_Bal": data['Total_Revolving_Bal'],
            "Total_Ct_Chng_Q4_Q1": data['Total_Ct_Chng_Q4_Q1'],
            "Total_Amt_Chng_Q4_Q1": data['Total_Amt_Chng_Q4_Q1'],
            "Avg_Utilization_Ratio": data['Avg_Utilization_Ratio'],
            "Total_Relationship_Count": data['Total_Relationship_Count'],
            "Total_Trans_Ct": data['Total_Trans_Ct'],

        }
        return pd.DataFrame(dummy_data)

    df =fetch_data(use_checkbox)
    gb = GridOptionsBuilder.from_dataframe(df)
    # customize gridOptions
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
    gb.configure_column("Total_Trans_Amt", type=["numericColumn", "numberColumnFilter", "customNumericFormat"])
    gb.configure_column("Total_Revolving_Bal", type=["numericColumn", "numberColumnFilter", "customNumericFormat"])
    gb.configure_column("Total_Ct_Chng_Q4_Q1", type=["numericColumn", "numberColumnFilter", "customCurrencyFormat"])
    gb.configure_column("Total_Amt_Chng_Q4_Q1", type=["numericColumn", "numberColumnFilter", "customNumericFormat"])
    gb.configure_column("Avg_Utilization_Ratio", type=["numericColumn", "numberColumnFilter", "customNumericFormat"])
    gb.configure_column("Total_Relationship_Count", type=["numericColumn", "numberColumnFilter", "customNumericFormat"])
    gb.configure_column("Total_Trans_Ct", type=["numericColumn", "numberColumnFilter", "customNumericFormat"])

    gb.configure_selection(selection_mode)
    if use_checkbox:
        gb.configure_selection(selection_mode, use_checkbox=True,)

    gb.configure_grid_options(domLayout='normal')
    gridOptions = gb.build()

    grid_response = AgGrid(
        df,
        gridOptions=gridOptions,
        #height=grid_height,
        width='100%',
        #data_return_mode=return_mode_value,
        #update_mode=update_mode_value,
        #fit_columns_on_grid_load=fit_columns_on_grid_load,
        allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
        #enable_enterprise_modules=enable_enterprise_modules,
    )









    # st.subheader('Dataset')
    # st.write(df)
    # st.subheader('Tableau descriptif')
    # st.write(df.describe())
    # st.subheader('Variables quantitatives')
    # data_quant = df.select_dtypes(exclude=object)
    # st.write(data_quant)
    # st.subheader('Variables qualitatives')
    # data_qual = df.select_dtypes(object)
    # st.write(data_qual)
    # st.subheader('Variable cible')
    # st.write(df[['Attrition_Flag']])
    # st.subheader('Graphiques Target en fonction des variables pertinentes')
    # fig = px.bar(df, x="Attrition_Flag", y="Total_Trans_Ct", color='Attrition_Flag', barmode="group")
    # st.plotly_chart(fig)
    #
    # fig = px.box(df, x="Attrition_Flag", y="Total_Trans_Amt", color='Attrition_Flag', notched=True)
    # st.plotly_chart(fig)
    #
    # fig = px.box(df, x="Attrition_Flag", y="Total_Trans_Ct", color='Attrition_Flag', notched=True)
    # st.plotly_chart(fig)
    #
    # fig = px.box(df, x="Attrition_Flag", y="Total_Revolving_Bal", color='Attrition_Flag', notched=True)
    # st.plotly_chart(fig)

    # fig = px.box(df, x="Attrition_Flag", y="Total_Ct_Chng_Q4_Q1", color='Attrition_Flag', notched=True)
    # st.plotly_chart(fig)
    #
    # fig = px.box(df, x="Attrition_Flag", y="Total_Amt_Chng_Q4_Q1", color='Attrition_Flag', notched=True)
    # st.plotly_chart(fig)
    #
    # fig = px.box(df, x="Attrition_Flag", y="Avg_Utilization_Ratio", color='Attrition_Flag', notched=True)
    # st.plotly_chart(fig)
    #
    # fig = px.box(df, x="Attrition_Flag", y="Total_Relationship_Count", color='Attrition_Flag', notched=True)
    # st.plotly_chart(fig)













