import streamlit as st
from unique import predunique
from multiple import predic_multiple
# import streamlit.components.v1 as components  # Import Streamlit
from specifique import get_table_download_link
from explore import show_explore_page

def main():
    #st.title('CHURN CARD PREDICTION')
    html_temp = """
    <div style = "background-color:#464e5f;padding:5px, margin:5px, border-radius:20px;">
    <h1 style = "color:white;text-align:center;">CHURN PREDICTION </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html= True)
    #st.markdown("<h1 style='text-align: center; color: grey;'>CHURN CARD PREDICTION</h1>", unsafe_allow_html=True)
    #menu = ["DESCRIPTION DU PROJET", "PREDICTION INDIVIDUELLE", "PREDICTION MULTIPLE"]
    choix = st.sidebar.selectbox('MENU', ("DESCRIPTION DU PROJET", "PREDICTION INDIVIDUELLE", "PREDICTION MULTIPLE", "PREDICTION SPECIFIQUE"))

    if choix == "DESCRIPTION DU PROJET":
        #st.title("Description du projet")
        st.markdown("<h1 style='text-align: center; color: white;'>Description du projet</h1>", unsafe_allow_html=True)
        st.write("Un responsable d’une banque souhaite réduire"
                 " le nombre de clients qui quittent leurs services "
                 "de carte de crédit. Il aimerait pouvoir anticiper "
                 "le départ des clients afin de leur fournir de meilleurs"
                 " services et ainsi les retenir. Votre travail sera "
                 "de mettre en place un modèle de Machine Learning "
                 "capable de prédire les départs des clients. Pour cela, "
                 "la banque met à votre disposition une base "
                 "de données de 10127 clients. La variable cible est"
                 " Attrition_Flag.")

        st.image("bg-img.jpg")

    elif choix == "PREDICTION INDIVIDUELLE":
        predunique()
    elif choix == "PREDICTION MULTIPLE":
        predic_multiple()
    else:
        get_table_download_link()
        #show_explore_page()


if __name__ == '__main__':
    main()