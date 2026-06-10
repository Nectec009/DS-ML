import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Market Segmentation Tactical UI",
    page_icon="🟧",
    layout="wide"
)

# ================= UI STYLE แบบภาพตัวอย่าง =================
st.markdown("""
<style>
/* ===== Main Background ===== */
.stApp {
    background: #17172b;
    color: #f5f5ff;
}

/* ซ่อนเมนู Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ===== Font Color ===== */
h1, h2, h3 {
    color: #ff8a00 !important;
    font-weight: 900 !important;
    letter-spacing: 1px;
}

p, label, span, div {
    color: #e8e6ff;
}

/* ===== Header Box ===== */
.main-panel {
    background: #101026;
    border: 2px solid #34254d;
    border-radius: 18px;
    padding: 28px;
    box-shadow: 0 0 20px rgba(255, 111, 0, 0.25);
    margin-bottom: 22px;
}

.app-title {
    font-size: 42px;
    font-weight: 900;
    color: #ff8a00;
    text-shadow: 0 0 12px rgba(255, 120, 0, 0.9);
    margin-bottom: 6px;
}

.app-subtitle {
    color: #00ff66;
    font-size: 18px;
    font-weight: 800;
    text-shadow: 0 0 8px rgba(0, 255, 100, 0.7);
}

.app-desc {
    color: #bdb8d9;
    font-size: 15px;
}

/* ===== Section Card ===== */
.section-card {
    background: #101026;
    border: 2px solid #32244c;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 18px;
    box-shadow: 0 0 18px rgba(62, 43, 91, 0.45);
}

/* ===== Input Card ===== */
.input-card {
    background: #0c0b22;
    border: 2px solid #32244c;
    border-radius: 15px;
    padding: 18px;
    min-height: 165px;
    box-shadow: inset 0 0 12px rgba(255, 100, 0, 0.08);
}

/* ===== ปุ่ม Streamlit ===== */
.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: none;
    background: linear-gradient(180deg, #ffb000 0%, #ff7a00 45%, #ff3d00 100%);
    color: white;
    font-weight: 900;
    letter-spacing: 1px;
    padding: 13px 20px;
    box-shadow:
        inset 0 2px 4px rgba(255,255,255,0.45),
        0 0 14px rgba(255, 111, 0, 0.55);
    transition: 0.2s;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(180deg, #ffd000 0%, #ff8a00 45%, #ff3300 100%);
    color: #ffffff;
    box-shadow:
        inset 0 2px 4px rgba(255,255,255,0.55),
        0 0 24px rgba(255, 120, 0, 0.95);
}

/* ===== Input Box ===== */
.stNumberInput input {
    background: #0c0b22 !important;
    color: #ffffff !important;
    border: 2px solid #32244c !important;
    border-radius: 10px !important;
}

.stSlider {
    color: #ff8a00 !important;
}

/* ===== Metric Card ===== */
.metric-card {
    background: #0c0b22;
    border: 2px solid #32244c;
    border-radius: 15px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 0 14px rgba(255, 111, 0, 0.18);
}

.metric-title {
    color: #bdb8d9;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 6px;
}

.metric-value {
    color: #ff8a00;
    font-size: 28px;
    font-weight: 900;
    text-shadow: 0 0 10px rgba(255, 120, 0, 0.8);
}

/* ===== Result Box ===== */
.result-success {
    background: #0c0b22;
    border: 2px solid #32244c;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 0 20px rgba(0, 255, 100, 0.22);
}

.success-title {
    color: #00ff66;
    font-size: 28px;
    font-weight: 900;
    text-shadow: 0 0 10px rgba(0, 255, 100, 0.8);
}

.warning-title {
    color: #ff7a00;
    font-size: 28px;
    font-weight: 900;
    text-shadow: 0 0 10px rgba(255, 120, 0, 0.8);
}

/* ===== เส้นแบ่ง ===== */
.neon-line {
    height: 8px;
    border-radius: 20px;
    background: linear-gradient(90deg, #ff3d00, #ffb000, #ff3d00);
    box-shadow: 0 0 12px rgba(255, 120, 0, 0.8);
    margin: 20px 0 26px 0;
}

/* ===== Sidebar ===== */
[data-testid="stSidebar"] {
    background: #101026;
    border-right: 2px solid #32244c;
}

/* ===== Dataframe ===== */
[data-testid="stDataFrame"] {
    border: 2px solid #32244c;
    border-radius: 15px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)


# ================= HEADER =================
st.markdown("""
<div class="main-panel">
    <div class="app-title">MARKET SEGMENTATION COMMAND</div>
    <div class="app-subtitle">SUCCESS! SYSTEM READY</div>
    <div class="app-desc">
        ระบบจัดกลุ่มลูกค้าด้วย K-Means ในสไตล์ Dark Neon Tactical UI
    </div>
</div>
<div class="neon-line"></div>
""", unsafe_allow_html=True)


# ================= LOAD MODEL =================
try:
    kmeans_loaded = joblib.load("model/kmeans_redbull.pkl")
    scaler_loaded = joblib.load("model/scaler_redbull.pkl")
    st.sidebar.success("✅ โหลดโมเดล K-Means และ Scaler สำเร็จ")
except FileNotFoundError:
    st.error("❌ ไม่พบไฟล์ kmeans_redbull.pkl หรือ scaler_redbull.pkl ในโฟลเดอร์ model")
    st.stop()
except Exception as e:
    st.error(f"❌ โหลดโมเดลไม่สำเร็จ: {e}")
    st.stop()


# ================= FEATURES =================
features = [
    "Units_Sold",
    "Marketing_Spend",
    "Logistics_Delay",
    "Customer_Score",
    "Revenue"
]


# ================= CENTROIDS =================
centroids_data = {
    "Units_Sold": [94217.67, 224432.27],
    "Marketing_Spend": [101039.83, 200408.08],
    "Customer_Score": [49.97, 50.60],
    "Logistics_Delay": [44.85, 44.13],
    "Revenue": [3523438.42, 8562793.71]
}

centroids = pd.DataFrame(centroids_data, index=[0, 1])
centroids.index.name = "Cluster"


# ================= INPUT SECTION =================
st.markdown("""
<div class="section-card">
    <h3>INPUT IN ACTION</h3>
    <p>กรุณาป้อนข้อมูลลูกค้าเพื่อให้ระบบวิเคราะห์กลุ่ม</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='input-card'>", unsafe_allow_html=True)
    units_sold = st.number_input(
        "Units Sold",
        min_value=0,
        value=150000
    )

    marketing_spend = st.number_input(
        "Marketing Spend",
        min_value=0,
        value=100000
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='input-card'>", unsafe_allow_html=True)
    logistics_delay = st.number_input(
        "Logistics Delay (days)",
        min_value=0,
        value=30
    )

    customer_score = st.slider(
        "Customer Score",
        min_value=1,
        max_value=99,
        value=50
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='input-card'>", unsafe_allow_html=True)
    unit_price = st.number_input(
        "Unit Price",
        min_value=0.0,
        value=35.0,
        format="%.2f"
    )

    revenue = units_sold * unit_price

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">REVENUE</div>
        <div class="metric-value">{revenue:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ================= DATA PREVIEW =================
new_data_input = pd.DataFrame(
    [[units_sold, marketing_spend, logistics_delay, customer_score, revenue]],
    columns=features
)

st.markdown("### DATA PREVIEW")
st.dataframe(new_data_input, use_container_width=True, hide_index=True)


# ================= PREDICTION =================
if st.button("BUTTON  |  จัดกลุ่มข้อมูล"):
    if not new_data_input.isnull().values.any():

        scaled_data = scaler_loaded.transform(new_data_input)
        predicted_cluster = kmeans_loaded.predict(scaled_data)[0]
        cluster_info = centroids.loc[predicted_cluster]

        if predicted_cluster == 0:
            result_title = "WARNING!"
            result_class = "warning-title"
            result_text = "Cluster 0 - กลุ่มลูกค้ายอดขายต่ำ / ลูกค้าใหม่"
            result_detail = (
                "กลุ่มนี้มี Units Sold, Marketing Spend และ Revenue อยู่ในระดับต่ำ "
                "ควรใช้กลยุทธ์เพิ่มยอดขาย โปรโมชัน และติดตามลูกค้าให้มากขึ้น"
            )
        else:
            result_title = "SUCCESS!"
            result_class = "success-title"
            result_text = "Cluster 1 - กลุ่มลูกค้ายอดขายสูง / High-Value"
            result_detail = (
                "กลุ่มนี้มี Units Sold, Marketing Spend และ Revenue อยู่ในระดับสูง "
                "ควรรักษาลูกค้ากลุ่มนี้ด้วยบริการพิเศษและลดความล่าช้าในการจัดส่ง"
            )

        st.markdown(f"""
        <div class="result-success">
            <div class="{result_class}">{result_title}</div>
            <p><b>{result_text}</b></p>
            <p>{result_detail}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### CLUSTER DETAIL")

        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">UNITS SOLD</div>
                <div class="metric-value">{cluster_info['Units_Sold']:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">MARKETING</div>
                <div class="metric-value">{cluster_info['Marketing_Spend']:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">SCORE</div>
                <div class="metric-value">{cluster_info['Customer_Score']:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">DELAY</div>
                <div class="metric-value">{cluster_info['Logistics_Delay']:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)

        with c5:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">REVENUE</div>
                <div class="metric-value">{cluster_info['Revenue']:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.warning("กรุณาตรวจสอบการป้อนข้อมูลให้ครบถ้วน")


# ================= FOOTER =================
st.markdown("""
<div class="neon-line"></div>
<div style="text-align:center; color:#77708f;">
    Boot Camp: Data Science and Machine Learning
</div>
""", unsafe_allow_html=True)


# ================= BACK HOME =================
if st.button("🏠 กลับหน้าหลัก"):
    st.switch_page("app.py")
