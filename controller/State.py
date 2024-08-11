import streamlit as st
from typing import Any

class State:
    @staticmethod
    def get(key: str, default_value: Any = None, is_overwrite: bool = False) -> Any:
        if key not in st.session_state:
            st.session_state[key] = default_value
        return st.session_state[key]

    @staticmethod
    def set(key: str, value: Any) -> None:
        st.session_state[key] = value
