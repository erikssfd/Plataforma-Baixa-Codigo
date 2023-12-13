# IMPORTANDO BIBLIOTECAS
import streamlit as st
import pandas as pd
from PIL import Image

# CONFIGURAÇÃO DO APP
st.set_page_config(layout = "wide", page_icon = ":bar_chart:", page_title = "Portfólio - Ciência de Dados",)

# ESTILO CSS
css = "estilo.css"
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
    st.subheader("Cientista de Dados")
    st.caption("Auxiliando empresas a realizar decisões com tecnologia e análises")
    
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
        ":computer: Projetos" : "https://github.com/erikssfd",
        ":books: Artigos" : "https://medium.com/@erik.martaneva",
        ":male-technologist: LinkedIn" : "https://www.linkedin.com/in/erikmartagarcia/"
        }
        
        colmd = st.columns(len(midia_social))
        for indice, (plataforma, link) in enumerate(midia_social.items()):
            colmd[indice].write(f"[{plataforma}]({link})")
    
    st.caption(":green[O senhor é meu pastor e nada me faltará!]")
    
# PÁGINA INCIAL
with container():
    # TÍTULO PÁGINA OFICIAL
    st.write("### Projetos")
    
    # CRIAÇÃO DAS ABAS DOS PROJETOS (LOGO) & (TITULO DO PROJETO)
    tab1, tab2 = st.tabs([":computer: Análises Exploratórias", ":computer: Machine Learning"])
    
# PROJETO AMAZON

    # ESTILIZAÇÃO DA COLUNA 1
    #with tab1:
    