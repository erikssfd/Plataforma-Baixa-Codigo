# IMPORTANDO BIBLIOTECAS
import streamlit as st
from PIL import Image

# CONFIGURAÇÃO DO APP
st.set_page_config(layout = "wide")

css = "estilo.css"
# ESTILO CSS
with open(css, encoding = "utf8") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)

# LAYOUT
lateral = st.sidebar
container = st.container
projetos = ()

# Utilitários
imagem = Image.open("imagem/linhas.jpg")
perfil = Image.open("imagem/perfil.png")


# PÁGINA DE INICIO
# with container():

# BARRA LATERAL
with lateral:
    st.write("#")
    st.image(perfil)
    st.title("Erik Marta Garcia")
    st.caption("Ciência de Dados | Analista de Dados")
    with open("arquivo/curriculo.pdf", "rb") as arquivo:
        botao = st.download_button(
            label = "Meu Curriculo 	':page_with_curl:'",
            data = arquivo,
            file_name = "Erik Marta Garcia - Currículo.pdf",
            mime = "text/pdf"
        )
        st.divider()
        
# MÍDIAS SOCIAIS
    midia_social = {
        ":computer: GitHub" : "https://github.com/erikssfd",
        ":books: Medium" : "https://medium.com/@erik.martaneva",
        ":male-technologist: LinkedIn" : "https://www.linkedin.com/in/erikmartagarcia/"
    }
    
# RECOLHENDO AS MÍDIAS SOCIAS E AS EXIBINDO
    colmd = st.columns(len(midia_social))
    
    for indice, (plataforma, link) in enumerate(midia_social.items()):
        colmd[indice].write(f"[{plataforma}]({link})")
    
    st.caption(":book: O senhor és meu pastor e nada me faltará! :book:")