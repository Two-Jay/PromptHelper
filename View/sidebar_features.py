import streamlit as st
from Pipeline.caller.model_catalog import get_all_valid_models, get_model_enum
from shared_dict_key import (
    llm_config, llm_category, hyperparameter, input_api_key, 
    temp, max_t, freq_penalty, pres_penalty, tp
)

def api_key_section(render_component : st.delta_generator.DeltaGenerator = st.sidebar):
    render_component.write("API 키")
    api_key = render_component.text_input("API 키를 입력하세요", value="", type="password")
    if api_key:
        if validate_api_key(api_key, st.session_state[llm_category]):
            st.session_state[input_api_key] = api_key
        else:
            render_component.error("API 키가 올바르지 않습니다.")

def validate_api_key(api_key: str, current_llm_category: str = None):
    if current_llm_category is None:
        return False
    model = get_model_enum(current_llm_category)
    return model.validate_api_key(api_key)

def llm_config_section(render_component : st.delta_generator.DeltaGenerator = st.sidebar, state_manager = st.session_state):
    render_component.write("LLM 설정")
    if llm_config not in state_manager:
        state_manager[llm_config] = {}
    if hyperparameter not in state_manager:
        init_config = {
            temp: float(1),
            tp: float(1),
            max_t: int(100),
            freq_penalty: float(0),
            pres_penalty: float(0)
        }
        state_manager[hyperparameter] = init_config
    llm_category = render_component.selectbox(
        "model", 
        help="api 호출 llm 모델 선택", 
        options=get_all_valid_models(), 
        on_change=lambda: setattr(state_manager, llm_category, state_manager[llm_category])
    )
    temperature = render_component.slider(
        "temperature",
        help="sampling 수행시 온도 조절", 
        min_value=0.0, 
        max_value=2.0, 
        value=state_manager[hyperparameter].get(temp, 1.0), 
        step=0.01,
        on_change=lambda: state_manager[hyperparameter].update({temp: temperature})
    )
    top_p = render_component.slider(
        "top_p", 
        help="top_p 수치", 
        min_value=0.0, 
        max_value=float(1.0), 
        value=state_manager[hyperparameter].get(tp, float(1.0)), 
        step=0.01,
        on_change=lambda: state_manager[hyperparameter].update({tp: top_p})
    )
    max_tokens = render_component.slider(
        "max_tokens", 
        help="최대 토큰 수", 
        min_value=10, 
        max_value=1000, 
        value=state_manager[hyperparameter].get(max_t, int(100)), 
        step=10,
        on_change=lambda: state_manager[hyperparameter].update({max_t: max_tokens})
    )
    frequency_penalty = render_component.slider(
        "frequency_penalty", 
        help="빈번한 단어 사용 제약", 
        min_value=0.0, 
        max_value=2.0, 
        value=state_manager[hyperparameter].get(freq_penalty, float(0.0)), 
        step=0.01,
        on_change=lambda: state_manager[hyperparameter].update({freq_penalty: frequency_penalty})
    )
    presence_penalty = render_component.slider(
        "presence_penalty",
        help="단어 존재 제약", 
        min_value=0.0, 
        max_value=2.0, 
        value=state_manager[hyperparameter].get(pres_penalty, float(0.0)), 
        step=0.01,
        on_change=lambda: state_manager[hyperparameter].update({pres_penalty: presence_penalty})
    )