from enum import Enum
import streamlit as st
from typing import List
from dataclasses import dataclass
from View.prompt_scoring import PromptScoring
from View.multi_turn_prompt_scoring import MultiTurnPromptScoring
from View.ngram_prompt_optimization import NgramPromptOptimization

@dataclass
class PageInfo:
    name: str
    caller: callable

class Pages(Enum):
    prompt_scoring = PageInfo("prompt_scoring", PromptScoring.render)
    multi_turn_prompt_scoring = PageInfo("multi_turn_prompt_scoring", MultiTurnPromptScoring.render)
    ngram_prompt_optimization = PageInfo("ngram_prompt_optimization", NgramPromptOptimization.render)

    @property
    def name(self):
        return self.value.name

    @property
    def caller(self):
        return self.value.caller

    @staticmethod
    def get_pages_list() -> List[str]:
        return [page.name for page in Pages] 

class Sidebar:
    def __init__(self):
        self._selected_page = st.sidebar.selectbox("Select a page", Pages.get_pages_list(), index=0)

    def get_selected_page(self):
        return self._selected_page

    def render(self):
        for page in Pages:
            if page.name == self.get_selected_page():
                page.caller()

__all__ = ["Sidebar"]

