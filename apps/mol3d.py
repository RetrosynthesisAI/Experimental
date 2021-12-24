"""
Retrosynthesis AI - Bioinformatics Explore App
Author: @Margaret Linan 
Created: 12.21.21 
Contributors: None
"""

import streamlit as st
from PIL import Image
from stmol import component_3dmol
from pathlib import Path
import base64
 


# Initial page config

st.set_page_config(
     page_title='Explore',
     layout="wide",
    initial_sidebar_state="expanded",
)


def app():
    #introduction() 
    col1, col2 = st.columns(2)
  
    with col1:
        image1 = Image.open('media/logo.png')
        st.image(image1)
        st.header('Molecular Visualizations')
        st.write('Please visit the Protein DataBank for more structural identifiers that you can input below, try the Structure of human SRSF1 RRM1 bound to AACAAA RNA: **6HPJ** [1]')
        component_3dmol()  
        st.write('Please visit the Protein DataBank for more structural identifiers that you can input below, try the Crystal Structure of Human CRMP2 1-532, AGE-modified: **6JVB** [2]') 
        component_3dmol()
        
    with col2:
        image2 = Image.open('media/empty.png')
        st.image(image2)
        st.header('')
        st.write('')
        st.write('')
        st.write('')
        st.write('Please visit the Protein DataBank for more structural identifiers that you can input below, try the Crystal structure of Lysine Specific Demethylase 1 (LSD1) with TAK-418, FAD-adduct: **7E0G** [3]')
        component_3dmol() 
        st.write('Please visit the Protein DataBank for more structural identifiers that you can input below, try the Crystal Structure of d(G4C2)2-K in F222 space group: **7ECH** [4]')
        component_3dmol()
     
    
    st.subheader('Citations')
    st.write('[1] Clery A, Krepl M, Nguyen C, et al. Structure of SRSF1 RRM1 bound to RNA reveals an unexpected bimodal mode of interaction and explains its involvement in SMN1 exon7 splicing. Nat Commun. 2021. PMID: 33462199')
    st.write('[2] Toyoshima M, Jiang X, Ogawa T, et al. Enhanced carbonyl stress induces irreversible multimerization of CRMP2 in schizophrenia pathogenesis. 2019. Life Sci Alliance. PMID: 31591136')
    st.write('[3] Baba R, Matsuda S, Arakawa Y, et al. LSD1 enzyme inhibitor TAK-418 unlocks aberrant epigenetic machinery and improves autism symptoms in neurodevelopmental disorder models. 2021. Sci Adv. PMID: 33712455')
    st.write('[4] Geng Y, Liu C, Cai Q, et al. Crystal structure of parallel G-quadruplex formed by the two-repeat ALS- and FTD-related GGGGCC sequence. 2021. Nucleic Acids Res. PMID: 34048588')
    st.write('[5] Nicholas Rego and David Koes 3Dmol.js: molecular visualization with WebGL Bioinformatics (2015) 31 (8): 1322-1324 doi:10.1093/bioinformatics/btu829')
    