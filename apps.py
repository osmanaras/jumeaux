# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:08:52 2021

@author: osman
"""
import streamlit as st
from Tools import *


st.title('Entreprise Jumeaux')


st.write("Vous voulez savoir quels sont les entreprises que ressemble à la vôtre ?")
st.write("**Alors remplissez le formulaire ci-dessous**")

st.header("**Formulaire**")

# Recuperation du job
activite = st.text_input('Secteur d\'Activité :','Ex: Patisserie')

# Recuperation de la ville
region = st.text_input('Région :','Ex: île-de-france')


# Capital
capital = st.number_input('Capital',value=1000.0)

# trouver les entreprises jumeaux
st.header('**Trouver les entreprise Jumeaux**')

if st.button('Chercher'):
    liste_result = search(activite, region, capital)
    
    st.write(liste_result)
