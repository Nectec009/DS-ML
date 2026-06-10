import streamlit as st
import pandas as pd
import ast
import re

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    layout="wide",
    page_title="TCP Group: ระบบแนะนำสินค้า",
    page_icon="🛒"
)

# =====================================================
# CSS STYLE: PINK PURPLE SMART DASHBOARD
# =====================================================
st.markdown("""
<style>
/* ================= GLOBAL ================= */
.stApp {
    background:
        radial-gradient(circle at 18% 18%, rgba(255,255,255,0.22), transparent 20%),
        radial-gradient(circle at 70% 10%, rgba(255,255,255,0.12), transparent 22%),
        linear-gradient(150deg, #ec3c86 0%, #a12ad0 45%, #4115c8 100%);
    color: white;
}

.block-container {
    max-width: 1200px;
    padding-top: 1rem;
    padding-bottom: 2rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

h1, h2, h3, p, label, span, div {
    color: white;
}

/* ================= TOP BAR ================= */
.top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 18px;
}

.logo-dot {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    background: rgba(73, 22, 89, 0.75);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 12px 28px rgba(0,0,0,0.22);
    font-size: 18px;
}

.top-title {
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 1px;
    opacity: 0.95;
}

/* ================= HERO LAYOUT ================= */
.smart-layout {
    display: grid;
    grid-template-columns: 280px 1fr 320px;
    gap: 36px;
    align-items: center;
}

/* ================= PHONE MOCKUP ================= */
.phone {
    width: 240px;
    height: 500px;
    border-radius: 36px;
    margin: auto;
    background:
        linear-gradient(180deg, rgba(255,255,255,0.55), rgba(255,255,255,0.18)),
        linear-gradient(160deg, rgba(250,177,255,0.55), rgba(110,59,220,0.35));
    box-shadow:
        0 28px 55px rgba(30, 7, 90, 0.38),
        inset 0 0 22px rgba(255,255,255,0.35);
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.18);
}

.phone-notch {
    position: absolute;
    width: 95px;
    height: 22px;
    background: rgba(255,255,255,0.88);
    left: 72px;
    top: 0;
    border-radius: 0 0 16px 16px;
}

.phone-status {
    position: absolute;
    top: 20px;
    left: 25px;
    right: 24px;
    display: flex;
    justify-content: space-between;
    font-size: 8px;
    opacity: 0.8;
}

.phone-content {
    padding: 74px 24px 20px 24px;
}

.mockup-title {
    text-align: center;
    font-size: 27px;
    font-weight: 900;
    letter-spacing: 6px;
    line-height: 1.1;
    margin-bottom: 2px;
}

.mockup-subtitle {
    text-align: center;
    font-size: 15px;
    letter-spacing: 5px;
    opacity: 0.85;
    margin-bottom: 20px;
}

.phone-label {
    font-size: 10px;
    opacity: 0.75;
    margin-left: 8px;
    margin-bottom: 4px;
}

.phone-input {
    background: linear-gradient(90deg, #ff5f9c, #ff2d78);
    height: 26px;
    border-radius: 20px;
    margin-bottom: 12px;
    font-size: 10px;
    display: flex;
    align-items: center;
    padding-left: 14px;
    box-shadow: 0 8px 18px rgba(235,40,120,0.25);
}

.phone-login {
    height: 28px;
    border-radius: 20px;
    border: 2px solid rgba(255,255,255,0.85);
    text-align: center;
    line-height: 24px;
    font-size: 12px;
    font-weight: 800;
    margin: 18px 28px;
}

.phone-card {
    background: rgba(255,255,255,0.88);
    color: #e23f86;
    border-radius: 24px;
    padding: 18px;
    margin-top: 38px;
    box-shadow: 0 18px 30px rgba(34,11,95,0.22);
}

.phone-card h4 {
    color: #e23f86 !important;
    margin: 0 0 8px 0;
    font-size: 14px;
}

.phone-card p {
    color: #6f6385 !important;
    font-size: 8px;
    line-height: 1.35;
}

.subscribe {
    background: #ff4c91;
    border-radius: 18px;
    height: 24px;
    margin-top: 14px;
    color: white;
    font-size: 9px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* ================= CENTER ROOM CARD ================= */
.room-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(160px, 1fr));
    gap: 20px;
}

.room-card {
    min-height: 132px;
    border-radius: 14px;
    border: 3px solid rgba(255,255,255,0.85);
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(8px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow:
        inset 0 0 22px rgba(255,255,255,0.08),
        0 18px 35px rgba(31,10,115,0.20);
}

.room-icon {
    font-size: 42px;
    margin-bottom: 12px;
}

.room-title {
    font-size: 17px;
    font-weight: 800;
}

.room-sub {
    font-size: 11px;
    opacity: 0.75;
    margin-top: 5px;
}

/* ================= RIGHT PANEL ================= */
.right-panel {
    min-height: 500px;
}

.room-select-title {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    font-size: 15px;
    font-weight: 800;
    margin-bottom: 20px;
}

.feature-buttons {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-bottom: 44px;
}

.feature-btn {
    border: 1.8px solid rgba(255,255,255,0.82);
    border-radius: 14px;
    height: 78px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: rgba(255,255,255,0.05);
}

.feature-btn .f-icon {
    font-size: 27px;
    margin-bottom: 6px;
}

.feature-btn .f-text {
    font-size: 10px;
    font-weight: 800;
}

.gauge-wrap {
    display: flex;
    justify-content: center;
}

.gauge {
    width: 210px;
    height: 210px;
    border-radius: 50%;
    background:
        radial-gradient(circle, rgba(255,255,255,0.08) 0 47%, transparent 48%),
        conic-gradient(from 225deg, rgba(255,255,255,0.95) 0deg, rgba(255,255,255,0.95) var(--degree), rgba(255,255,255,0.18) var(--degree), rgba(255,255,255,0.18) 270deg, transparent 270deg);
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}

.gauge-inner {
    width: 132px;
    height: 132px;
    border-radius: 50%;
    border: 1.5px solid rgba(255,255,255,0.75);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 38px;
    font-weight: 800;
}

.power-icon {
    text-align: center;
    margin-top: 18px;
    font-size: 36px;
    opacity: 0.9;
}

.click-text {
    text-align: center;
    font-size: 15px;
    font-weight: 800;
    margin-top: 5px;
}

.set-btn {
    margin: 20px auto 0 auto;
    width: 250px;
    height: 42px;
    border-radius: 30px;
    border: 2px solid rgba(255,255,255,0.9);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
}

/* ================= STREAMLIT INPUT STYLE ================= */
.stSelectbox > div > div {
    background: rgba(255,255,255,0.16);
    border-radius: 16px;
    border: 1.5px solid rgba(255,255,255,0.55);
    color: white;
}

.stButton > button {
    width: 100%;
    height: 42px;
    border-radius: 28px;
    border: 2px solid rgba(255,255,255,0.86);
    background: rgba(255,255,255,0.08);
    color: white;
    font-weight: 800;
    transition: 0.2s;
}

.stButton > button:hover {
    background: rgba(255,255,255,0.22);
    color: white;
    transform: scale(1.01);
}

[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
}

/* ================= RESULT CARDS ================= */
.result-section {
    margin-top: 34px;
    padding: 22px;
    border-radius: 26px;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.22);
    backdrop-filter: blur(8px);
}

.reco-card {
    border-radius: 18px;
    border: 2px solid rgba(255,255,255,0.55);
    background: rgba(255,255,255,0.10);
    padding: 18px;
    margin-bottom: 14px;
    box-shadow: 0 14px 30px rgba(31,10,115,0.18);
}

.reco-title {
    font-size: 18px;
    font-weight: 900;
    margin-bottom: 7px;
}

.reco-detail {
    font-size: 14px;
    opacity: 0.9;
}

.badge-row {
    display: flex;
    gap: 10px;
    margin-top: 12px;
}

.badge {
    padding: 6px 12px;
    border-radius: 18px;
    background: rgba(255,255,255,0.20);
    border: 1px solid rgba(255,255,255,0.35);
    font-size: 12px;
    font-weight: 800;
}

/* ================= RESPONSIVE ================= */
@media (max-width: 950px) {
    .smart-layout {
        grid-template-columns: 1fr;
    }

    .phone {
        width: 230px;
    }

    .right-panel {
        min-height: auto;
    }
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# HELPER FUNCTIONS
# =====================================================
def parse_itemset(value):
    """
    แปลงค่า antecedents / consequents จาก CSV ให้เป็น frozenset
    รองรับรูปแบบ:
    - frozenset({'A', 'B'})
    - ['A', 'B']
    - {'A', 'B'}
    - A
    """
    if isinstance(value, frozenset):
        return value

    if isinstance(value, set):
        return frozenset(value)

    if isinstance(value, list):
        return frozenset(value)

    if pd.isna(value):
        return frozenset()

    text = str(value).strip()

    try:
        if text.startswith("frozenset"):
            inner = re.sub(r"^frozenset\\((.*)\\)$", r"\\1", text)
            parsed = ast.literal_eval(inner)
            return frozenset(parsed)

        if text.startswith("[") or text.startswith("{") or text.startswith("("):
            parsed = ast.literal_eval(text)
            return frozenset(parsed)

        return frozenset([text])

    except Exception:
        return frozenset([text])


def itemset_to_text(itemset):
    if not itemset:
        return "-"
    return ", ".join([str(item) for item in itemset])


# =====================================================
# LOAD DATA
# =====================================================
@st.cache_data
def load_rules():
    try:
        df = pd.read_csv("model/Model_Association_Rules_Item.csv")

        required_cols = ["antecedents", "consequents", "support", "confidence", "lift"]
        missing_cols = [col for col in required_cols if col not in df.columns]

        if missing_cols:
            st.error(f"❌ ไฟล์ CSV ขาดคอลัมน์: {', '.join(missing_cols)}")
            return pd.DataFrame()

        df["antecedents"] = df["antecedents"].apply(parse_itemset)
        df["consequents"] = df["consequents"].apply(parse_itemset)

        df["antecedents_text"] = df["antecedents"].apply(itemset_to_text)
        df["consequents_text"] = df["consequents"].apply(itemset_to_text)

        return df

    except FileNotFoundError:
        st.error("❌ ไม่พบไฟล์ `model/Model_Association_Rules_Item.csv` กรุณาตรวจสอบ path ไฟล์")
        return pd.DataFrame()

    except Exception as e:
        st.error(f"❌ อ่านไฟล์ไม่สำเร็จ: {e}")
        return pd.DataFrame()


df_rules = load_rules()


# =====================================================
# HEADER DASHBOARD
# =====================================================
st.markdown("""
<div class="top-bar">
    <div class="logo-dot">👑</div>
    <div class="top-title">TCP GROUP SMART RECOMMENDATION</div>
</div>
""", unsafe_allow_html=True)


if df_rules.empty:
    st.stop()


# =====================================================
# PREPARE DATA
# =====================================================
all_antecedent_items = sorted(
    list(set(item for sublist in df_rules["antecedents"] for item in sublist))
)

if not all_antecedent_items:
    st.error("❌ ไม่พบรายการสินค้าในคอลัมน์ antecedents")
    st.stop()


# =====================================================
# SELECT PRODUCT
# =====================================================
selected_antecedent = st.selectbox(
    "เลือกสินค้าเพื่อดูสินค้าแนะนำ",
    all_antecedent_items,
    help="เลือกสินค้าหลักเพื่อดูว่าสินค้าใดมักถูกซื้อคู่กัน"
)

recommendation_rules = df_rules[
    df_rules["antecedents"].apply(lambda x: selected_antecedent in x)
].copy()

if not recommendation_rules.empty:
    recommendation_rules = recommendation_rules.sort_values(
        by=["lift", "confidence"],
        ascending=False
    )

    top_confidence = float(recommendation_rules.iloc[0]["confidence"])
    top_lift = float(recommendation_rules.iloc[0]["lift"])
    gauge_value = max(0, min(100, round(top_confidence * 100)))
else:
    top_confidence = 0
    top_lift = 0
    gauge_value = 0

degree = int(gauge_value / 100 * 270)


# =====================================================
# MAIN VISUAL AREA
# =====================================================
card_items = [
    ("🛒", "Product", selected_antecedent, "สินค้าที่เลือก"),
    ("🎁", "Bundle", "Top 5", "สินค้าแนะนำ"),
    ("📊", "Confidence", f"{top_confidence:.2f}", "โอกาสซื้อคู่กัน"),
    ("🚀", "Lift", f"{top_lift:.2f}", "ความสัมพันธ์"),
    ("💡", "Promotion", "Ready", "เหมาะจัดโปร"),
    ("🔎", "Rules", f"{len(recommendation_rules)}", "จำนวนกฎที่พบ")
]

center_cards_html = ""
for icon, title, value, sub in card_items:
    center_cards_html += f"""
    <div class="room-card">
        <div class="room-icon">{icon}</div>
        <div class="room-title">{title}</div>
        <div class="room-sub">{value}</div>
        <div class="room-sub">{sub}</div>
    </div>
    """

st.markdown(f"""
<div class="smart-layout">

    <div class="phone">
        <div class="phone-notch"></div>
        <div class="phone-status">
            <div>9:30</div>
            <div>●● ▬</div>
        </div>

        <div class="phone-content">
            <div class="mockup-title">TCP</div>
            <div class="mockup-subtitle">smart basket</div>

            <div class="phone-label">Product name</div>
            <div class="phone-input">{selected_antecedent}</div>

            <div class="phone-label">Recommendation</div>
            <div class="phone-input">Market Basket AI</div>

            <div class="phone-login">ANALYZE</div>

            <div class="phone-card">
                <h4>Smart Basket Mockup</h4>
                <p>
                    ระบบช่วยแนะนำสินค้าที่ลูกค้ามักซื้อคู่กันจาก Association Rules
                    เพื่อใช้วางแผนโปรโมชัน จัดชั้นสินค้า และเพิ่มยอดขาย
                </p>
                <div class="subscribe">Recommendation ready</div>
            </div>
        </div>
    </div>

    <div class="room-grid">
        {center_cards_html}
    </div>

    <div class="right-panel">
        <div class="room-select-title">
            <span>{selected_antecedent}</span>
            <span>⌄</span>
        </div>

        <div class="feature-buttons">
            <div class="feature-btn">
                <div class="f-icon">🛒</div>
                <div class="f-text">Product</div>
            </div>
            <div class="feature-btn">
                <div class="f-icon">📈</div>
                <div class="f-text">Lift</div>
            </div>
            <div class="feature-btn">
                <div class="f-icon">🎯</div>
                <div class="f-text">Confidence</div>
            </div>
        </div>

        <div class="gauge-wrap">
            <div class="gauge" style="--degree:{degree}deg;">
                <div class="gauge-inner">{gauge_value}%</div>
            </div>
        </div>

        <div class="power-icon">⏻</div>
        <div class="click-text">Click to recommend</div>
        <div class="set-btn">Market Basket Analysis</div>
    </div>

</div>
""", unsafe_allow_html=True)


# =====================================================
# RESULT SECTION
# =====================================================
st.markdown("""
<div class="result-section">
    <h2>✨ แนะนำสินค้าที่น่าจะซื้อคู่กัน</h2>
    <p>ระบบจะแสดงสินค้าที่มักถูกซื้อร่วมกับสินค้าที่เลือก พร้อมค่า Confidence และ Lift</p>
</div>
""", unsafe_allow_html=True)

if not recommendation_rules.empty:
    st.subheader(f"✅ คำแนะนำสำหรับ: {selected_antecedent}")

    for _, row in recommendation_rules.head(5).iterrows():
        antecedents_str = itemset_to_text(row["antecedents"])
        consequents_str = itemset_to_text(row["consequents"])

        st.markdown(f"""
        <div class="reco-card">
            <div class="reco-title">🛍️ ลูกค้าที่ซื้อ {antecedents_str}</div>
            <div class="reco-detail">
                มักจะซื้อ <b>{consequents_str}</b> ร่วมด้วย
            </div>
            <div class="badge-row">
                <div class="badge">Support: {row["support"]:.3f}</div>
                <div class="badge">Confidence: {row["confidence"]:.3f}</div>
                <div class="badge">Lift: {row["lift"]:.3f}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📊 รายละเอียดคำแนะนำทั้งหมด")

    display_reco = recommendation_rules[
        ["antecedents_text", "consequents_text", "support", "confidence", "lift"]
    ].head(10).rename(columns={
        "antecedents_text": "สินค้าหลัก",
        "consequents_text": "สินค้าแนะนำ",
        "support": "Support",
        "confidence": "Confidence",
        "lift": "Lift"
    })

    st.dataframe(
        display_reco.style.format({
            "Support": "{:.3f}",
            "Confidence": "{:.3f}",
            "Lift": "{:.3f}"
        }),
        use_container_width=True
    )

else:
    st.info(f"💡 ไม่พบกฎความสัมพันธ์ที่แข็งแกร่งสำหรับ {selected_antecedent}")


# =====================================================
# ALL RULES
# =====================================================
st.markdown("---")
st.subheader("🔍 สำรวจกฎความสัมพันธ์ทั้งหมด")

display_all = df_rules[
    ["antecedents_text", "consequents_text", "support", "confidence", "lift"]
].rename(columns={
    "antecedents_text": "สินค้าหลัก",
    "consequents_text": "สินค้าแนะนำ",
    "support": "Support",
    "confidence": "Confidence",
    "lift": "Lift"
})

st.dataframe(
    display_all.style.format({
        "Support": "{:.3f}",
        "Confidence": "{:.3f}",
        "Lift": "{:.3f}"
    }),
    use_container_width=True
)


# =====================================================
# FOOTER / BACK HOME
# =====================================================
st.markdown("---")

col_back, col_info = st.columns([1, 3])

with col_back:
    if st.button("🏠 กลับหน้าหลัก", use_container_width=True):
        st.switch_page("app.py")

with col_info:
    st.markdown(
        "ℹ️ ไฟล์ข้อมูลที่ใช้: `model/Model_Association_Rules_Item.csv`"
    )
