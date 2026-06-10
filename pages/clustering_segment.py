import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Tactical Market Segmentation",
    page_icon="🎯",
    layout="wide"
)

# ================= CSS STYLE =================
st.markdown("""
<style>
/* พื้นหลังแนว Tactical Game */
.stApp {
    background:
        linear-gradient(rgba(0, 0, 0, 0.78), rgba(0, 0, 0, 0.88)),
        radial-gradient(circle at 15% 20%, rgba(34,197,94,0.25), transparent 28%),
        radial-gradient(circle at 85% 30%, rgba(245,158,11,0.18), transparent 30%),
        linear-gradient(135deg, #020617 0%, #0F1F13 45%, #000000 100%);
    color: #E5E7EB;
}

/* ซ่อน menu/footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* กล่อง Header */
.hero-box {
    padding: 32px 28px;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(22,101,52,0.85), rgba(2,6,23,0.95));
    border: 1px solid rgba(132,204,22,0.75);
    box-shadow: 0 0 35px rgba(34,197,94,0.25);
    margin-bottom: 25px;
    position: relative;
}

.hero-title {
    font-size: 46px;
    font-weight: 900;
    color: #A3E635;
    text-shadow: 0 0 16px rgba(163,230,53,0.85);
    letter-spacing: 1px;
}

.hero-subtitle {
    font-size: 19px;
    color: #FDBA74;
    margin-top: 8px;
}

.hero-desc {
    font-size: 15px;
    color: #D1D5DB;
    margin-top: 10px;
}

/* แถบ Mission */
.mission-bar {
    padding: 12px 18px;
    border-radius: 14px;
    background: rgba(2,6,23,0.88);
    border-left: 5px solid #F97316;
    border-right: 1px solid rgba(249,115,22,0.45);
    color: #FDBA74;
    font-weight: 700;
    margin-bottom: 25px;
}

/* Section Card */
.section-card {
    padding: 22px;
    border-radius: 20px;
    background: rgba(15,23,42,0.88);
    border: 1px solid rgba(132,204,22,0.45);
    box-shadow: 0 0 20px rgba(34,197,94,0.16);
    margin-bottom: 18px;
}

/* Input Zone */
.input-card {
    padding: 20px;
    border-radius: 18px;
    background: linear-gradient(145deg, rgba(3,7,18,0.95), rgba(20,83,45,0.45));
    border: 1px solid rgba(74,222,128,0.35);
    box-shadow: inset 0 0 20px rgba(34,197,94,0.08);
}

/* หัวข้อ */
h1, h2, h3 {
    color: #A3E635 !important;
}

[data-testid="stMarkdownContainer"] p {
    color: #E5E7EB;
}

/* ปุ่ม */
.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid #A3E635;
    background: linear-gradient(90deg, #052E16, #111827);
    color: #A3E635;
    font-weight: 900;
    padding: 14px 20px;
    box-shadow: 0 0 14px rgba(132,204,22,0.28);
    transition: 0.25s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #A3E635, #F97316);
    color: #020617;
    border: 1px solid #FFFFFF;
    box-shadow: 0 0 28px rgba(163,230,53,0.75);
    transform: scale(1.01);
}

/* Metric Card */
.metric-card {
    padding: 18px;
    border-radius: 18px;
    background: rgba(2,6,23,0.90);
    border: 1px solid rgba(249,115,22,0.45);
    box-shadow: 0 0 18px rgba(249,115,22,0.18);
    text-align: center;
}

.metric-title {
    color: #FDBA74;
    font-size: 14px;
    margin-bottom: 6px;
}

.metric-value {
    color: #A3E635;
    font-size: 28px;
    font-weight: 900;
    text-shadow: 0 0 12px rgba(163,230,53,0.8);
}

/* Result Box */
.result-box {
    padding: 26px;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(20,83,45,0.88), rgba(2,6,23,0.95));
    border: 1px solid rgba(163,230,53,0.75);
    box-shadow: 0 0 30px rgba(34,197,94,0.25);
    margin-top: 20px;
}

.cluster-title {
    font-size: 30px;
    color: #A3E635;
    font-weight: 900;
    text-shadow: 0 0 14px rgba(163,230,53,0.9);
}

.cluster-desc {
    font-size: 16px;
    color: #E5E7EB;
    margin-top: 10px;
}

/* เส้นแบ่ง */
.tactical-line {
    height: 2px;
    background: linear-gradient(90deg, transparent, #A3E635, #F97316, transparent);
    margin: 22px 0 28px 0;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #052E16);
    border-right: 1px solid rgba(163,230,53,0.35);
}
</style>
""", unsafe_allow_html=True)


# ================= HEADER =================
st.markdown("""
<div class="hero-box">
    <div class="hero-title">🎯 TACTICAL MARKET OPS</div>
    <div class="hero-subtitle">Market Segmentation Predictor | K-Means Intelligence System</div>
    <div class="hero-desc">
        ระบบวิเคราะห์และจัดกลุ่มลูกค้าในรูปแบบศูนย์บัญชาการ Tactical Dashboard
    </div>
</div>

<div class="mission-bar">
    🟢 MISSION STATUS: READY | วิเคราะห์ Units Sold, Marketing Spend, Logistics Delay, Customer Score และ Revenue
</div>
""", unsafe_allow_html=True)


# ================= LOAD MODEL =================
try:
    kmeans_loaded = joblib.load("model/kmeans_redbull.pkl")
    scaler_loaded = joblib.load("model/scaler_redbull.pkl")
    st.sidebar.success("✅ โหลดโมเดล K-Means และ Scaler สำเร็จ")
