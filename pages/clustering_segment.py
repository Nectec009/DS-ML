import streamlit as st
import pandas as pd
import joblib

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Market Segmentation Tactical UI",
    page_icon="🟧",
    layout="wide"
)


# =====================================================
# THEME SWITCHER
# =====================================================
themes = {
    "orange": {
        "name": "🟧 ORANGE NEON",
        "bg": "#17172b",
        "panel": "#101026",
        "card": "#0c0b22",
        "border": "#32244c",
        "primary": "#ff8a00",
        "secondary": "#ff3d00",
        "success": "#00ff66",
        "warning": "#ff8a00",
        "text": "#e8e6ff",
        "muted": "#bdb8d9"
    },
    "green": {
        "name": "🟩 TACTICAL GREEN",
        "bg": "#07130c",
        "panel": "#0b1f12",
        "card": "#06150c",
        "border": "#1f6f3a",
        "primary": "#a3e635",
        "secondary": "#22c55e",
        "success": "#00ff66",
        "warning": "#facc15",
        "text": "#eaffea",
        "muted": "#b7c7b7"
    },
    "blue": {
        "name": "🟦 CYBER BLUE",
        "bg": "#071225",
        "panel": "#0b1b33",
        "card": "#06101f",
        "border": "#1e3a8a",
        "primary": "#38bdf8",
        "secondary": "#2563eb",
        "success": "#00ffcc",
        "warning": "#facc15",
        "text": "#e0f2fe",
        "muted": "#a9c4d8"
    },
    "purple": {
        "name": "🟪 GALAXY PURPLE",
        "bg": "#160b2e",
        "panel": "#21113f",
        "card": "#120824",
        "border": "#6d28d9",
        "primary": "#c084fc",
        "secondary": "#7c3aed",
        "success": "#22ff88",
        "warning": "#f59e0b",
        "text": "#f3e8ff",
        "muted": "#c4b5fd"
    }
}

if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "orange"

theme_keys = list(themes.keys())

with st.sidebar:
    st.markdown("## 🎨 THEME CONTROL")
    st.info(f"Current Theme: {themes[st.session_state.theme_mode]['name']}")

    if st.button("🔄 SWITCH COLOR THEME", use_container_width=True):
        current_index = theme_keys.index(st.session_state.theme_mode)
        next_index = (current_index + 1) % len(theme_keys)
        st.session_state.theme_mode = theme_keys[next_index]
        st.rerun()

theme = themes[st.session_state.theme_mode]


