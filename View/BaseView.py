import streamlit as st
from Controller.State import State
from typing import Any

class BaseView:
    state_manager = State
    @classmethod
    def render(cls):
        pass

    @classmethod
    def get_state(cls, key: str, default_value: Any = None, is_overwrite: bool = False) -> Any:
        return cls.state_manager.get(key, default_value, is_overwrite)

    @classmethod
    def set_state(cls, key: str, value: Any) -> None:
        cls.state_manager.set(key, value)

    @classmethod
    def __getitem__(cls, key: str) -> Any:
        return cls.state_manager.get(key)

    @classmethod
    def __setitem__(cls, key: str, value: Any) -> None:
        cls.state_manager.set(key, value)