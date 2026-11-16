# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:43:32 2026

@author: tomas
"""

import streamlit as st

st.markdown(
    """
    <style>
    
  
    .stApp {
        background-color: #12151C;
        color: #FFFFFF;
        text-alignment="center"
    }

    /* 2. Muda o fundo e a borda das caixas (st.container) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #1B202B;
        border: 5px solid #2E3646;
        border-radius: 12px;
    }


    div.stButton > button[kind="primary"] {
        background-color: #00E676;      /* Verde vibrante */
        color: #000000;                 /* Texto preto para alto contraste */
        border: none;
        border-radius: 8px;
        height: 100px;
        width: 100px;
        font-size: 16px;
        font-weight: 800;
        font-size: 500;
        letter-spacing: 5px;
    }

    div.stButton > button[kind="primary"]:hover {
        background-color: #00C853;
    

    }
    
    
    }
    </style>
    """,
    
    unsafe_allow_html=True,
)

if "game_on" not in st.session_state:
  st.session_state.game_on = False
    
border = st.container()

border.title("Burguer Hunting Game")

border.write("Whoever reaches the burguer first wins!!")
border.write("Characters move upon voice commands")

if not st.session_state.game_on:
    
    start = border.button("START",type="primary")

    if start:
        st.session_state.game_on = True
        st.rerun()


else:
   
    N=6
    board = st.container(border=True)
    board.title("Let's play")