except FileNotFoundError:
    st.error(
        "❌ ไม่พบไฟล์ `kmeans_redbull.pkl` หรือ `scaler_redbull.pkl` "
        "กรุณาตรวจสอบว่าไฟล์อยู่ในโฟลเดอร์ `model/`"
    )
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
    <h3>🪖 Mission Input: ป้อนข้อมูลลูกค้า</h3>
    <p>กรอกข้อมูลเพื่อให้ระบบวิเคราะห์ว่าอยู่ในกลุ่มลูกค้าประเภทใด</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='input-card'>", unsafe_allow_html=True)
    units_sold = st.number_input(
        "🎯 Units Sold",
        min_value=0,
        value=150000
    )

    marketing_spend = st.number_input(
        "📡 Marketing Spend",
        min_value=0,
        value=100000
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='input-card'>", unsafe_allow_html=True)
    customer_score = st.slider(
        "⭐ Customer Score",
        min_value=1,
        max_value=99,
        value=50
    )

    logistics_delay = st.number_input(
        "🚚 Logistics Delay (days)",
        min_value=0,
        value=30
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='input-card'>", unsafe_allow_html=True)
    unit_price = st.number_input(
        "💵 Unit Price",
        min_value=0.0,
        value=35.0,
        format="%.2f"
    )

    revenue = units_sold * unit_price

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Calculated Revenue</div>
        <div class="metric-value">{revenue:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ================= IMPORTANT FIX =================
# ต้องเรียงข้อมูลให้ตรงกับ features:
# Units_Sold, Marketing_Spend, Logistics_Delay, Customer_Score, Revenue
new_data_input = pd.DataFrame(
    [[units_sold, marketing_spend, logistics_delay, customer_score, revenue]],
    columns=features
)


# ================= PREVIEW =================
st.markdown("### 🧾 Mission Data Preview")
st.dataframe(new_data_input, use_container_width=True, hide_index=True)


# ================= PREDICTION =================
st.markdown("<div class='tactical-line'></div>", unsafe_allow_html=True)

if st.button("🚀 START MISSION: จัดกลุ่มข้อมูล"):
    if not new_data_input.isnull().values.any():

        scaled_data = scaler_loaded.transform(new_data_input)

        predicted_cluster = kmeans_loaded.predict(scaled_data)[0]

        cluster_info = centroids.loc[predicted_cluster]

        st.markdown(f"""
        <div class="result-box">
            <div class="cluster-title">🎖️ TARGET CLASSIFIED: CLUSTER {predicted_cluster}</div>
            <div class="cluster-desc">
                ระบบวิเคราะห์แล้วว่าข้อมูลนี้ถูกจัดอยู่ในกลุ่ม Cluster {predicted_cluster}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("## 📊 Cluster Intelligence Report")

        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:
            st.metric("Units Sold Avg", f"{cluster_info['Units_Sold']:,.0f}")

        with c2:
            st.metric("Marketing Avg", f"{cluster_info['Marketing_Spend']:,.0f}")

        with c3:
            st.metric("Customer Score", f"{cluster_info['Customer_Score']:,.0f}")

        with c4:
            st.metric("Delay Avg", f"{cluster_info['Logistics_Delay']:,.0f} วัน")

        with c5:
            st.metric("Revenue Avg", f"{cluster_info['Revenue']:,.0f}")

        st.markdown("### 🧠 Tactical Interpretation")

        if predicted_cluster == 0:
            st.info("🟡 Cluster 0 — กลุ่มลูกค้ายอดขายต่ำ / ลูกค้าใหม่")
            st.write(
                "กลุ่มนี้มีลักษณะเด่นคือ Units Sold, Marketing Spend และ Revenue "
                "อยู่ในระดับต่ำกว่ากลุ่ม High-Value ส่วน Customer Score และ Logistics Delay "
                "อยู่ในระดับปานกลาง"
            )
            st.warning(
                "ข้อเสนอแนะ: ควรใช้กลยุทธ์กระตุ้นยอดขาย เช่น โปรโมชันเฉพาะกลุ่ม "
                "เพิ่มการติดตามลูกค้า และวิเคราะห์สาเหตุที่ทำให้ยอดซื้อน้อย"
            )

        elif predicted_cluster == 1:
            st.success("🟢 Cluster 1 — กลุ่มลูกค้ายอดขายสูง / High-Value Customer")
            st.write(
                "กลุ่มนี้มีลักษณะเด่นคือ Units Sold, Marketing Spend และ Revenue "
                "อยู่ในระดับสูง แสดงถึงลูกค้าที่มีมูลค่าสูงหรือมีส่วนร่วมกับธุรกิจมาก"
            )
            st.warning(
                "ข้อเสนอแนะ: ควรรักษาลูกค้ากลุ่มนี้ด้วยสิทธิพิเศษ การดูแลเฉพาะทาง "
                "และลดความล่าช้าด้าน Logistics เพื่อป้องกันการเสียลูกค้าสำคัญ"
            )

    else:
        st.warning("⚠️ กรุณาตรวจสอบการป้อนข้อมูลให้ครบถ้วน")


# ================= FOOTER =================
st.markdown("""
<div class="tactical-line"></div>
<div style="text-align:center; color:#9CA3AF;">
    Boot Camp: Data Science and Machine Learning | Tactical Market Segmentation System
</div>
""", unsafe_allow_html=True)


# ================= BACK HOME =================
if st.button("🏠 กลับหน้าหลัก"):
    st.switch_page("app.py")
