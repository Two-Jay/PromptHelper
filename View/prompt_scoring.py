import streamlit as st
from .BaseView import BaseView

class PromptScoring(BaseView):
    @classmethod
    def render(cls):
        st.write("Prompt Scoring")