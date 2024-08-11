import streamlit as st
from .BaseView import BaseView

class MultiTurnPromptScoring(BaseView):
    @classmethod
    def render(cls):
        st.write("Multi-turn Prompt Scoring")