# =====================================================
# CSS STYLE
# =====================================================
st.markdown(f"""
<style>
:root {{
    --bg: {theme['bg']};
    --panel: {theme['panel']};
    --card: {theme['card']};
    --border: {theme['border']};
    --primary: {theme['primary']};
    --secondary: {theme['secondary']};
    --success: {theme['success']};
    --warning: {theme['warning']};
    --text: {theme['text']};
    --muted: {theme['muted']};
}}

/* ===== Main Background ===== */
.stApp {{
    background:
        radial-gradient(circle at 10% 15%, color-mix(in srgb, var(--primary) 22%, transparent), transparent 25%),
        radial-gradient(circle at 90% 15%, color-mix(in srgb, var(--secondary) 18%, transparent), transparent 28%),
        linear-gradient(135deg, var(--bg), #05050f);
    color: var(--text);
}}

/* Hide Streamlit Default UI */
#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

/* Text */
h1, h2, h3 {{
    color: var(--primary) !important;
    font-weight: 900 !important;
    letter-spacing: 1px;
}}

p, label, span {{
    color: var(--text);
}}

/* Sidebar */
[data-testid="stSidebar"] {{
    background: var(--panel);
    border-right: 2px solid var(--border);
}}

/* Header Panel */
.main-panel {{
    background: var(--panel);
    border: 2px solid var(--border);
    border-radius: 18px;
    padding: 28px;
    box-shadow: 0 0 22px color-mix(in srgb, var(--primary) 65%, transparent);
    margin-bottom: 22px;
}}

.app-title {{
    font-size: 44px;
    font-weight: 900;
    color: var(--primary);
    text-shadow: 0 0 14px var(--primary);
    margin-bottom: 6px;
}}

.app-subtitle {{
    color: var(--success);
    font-size: 18px;
    font-weight: 900;
    text-shadow: 0 0 8px var(--success);
}}

.app-desc {{
    color: var(--muted);
    font-size: 15px;
    margin-top: 8px;
}}

/* Section Card */
.section-card {{
    background: var(--panel);
    border: 2px solid var(--border);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 18px;
    box-shadow: 0 0 18px color-mix(in srgb, var(--border) 75%, transparent);
}}

/* Input Card */
.input-card {{
    background: var(--card);
    border: 2px solid var(--border);
    border-radius: 15px;
    padding: 18px;
    min-height: 175px;
    box-shadow: inset 0 0 14px color-mix(in srgb, var(--primary) 25%, transparent);
}}

/* Buttons */
.stButton > button {{
    width: 100%;
    border-radius: 14px;
    border: none;
    background: linear-gradient(180deg, var(--primary) 0%, var(--secondary) 100%);
    color: white;
    font-weight: 900;
    letter-spacing: 1px;
    padding: 13px 20px;
    box-shadow:
        inset 0 2px 4px rgba(255,255,255,0.35),
        0 0 16px color-mix(in srgb, var(--primary) 80%, transparent);
    transition: 0.20s;
}}

.stButton > button:hover {{
    transform: scale(1.02);
    filter: brightness(1.15);
    color: white;
    box-shadow:
        inset 0 2px 4px rgba(255,255,255,0.45),
        0 0 28px var(--primary);
}}

/* Input Box */
.stNumberInput input {{
    background: var(--card) !important;
    color: var(--text) !important;
    border: 2px solid var(--border) !important;
    border-radius: 10px !important;
}}

.stSlider {{
    color: var(--primary) !important;
}}

/* Metric Card */
.metric-card {{
    background: var(--card);
    border: 2px solid var(--border);
    border-radius: 15px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 0 16px color-mix(in srgb, var(--primary) 45%, transparent);
}}

.metric-title {{
    color: var(--muted);
    font-size: 13px;
    font-weight: 900;
    margin-bottom: 6px;
}}

.metric-value {{
    color: var(--primary);
    font-size: 27px;
    font-weight: 900;
    text-shadow: 0 0 10px var(--primary);
}}

/* Result Box */
.result-box {{
    background: var(--card);
    border: 2px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 0 22px color-mix(in srgb, var(--success) 45%, transparent);
    margin-bottom: 18px;
}}

.success-title {{
    color: var(--success);
    font-size: 30px;
    font-weight: 900;
    text-shadow: 0 0 10px var(--success);
}}

.warning-title {{
    color: var(--warning);
    font-size: 30px;
    font-weight: 900;
    text-shadow: 0 0 10px var(--warning);
}}

/* Neon Line */
.neon-line {{
    height: 8px;
    border-radius: 20px;
    background: linear-gradient(90deg, var(--secondary), var(--primary), var(--secondary));
    box-shadow: 0 0 14px var(--primary);
    margin: 20px 0 26px 0;
}}

/* Dataframe */
[data-testid="stDataFrame"] {{
    border: 2px solid var(--border);
    border-radius: 15px;
    overflow: hidden;
}}

/* Alert Box Adjustment */
.stAlert {{
    border-radius: 14px;
}}
</style>
""", unsafe_allow_html=True)


# =====================================================
# HEADER
# =====================================================
st.markdown("""
<div class="main-panel">
    <div class="app-title">MARKET SEGMENTATION COMMAND</div>
    <div class="app-subtitle">SUCCESS! SYSTEM READY</div>
    <div class="app-desc">
        ระบบจัดกลุ่มลูกค้าด้วย K-Means ในสไตล์ Dark Neon Tactical UI พร้อมปุ่มสลับสี Theme
    </div>
</div>
<div class="neon-line"></div>
""", unsafe_allow_html=True)


# =====================================================
# LOAD MODEL
# =====================================================
@st.cache_resource
def load_models():
    try:
        kmeans_model = joblib.load("model/kmeans_redbull.pkl")
        scaler_model = joblib.load("model/scaler_redbull.pkl")
        return kmeans_model, scaler_model, None

    except FileNotFoundError:
        return None, None, "ไม่พบไฟล์ kmeans_redbull.pkl หรือ scaler_redbull.pkl ในโฟลเดอร์ model"

    except Exception as e:
        return None, None, str(e)


kmeans_loaded, scaler_loaded, load_error = load_models()

