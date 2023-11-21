# IMPORTANDO BIBLIOTECAS
import streamlit as st
import pandas as pd
from PIL import Image

# CONFIGURAÇÃO DO APP
st.set_page_config(layout= "wide", page_icon = ":bar_chart:", page_title = "Portfólio - Ciência de Dados")

css = "estilo.css"
# ESTILO CSS
with open(css, encoding = "utf8") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)

# LAYOUT
lateral = st.sidebar
container = st.container

# Utilitários
imagem = Image.open("imagem/linhas.jpg")
perfil = Image.open("imagem/perfil.png")


# PÁGINA DE INICIO
# with container():

# BARRA LATERAL
with lateral:
    st.write("##")
    st.image(perfil, width = 220)
    st.title("Erik Marta Garcia")
    st.subheader("Cientista de Dados | Engenheiro de Dados | Analista de Dados")
    st.caption("Auxiliando empresas em tomadas de decisões com tecnologia e análises")
    
    with st.expander("Baixe meu currículo!"):
         with open("arquivo/curriculo.pdf", "rb") as arquivo:
            botao = st.download_button(
            label = "Curriculo 	':page_with_curl:'",
            data = arquivo,
            file_name = "Erik Marta Garcia - Currículo.pdf",
            mime = "text/pdf"
        )
            
    with st.expander("Mídias Sociais"):
            
# MÍDIAS SOCIAIS
        midia_social = {
        ":computer: GitHub" : "https://github.com/erikssfd",
        ":books: Medium" : "https://medium.com/@erik.martaneva",
        ":male-technologist: LinkedIn" : "https://www.linkedin.com/in/erikmartagarcia/"
        }
        
        colmd = st.columns(len(midia_social))
        for indice, (plataforma, link) in enumerate(midia_social.items()):
            colmd[indice].write(f"[{plataforma}]({link})")
    
    st.caption(":orange[O senhor é meu pastor e nada me faltará!]")
    
# PÁGINA INCIAL

with container():
    st.write("### Projetos")
    
    tab1, tab2, tab3 = st.tabs([":computer: Amazon", ":computer: Coursera", ":computer: Udemy"])
    
    # PROJETO AMAZON
    with tab1:
        
        
        st.image("imagem/logo-amazon.png", width = 280)
        st.image("imagem/exemplo-dash.jpg")
        st.divider()
        col1, col2, col3 = st.columns(3)
        col1.link_button("Github", "https://github.com/erikssfd/AmzonDashboard", type = "primary")
        col2.link_button("Medium", "https://github.com/erikssfd/AmzonDashboard", type = "primary")
        
        with col3.expander("Ferramentas Utilizadas"):
            subcol1, subcol2, subcol3 = st.columns([2,2,2])
            
            subcol1.image("imagem/python-logo.png", width = 40)
            subcol2.image("imagem/powerbi-logo.png", width = 40)
            subcol3.image("imagem/tableau-logo.png", width = 60)