import streamlit as st
import pandas as pd
import ast
import re
from html import escape

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    layout="wide",
    page_title="TCP Recommendation",
    page_icon="🛒"
)

# =====================================================
# CSS STYLE
# =====================================================
st.markdown("""
<style>
/* ================= GLOBAL ================= */
.stApp {
    background: #e9eef8;
    color: #14345f;
}

.block-container {
    max-width: 1220px;
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

h1, h2, h3, h4, h5, h6 {
    color: #14345f !important;
    font-weight: 900 !important;
}

p, label, span, div {
    color: #14345f;
}

/* ================= TOP BAR ================= */
.top-panel {
    border-radius: 28px;
    background: #e9eef8;
    padding: 24px 28px;
    margin-bottom: 26px;
    box-shadow:
        10px 10px 22px #c7ccd5,
        -10px -10px 22px #ffffff;
}

.top-row {
    display: flex;
    align-items: center;
    gap: 18px;
}

.logo-circle {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: #6f7889;
    color: #ffc107;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow:
        7px 7px 14px #c7ccd5,
        -7px -7px 14px #ffffff;
    font-size: 20px;
}

.app-title {
    font-size: 30px;
    font-weight: 900;
    color: #14345f;
}

.app-subtitle {
    margin-top: 8px;
    color: #6e7584;
    font-size: 15px;
}

/* ================= MOCKUP LAYOUT ================= */
.neo-layout {
    display: grid;
    grid-template-columns: 250px 270px 1fr;
    gap: 34px;
    align-items: start;
    margin-top: 8px;
    margin-bottom: 34px;
}

/* ================= LEFT MOCKUP ================= */
.vertical-bars {
    display: flex;
    gap: 24px;
    align-items: end;
    justify-content: center;
    margin: 35px 0 18px 0;
}

.v-track {
    width: 42px;
    height: 205px;
    border-radius: 25px;
    background: #e9eef8;
    box-shadow:
        inset 8px 8px 14px #cbd0da,
        inset -8px -8px 14px #ffffff;
    display: flex;
    align-items: end;
    justify-content: center;
    padding-bottom: 15px;
}

.v-fill {
    width: 42px;
    border-radius: 25px;
    background: #123b6d;
    box-shadow:
        6px 6px 14px #c2c8d2,
        -6px -6px 14px #ffffff;
}

.dot-row {
    display: flex;
    gap: 28px;
    justify-content: center;
    margin-bottom: 35px;
}

.dot {
    width: 43px;
    height: 43px;
    border-radius: 50%;
    background: #e9eef8;
    box-shadow:
        7px 7px 12px #c7ccd5,
        -7px -7px 12px #ffffff;
    display: flex;
    justify-content: center;
    align-items: center;
}

.dot-inner {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: #123b6d;
}

.product-card {
    background: #e9eef8;
    border-radius: 22px;
    padding: 22px;
    display: flex;
    gap: 18px;
    align-items: center;
    box-shadow:
        10px 10px 22px #c7ccd5,
        -10px -10px 22px #ffffff;
    margin-bottom: 34px;
}

.product-image {
    width: 82px;
    height: 82px;
    border-radius: 12px;
    background: linear-gradient(135deg, #004b86, #0e6ea7);
    display: flex;
    justify-content: center;
    align-items: center;
    color: #8ed6ff;
    font-size: 38px;
}

.product-name {
    font-size: 19px;
    color: #777d8b;
    font-weight: 700;
}

.product-price {
    font-size: 24px;
    color: #14345f;
    font-weight: 900;
}

.music-line {
    height: 6px;
    border-radius: 20px;
    background: #d7dde8;
    box-shadow:
        inset 3px 3px 6px #c4c9d2,
        inset -3px -3px 6px #ffffff;
    margin: 10px 0 22px 0;
    position: relative;
}

.music-line::before {
    content: "";
    width: 88px;
    height: 6px;
    background: #123b6d;
    border-radius: 20px;
    position: absolute;
    left: 0;
    top: 0;
}

.player-row {
    display: flex;
    justify-content: center;
    gap: 24px;
}

.player-btn {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: #e9eef8;
    box-shadow:
        7px 7px 13px #c7ccd5,
        -7px -7px 13px #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #123b6d;
    font-size: 20px;
}

.player-btn.active {
    background: #123b6d;
    color: white;
}

/* ================= MIDDLE MOCKUP ================= */
.rating-card {
    border-radius: 22px;
    background: #e9eef8;
    box-shadow:
        10px 10px 22px #c7ccd5,
        -10px -10px 22px #ffffff;
    padding: 20px;
    margin-bottom: 34px;
}

.rating-title {
    font-size: 20px;
    color: #7a808d;
    margin-bottom: 14px;
}

.rating-line {
    height: 1px;
    background: #d4d9e3;
    margin-bottom: 18px;
}

.stars {
    font-size: 22px;
    color: #123b6d;
    letter-spacing: 2px;
}

.rating-score {
    float: right;
    color: #737b89;
    font-size: 13px;
    margin-top: 6px;
}

.rating-list {
    margin-top: 18px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    row-gap: 12px;
    color: #7a808d;
    font-size: 14px;
}

.rating-footer {
    margin: 22px -20px -20px -20px;
    background: #123b6d;
    color: white;
    height: 58px;
    border-radius: 0 0 22px 22px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 19px;
}

.chat-card {
    border-radius: 18px;
    background: #e9eef8;
    box-shadow:
        8px 8px 18px #c7ccd5,
        -8px -8px 18px #ffffff;
    padding: 18px;
    margin-bottom: 28px;
    color: #777d8b;
    min-height: 82px;
}

.chat-bubble {
    background: #123b6d;
    color: white;
    padding: 13px 18px;
    border-radius: 14px 14px 0 14px;
    width: fit-content;
    margin-left: auto;
    box-shadow:
        5px 5px 12px #c7ccd5,
        -5px -5px 12px #ffffff;
}

.dots-bubble {
    width: 80px;
    height: 54px;
    border-radius: 15px 15px 15px 0;
    background: #e9eef8;
    box-shadow:
        8px 8px 18px #c7ccd5,
        -8px -8px 18px #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #777d8b;
    letter-spacing: 4px;
}

/* ================= RIGHT MOCKUP ================= */
.button-grid {
    display: grid;
    grid-template-columns: 150px repeat(5, 48px);
    gap: 22px 24px;
    align-items: center;
    margin-top: 34px;
    margin-bottom: 34px;
}

.neo-pill {
    height: 43px;
    border-radius: 22px;
    background: #e9eef8;
    box-shadow:
        7px 7px 14px #c7ccd5,
        -7px -7px 14px #ffffff;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #7a808d;
    font-weight: 700;
}

.neo-pill.active {
    background: #123b6d;
    color: white;
}

.icon-btn {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: #e9eef8;
    box-shadow:
        7px 7px 14px #c7ccd5,
        -7px -7px 14px #ffffff;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #123b6d;
    font-size: 19px;
}

.icon-btn.active {
    background: #123b6d;
    color: white;
}

.search-box {
    height: 46px;
    border-radius: 25px;
    background: #e9eef8;
    box-shadow:
        inset 5px 5px 10px #c7ccd5,
        inset -5px -5px 10px #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #838b9a;
    font-size: 18px;
    margin: 30px 120px 34px 0;
}

.toggle-row {
    display: flex;
    align-items: center;
    gap: 34px;
    margin-bottom: 34px;
}

.toggle {
    width: 75px;
    height: 33px;
    border-radius: 20px;
    background: #e9eef8;
    box-shadow:
        inset 5px 5px 10px #c7ccd5,
        inset -5px -5px 10px #ffffff;
    position: relative;
}

.toggle::before {
    content: "";
    width: 43px;
    height: 43px;
    border-radius: 50%;
    background: #e9eef8;
    position: absolute;
    top: -5px;
    left: 0;
    box-shadow:
        7px 7px 14px #c7ccd5,
        -7px -7px 14px #ffffff;
}

.toggle.active {
    background: #123b6d;
}

.toggle.active::before {
    left: 32px;
}

.share-btn {
    width: 130px;
    height: 43px;
    border-radius: 22px;
    background: #e9eef8;
    box-shadow:
        7px 7px 14px #c7ccd5,
        -7px -7px 14px #ffffff;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #7a808d;
    font-size: 18px;
}

.percent-bubble {
    width: 105px;
    height: 55px;
    border-radius: 20px;
    background: #e9eef8;
    box-shadow:
        7px 7px 14px #c7ccd5,
        -7px -7px 14px #ffffff;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #123b6d;
    font-size: 18px;
    margin: 24px auto 18px auto;
}

.progress-line {
    height: 15px;
    border-radius: 20px;
    background: #d7dde8;
    box-shadow:
        inset 5px 5px 10px #c7ccd5,
        inset -5px -5px 10px #ffffff;
    position: relative;
}

.progress-line::before {
    content: "";
    width: 50%;
    height: 15px;
    border-radius: 20px;
    background: #123b6d;
    position: absolute;
    left: 0;
    top: 0;
}

/* ================= FORM & RESULT ================= */
.form-shell {
    border-radius: 25px;
    background: #e9eef8;
    box-shadow:
        10px 10px 22px #c7ccd5,
        -10px -10px 22px #ffffff;
    padding: 24px;
    margin: 24px 0 28px 0;
}

.result-shell {
    border-radius: 25px;
    background: #e9eef8;
    box-shadow:
        10px 10px 22px #c7ccd5,
        -10px -10px 22px #ffffff;
    padding: 24px;
    margin-top: 26px;
}

.reco-card {
    border-radius: 20px;
    background: #e9eef8;
    box-shadow:
        8px 8px 16px #c7ccd5,
        -8px -8px 16px #ffffff;
    padding: 18px;
    margin-bottom: 16px;
}

.reco-title {
    color: #123b6d;
    font-weight: 900;
    font-size: 18px;
}

.reco-meta {
    color: #6e7584;
    margin-top: 8px;
}

/* ================= STREAMLIT COMPONENTS ================= */
.stMultiSelect div[data-baseweb="select"] > div {
    background: #e9eef8 !important;
    border-radius: 18px !important;
    border: none !important;
    box-shadow:
        inset 5px 5px 10px #c7ccd5,
        inset -5px -5px 10px #ffffff;
    color: #14345f !important;
}

[data-baseweb="tag"] {
    background-color: #123b6d !important;
    color: white !important;
    border-radius: 18px !important;
}

.stButton > button {
    width: 100%;
    height: 46px;
    border-radius: 25px;
    border: none;
    background: #123b6d;
    color: white;
    font-weight: 900;
    box-shadow:
        7px 7px 14px #c7ccd5,
        -7px -7px 14px #ffffff;
    transition: 0.2s;
}

.stButton > button:hover {
    background: #0c2f59;
    color: white;
    transform: scale(1.01);
}

[data-testid="stDataFrame"] {
    border-radius: 20px;
    overflow: hidden;
    box-shadow:
        8px 8px 16px #c7ccd5,
        -8px -8px 16px #ffffff;
}

.stAlert {
    border-radius: 20px;
}

/* ================= RESPONSIVE ================= */
@media (max-width: 1000px) {
    .neo-layout {
        grid-template-columns: 1fr;
    }

    .button-grid {
        grid-template-columns: repeat(3, 1fr);
    }

    .search-box {
        margin-right: 0;
    }
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# HELPER FUNCTIONS
# =====================================================
def parse_itemset(value):
    if isinstance(value, frozenset):
        return value

    if isinstance(value, (set, list, tuple)):
        return frozenset(value)

    if pd.isna(value):
        return frozenset()

    text = str(value).strip()

    if text == "" or text.lower() == "nan":
        return frozenset()

    try:
        if text.startswith("frozenset"):
            match = re.match(r"^frozenset\\((.*)\\)$", text)
            if match:
                inner = match.group(1).strip()

                if inner == "":
                    return frozenset()

                parsed = ast.literal_eval(inner)

                if isinstance(parsed, (set, list, tuple, frozenset)):
                    return frozenset(parsed)

                return frozenset([parsed])

        if text.startswith("[") or text.startswith("{") or text.startswith("("):
            parsed = ast.literal_eval(text)

            if isinstance(parsed, (set, list, tuple, frozenset)):
                return frozenset(parsed)

            return frozenset([parsed])

        return frozenset([text])

    except Exception:
        return frozenset([text])


def itemset_to_text(itemset):
    if itemset is None:
        return "-"

    if isinstance(itemset, str):
        return itemset

    try:
        items = sorted([str(item) for item in itemset])
        if len(items) == 0:
            return "-"
        return ", ".join(items)

    except Exception:
        return str(itemset)


def get_recommendations(user_selected_items, rules_df, top_n=5):
    potential_recommendations = []

    for _, rule in rules_df.iterrows():
        rule_antecedents = rule["antecedents"]
        rule_consequents = rule["consequents"]

        if rule_antecedents.issubset(user_selected_items):
            for rec_item in rule_consequents:
                if rec_item not in user_selected_items:
                    potential_recommendations.append({
                        "item": rec_item,
                        "confidence": float(rule["confidence"]),
                        "lift": float(rule["lift"]),
                        "support": float(rule["support"]) if "support" in rules_df.columns else 0.0
                    })

    sorted_recs = sorted(
        potential_recommendations,
        key=lambda x: (x["lift"], x["confidence"]),
        reverse=True
    )

    final_recs = []
    seen_items = set()

    for rec in sorted_recs:
        if rec["item"] not in seen_items:
            final_recs.append(rec)
            seen_items.add(rec["item"])

        if len(final_recs) >= top_n:
            break

    return final_recs


def make_rules_display(df):
    display_df = df.copy()

    display_df["Antecedents"] = display_df["antecedents"].apply(itemset_to_text)
    display_df["Consequents"] = display_df["consequents"].apply(itemset_to_text)

    show_cols = ["Antecedents", "Consequents"]

    if "support" in display_df.columns:
        show_cols.append("support")

    show_cols += ["confidence", "lift"]

    display_df = display_df[show_cols].rename(columns={
        "support": "Support",
        "confidence": "Confidence",
        "lift": "Lift"
    })

    return display_df


# =====================================================
# LOAD DATA
# =====================================================
@st.cache_data
def load_rules():
    try:
        rules = pd.read_csv("model/Model_association_Rules.csv")

        required_cols = ["antecedents", "consequents", "confidence", "lift"]
        missing_cols = [col for col in required_cols if col not in rules.columns]

        if missing_cols:
            st.error(f"❌ ไฟล์ CSV ขาดคอลัมน์: {', '.join(missing_cols)}")
            return pd.DataFrame()

        rules["antecedents"] = rules["antecedents"].apply(parse_itemset)
        rules["consequents"] = rules["consequents"].apply(parse_itemset)

        return rules

    except FileNotFoundError:
        st.error("❌ ไม่พบไฟล์ `model/Model_association_Rules.csv` กรุณาตรวจสอบ path ไฟล์")
        return pd.DataFrame()

    except Exception as e:
        st.error(f"❌ โหลดข้อมูลไม่สำเร็จ: {e}")
        return pd.DataFrame()


df_rules_app = load_rules()

if df_rules_app.empty:
    st.stop()


# =====================================================
# CATEGORY MASTER DATA
# =====================================================
all_regions_master = [
    "USA-WEST",
    "ASIA-PACIFIC",
    "TH-NORTH",
    "TH-CENTRAL",
    "EUROPE-EU",
    "USA-EAST",
    "TH-SOUTH"
]

all_products_master = [
    "Tropical Edition",
    "Original Blue",
    "Sugarfree",
    "Krating Daeng 250",
    "Red Edition"
]

all_channels_master = [
    "extreme sports",
    "f1 sponsorship",
    "TV Ad",
    "in-store promo",
    "Social Media"
]

all_items_in_rules = (
    {item for itemset in df_rules_app["antecedents"] for item in itemset}
    .union({item for itemset in df_rules_app["consequents"] for item in itemset})
)

all_regions = sorted([item for item in all_regions_master if item in all_items_in_rules])
all_products = sorted([item for item in all_products_master if item in all_items_in_rules])
all_channels = sorted([item for item in all_channels_master if item in all_items_in_rules])


def get_item_type(item):
    if item in all_regions_master:
        return "Region"

    if item in all_products_master:
        return "Product"

    if item in all_channels_master:
        return "Channel"

    return "Item"


# =====================================================
# TOP HEADER
# =====================================================
st.markdown("""
<div class="top-panel">
    <div class="top-row">
        <div class="logo-circle">👑</div>
        <div>
            <div class="app-title">TCP Behavioral Association Recommendation</div>
            <div class="app-subtitle">
                ระบบแนะนำสินค้า ช่องทาง และภูมิภาค จากกฎความสัมพันธ์ Association Rules
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# =====================================================
# MOCKUP UI AREA
# =====================================================
st.markdown("""
<div class="neo-layout">

    <div>
        <div class="vertical-bars">
            <div class="v-track"><div class="v-fill" style="height: 98px;"></div></div>
            <div class="v-track"><div class="v-fill" style="height: 154px;"></div></div>
            <div class="v-track"><div class="v-fill" style="height: 52px;"></div></div>
        </div>

        <div class="dot-row">
            <div class="dot"><div class="dot-inner"></div></div>
            <div class="dot"><div class="dot-inner"></div></div>
            <div class="dot"><div class="dot-inner"></div></div>
        </div>

        <div class="product-card">
            <div class="product-image">🛒</div>
            <div>
                <div class="product-name">TCP</div>
                <div class="product-price">AI</div>
            </div>
        </div>

        <div class="music-line"></div>

        <div class="player-row">
            <div class="player-btn">‹</div>
            <div class="player-btn active">▷</div>
            <div class="player-btn">›</div>
        </div>
    </div>

    <div>
        <div class="rating-card">
            <div class="rating-title">recommendation</div>
            <div class="rating-line"></div>

            <div>
                <span class="stars">★ ★ ★</span>
                <span style="color:#c8ced8;">★ ★</span>
                <span class="rating-score">3/5</span>
            </div>

            <div class="rating-list">
                <div>region</div><div>good</div>
                <div>product</div><div>excellent</div>
                <div>channel</div><div>not bad</div>
            </div>

            <div class="rating-footer">TCP recommendation</div>
        </div>

        <div class="chat-card">
            <b>Hi!</b><br>
            what I can help you?
        </div>

        <div class="chat-bubble">Hi! there</div>

        <br>

        <div class="dots-bubble">••••</div>
    </div>

    <div>
        <div class="button-grid">
            <div class="neo-pill">button</div>
            <div class="icon-btn">≡</div>
            <div class="icon-btn">⌂</div>
            <div class="icon-btn">♧</div>
            <div class="icon-btn">♡</div>
            <div class="icon-btn">▱</div>

            <div class="neo-pill">button</div>
            <div class="icon-btn">≡</div>
            <div class="icon-btn">⌂</div>
            <div class="icon-btn">♧</div>
            <div class="icon-btn">♡</div>
            <div class="icon-btn">▱</div>

            <div class="neo-pill active">button</div>
            <div class="icon-btn active">≡</div>
            <div class="icon-btn active">⌂</div>
            <div class="icon-btn active">♧</div>
            <div class="icon-btn active">♡</div>
            <div class="icon-btn active">▱</div>

            <div class="neo-pill">button</div>
            <div class="icon-btn">≡</div>
            <div class="icon-btn">⌂</div>
            <div class="icon-btn">♧</div>
            <div class="icon-btn">♡</div>
            <div class="icon-btn">▱</div>
        </div>

        <div class="search-box">search for 🔍</div>

        <div class="toggle-row">
            <div class="toggle"></div>
            <div class="toggle active"></div>
            <div class="dot"><div class="dot-inner"></div></div>
            <div class="dot"></div>
            <div class="share-btn">⌘ share</div>
        </div>

        <div class="percent-bubble">50%</div>
        <div class="progress-line"></div>
    </div>

</div>
""", unsafe_allow_html=True)


# =====================================================
# INPUT FORM
# =====================================================
st.markdown("""
<div class="form-shell">
    <h2>🛒 เลือกรายการที่สนใจ</h2>
    <p>
        เลือก Region, Product Variant หรือ Channel แล้วให้ระบบแนะนำรายการที่เกี่ยวข้อง
        จากกฎความสัมพันธ์
    </p>
</div>
""", unsafe_allow_html=True)

col_region, col_product, col_channel = st.columns(3)

with col_region:
    selected_regions = st.multiselect(
        "เลือกภูมิภาค (Region)",
        options=all_regions,
        default=[]
    )

with col_product:
    selected_products = st.multiselect(
        "เลือกประเภทสินค้า (Product Variant)",
        options=all_products,
        default=[]
    )

with col_channel:
    selected_channels = st.multiselect(
        "เลือกช่องทาง (Channel)",
        options=all_channels,
        default=[]
    )

user_input_items = frozenset(selected_regions + selected_products + selected_channels)


# =====================================================
# RECOMMENDATION RESULT
# =====================================================
if st.button("💡 แนะนำ!", use_container_width=True):
    if not user_input_items:
        st.warning("กรุณาเลือกอย่างน้อยหนึ่งรายการเพื่อรับคำแนะนำ")

    else:
        recommendations = get_recommendations(
            user_selected_items=user_input_items,
            rules_df=df_rules_app,
            top_n=5
        )

        selected_display = ", ".join([escape(str(item)) for item in user_input_items])

        st.markdown("""
        <div class="result-shell">
            <h2>ผลการแนะนำ</h2>
            <p>รายการที่ระบบพบว่ามีความสัมพันธ์สูงกับสิ่งที่คุณเลือก</p>
        </div>
        """, unsafe_allow_html=True)

        st.info(f"รายการที่เลือก: {selected_display}")

        if recommendations:
            for i, rec in enumerate(recommendations, start=1):
                item = rec["item"]
                item_type = get_item_type(item)
                item_text = escape(str(item))

                st.markdown(f"""
                <div class="reco-card">
                    <div class="reco-title">{i}. {item_type}: {item_text}</div>
                    <div class="reco-meta">
                        Confidence: {rec["confidence"]:.3f} |
                        Lift: {rec["lift"]:.3f} |
                        Support: {rec["support"]:.3f}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.info("ไม่พบกฎการแนะนำสำหรับรายการที่คุณเลือก โปรดลองเลือกรายการอื่น ๆ")


# =====================================================
# RULES TABLE
# =====================================================
with st.expander("🔍 ดูกฎความสัมพันธ์ทั้งหมด"):
    display_rules = make_rules_display(df_rules_app)

    format_dict = {
        "Confidence": "{:.3f}",
        "Lift": "{:.3f}"
    }

    if "Support" in display_rules.columns:
        format_dict["Support"] = "{:.3f}"

    st.dataframe(
        display_rules.style.format(format_dict),
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# BACK HOME
# =====================================================
st.markdown("---")

if st.button("🏠 กลับหน้าหลัก", use_container_width=True):
    st.switch_page("app.py")