if load_error:
    st.error(f"❌ โหลดโมเดลไม่สำเร็จ: {load_error}")
    st.stop()
else:
    st.sidebar.success("✅ โหลดโมเดล K-Means และ Scaler สำเร็จ")


# =====================================================
# FEATURES
# =====================================================
features = [
    "Units_Sold",
    "Marketing_Spend",
    "Logistics_Delay",
    "Customer_Score",
    "Revenue"
]


# =====================================================
# CENTROIDS
# =====================================================
centroids_data = {
    "Units_Sold": [94217.67, 224432.27],
    "Marketing_Spend": [101039.83, 200408.08],
    "Customer_Score": [49.97, 50.60],
    "Logistics_Delay": [44.85, 44.13],
    "Revenue": [3523438.42, 8562793.71]
}

centroids = pd.DataFrame(centroids_data, index=[0, 1])
centroids.index.name = "Cluster"


# =====================================================
# INPUT SECTION
# =====================================================
st.markdown("""
<div class="section-card">
    <h3>INPUT IN ACTION</h3>
    <p>กรุณาป้อนข้อมูลลูกค้าเพื่อให้ระบบวิเคราะห์กลุ่มลูกค้า</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='input-card'>", unsafe_allow_html=True)

    units_sold = st.number_input(
        "Units Sold",
        min_value=0,
        value=150000,
        step=1000
    )

    marketing_spend = st.number_input(
        "Marketing Spend",
        min_value=0,
        value=100000,
        step=1000
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='input-card'>", unsafe_allow_html=True)

    logistics_delay = st.number_input(
        "Logistics Delay (days)",
        min_value=0,
        value=30,
        step=1
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
        step=0.50,
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


# =====================================================
# DATA PREVIEW
# =====================================================
new_data_input = pd.DataFrame(
    [[units_sold, marketing_spend, logistics_delay, customer_score, revenue]],
    columns=features
)

st.markdown("### DATA PREVIEW")
st.dataframe(
    new_data_input,
    use_container_width=True,
    hide_index=True
)


# =====================================================
# PREDICTION
# =====================================================
st.markdown("<div class='neon-line'></div>", unsafe_allow_html=True)

if st.button("BUTTON  |  จัดกลุ่มข้อมูล", use_container_width=True):

    if new_data_input.isnull().values.any():
        st.warning("กรุณาตรวจสอบการป้อนข้อมูลให้ครบถ้วน")

    else:
        try:
            scaled_data = scaler_loaded.transform(new_data_input)
            predicted_cluster = int(kmeans_loaded.predict(scaled_data)[0])

        except Exception as e:
            st.error(f"❌ เกิดข้อผิดพลาดในการทำนาย: {e}")
            st.stop()

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
            result_text = "Cluster 1 - กลุ่มลูกค้ายอดขายสูง / High-Value Customer"
            result_detail = (
                "กลุ่มนี้มี Units Sold, Marketing Spend และ Revenue อยู่ในระดับสูง "
                "ควรรักษาลูกค้ากลุ่มนี้ด้วยบริการพิเศษ และลดความล่าช้าในการจัดส่ง"
            )

        st.markdown(f"""
        <div class="result-box">
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


# =====================================================
# HOW TO USE
# =====================================================
st.markdown("""
<div class="section-card">
    <h3>วิธีใช้งาน</h3>
    <p>1. ป้อน Units Sold, Marketing Spend, Logistics Delay, Customer Score และ Unit Price</p>
    <p>2. ระบบจะคำนวณ Revenue ให้อัตโนมัติ</p>
    <p>3. กดปุ่ม BUTTON | จัดกลุ่มข้อมูล</p>
    <p>4. ดูผลลัพธ์ Cluster และรายละเอียดค่าเฉลี่ยของกลุ่ม</p>
    <p>5. กด SWITCH COLOR THEME ที่ Sidebar เพื่อเปลี่ยนสีหน้าจอ</p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# FOOTER
# =====================================================
st.markdown("""
<div class="neon-line"></div>
<div style="text-align:center; color: var(--muted);">
    Boot Camp: Data Science and Machine Learning | Market Segmentation Tactical UI
</div>
""", unsafe_allow_html=True)


# =====================================================
# BACK HOME
# =====================================================
if st.button("🏠 กลับหน้าหลัก", use_container_width=True):
    st.switch_page("app.py")
