import streamlit as st
from Pipeline.caller.model_catalog import get_all_valid_models

def api_key_section(render_component : st.delta_generator.DeltaGenerator = st.sidebar):
    render_component.write("API 키")
    api_key = render_component.text_input("API 키를 입력하세요", value="", type="password")
    if api_key:
        if validate_api_key(api_key, st.session_state['llm_category']):
            st.session_state['api_key'] = api_key
        else:
            render_component.error("API 키가 올바르지 않습니다.")

def validate_api_key(api_key: str, current_llm_category: str = None):
    if current_llm_category is None:
        return False
    if api_key == "1234":
        return True
    return False

def llm_config_section(render_component : st.delta_generator.DeltaGenerator = st.sidebar, state_manager = st.session_state):
    render_component.write("LLM 설정")
    llm_category = render_component.selectbox("모델 선택", options=get_all_valid_models())
    temperature = render_component.slider("테스트 온도", min_value=0.0, max_value=2.0, value=float(1), step=0.01)
    top_p = render_component.slider("top_p", min_value=0.0, max_value=float(1.0), value=float(1.0), step=0.01)
    max_tokens = render_component.slider("최대 토큰 수", min_value=10, max_value=1000, value=int(100), step=10)
    state_manager.llm_category = llm_category
    state_manager.temperature = temperature
    state_manager.max_tokens = max_tokens
    state_manager.top_p = top_p