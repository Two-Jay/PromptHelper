import streamlit as st
from .BaseView import BaseView

class NgramPromptOptimization(BaseView):
    @classmethod
    def render(cls):
        st.write("N-gram Prompt Optimization")