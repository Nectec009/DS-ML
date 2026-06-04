import streamlit as st

st.set_page_config(page_title="MyApp", layout="wide")

st.title("🏠 หน้าหลัก ")
st.write("### Boot Camp: Data Science and Machine Learning")
st.info("7 Day Intensive Hands-on Workshop")
st.write("Nectec")
st.write("##### Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
    st.switch_page("pages/app1_discount_calc.py")
elif st.button("💰 ทำความสะอาดของอาจารย์"):
    st.switch_page("pages/clean_customers.py")
elif st.button("💰 ทำความสะอาดของผม"):
    st.switch_page("pages/clean_appNectec.py")
elif st.button("💰 ทำความสะอาดของผม1"):
    st.switch_page("pages/clean_appNectec1.py")
elif st.button("💰 transform"):
    st.switch_page("pages/transform_app.py")
elif st.button("💰 EDA APP"):
    st.switch_page("pages/EDA_app.py")
elif st.button("💰 sale_predict"):
    st.switch_page("pages/sale_predict.py")
elif st.button("💰 truck_predict"):
    st.switch_page("pages/truck_predict.py")
