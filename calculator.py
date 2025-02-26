import streamlit as st

if 'current_input' not in st.session_state:
    st.session_state.current_input = ""

def add_to_input(value):
    st.session_state.current_input += str(value)

def clear_input():
    st.session_state.current_input = ""

def calculate_result():
    try:
        result = eval(st.session_state.current_input)
        st.session_state.current_input = str(result)
    except:
        st.session_state.current_input = "エラー"

st.title("電卓")
st.markdown(f'<div class="calculator-display">{st.session_state.current_input}</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button('1', key='1', on_click=add_to_input, args=(1,)):
        pass
    if st.button('4', key='4', on_click=add_to_input, args=(4,)):
        pass
    if st.button('7', key='7', on_click=add_to_input, args=(7,)):
        pass
    if st.button('C', key='C', on_click=clear_input):
        pass

with col2:
    if st.button('2', key='2', on_click=add_to_input, args=(2,)):
        pass
    if st.button('5', key='5', on_click=add_to_input, args=(5,)):
        pass
    if st.button('8', key='8', on_click=add_to_input, args=(8,)):
        pass
    if st.button('0', key='0', on_click=add_to_input, args=(0,)):
        pass

with col3:
    if st.button('3', key='3', on_click=add_to_input, args=(3,)):
        pass
    if st.button('6', key='6', on_click=add_to_input, args=(6,)):
        pass
    if st.button('9', key='9', on_click=add_to_input, args=(9,)):
        pass
    if st.button('=', key='=', on_click=calculate_result):
        pass

with col4:
    if st.button('⁺', key='+', on_click=add_to_input, args=('+',)):
        pass
    if st.button('⁻', key='-', on_click=add_to_input, args=('-',)):
        pass
    if st.button('×', key='*', on_click=add_to_input, args=('*',)):
        pass
    if st.button('÷', key='/', on_click=add_to_input, args=('/',)):
        pass

st.markdown(
    """
    <style>

        div.stButton > button:first-child {
            color: white;
            border: 1px solid white;
            border-radius: 5px;
            background-color: rgb(204, 49, 49);
            cursor:pointer;
            transition: .1s;
        }

        div.stButton > button:first-child:hover {
            color: white;
            border: 1px solid white;
            border-radius: 5px;
            background-color: rgb(250, 80, 80);
        }

        .calculator-display {
            color: white;
            width: 81%;
            height: 80px;
            padding: 10px;
            font-size: 36px;
            text-align: right;
            margin-bottom: 10px;
            border: 1px solid white;
            border-radius: 5px;
        }        

    </style>
    """,
    unsafe_allow_html=True
)
