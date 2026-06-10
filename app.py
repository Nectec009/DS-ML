import streamlit as st

st.set_page_config(
    page_title="MyApp | Star Wars Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ================= CSS STYLE =================
st.markdown("""
<style>
/* พื้นหลังอวกาศ */
.stApp {
    background:
        radial-gradient(circle at 20% 20%, rgba(255,255,255,0.25) 1px, transparent 2px),
        radial-gradient(circle at 80% 30%, rgba(255,255,255,0.18) 1px, transparent 2px),
        radial-gradient(circle at 50% 80%, rgba(255,255,255,0.22) 1px, transparent 2px),
        linear-gradient(135deg, #020024 0%, #090979 35%, #000000 100%);
    background-size: 180px 180px, 260px 260px, 320px 320px, cover;
    color: white;
}

/* กล่องหัวข้อหลัก */
.main-title {
    text-align: center;
    padding: 35px 20px;
    margin-bottom: 25px;
    border-radius: 25px;
    background: linear-gradient(135deg, rgba(255,215,0,0.18), rgba(0,191,255,0.12));
    border: 1px solid rgba(255,215,0,0.45);
    box-shadow: 0 0 30px rgba(255,215,0,0.35);
}

.main-title h1 {
    font-size: 56px;
    color: #FFD700;
    text-shadow: 0 0 18px #FFD700;
    margin-bottom: 10px;
}

.main-title h3 {
    color: #87CEFA;
    text-shadow: 0 0 12px #00BFFF;
}

/* การ์ดเมนู */
.menu-card {
    padding: 22px;
    min-height: 155px;
    border-radius: 20px;
    margin-bottom: 18px;
    background: rgba(5, 10, 35, 0.82);
    border: 1px solid rgba(135, 206, 250, 0.45);
    box-shadow: 0 0 20px rgba(0,191,255,0.25);
    transition: 0.3s;
}

.menu-card:hover {
    transform: scale(1.03);
    border: 1px solid #FFD700;
    box-shadow: 0 0 28px rgba(255,215,0,0.45);
}

.menu-title {
    font-size: 21px;
    font-weight: 700;
    color: #FFD700;
    margin-bottom: 8px;
}

.menu-desc {
    font-size: 14px;
    color: #D6EAF8;
}

/* ปุ่ม Streamlit */
.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid #FFD700;
    background: linear-gradient(90deg, #111827, #1E3A8A);
    color: #FFD700;
    font-weight: bold;
    padding: 13px 18px;
    box-shadow: 0 0 12px rgba(255,215,0,0.25);
    transition: 0.25s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #FFD700, #F59E0B);
    color: #000000;
    border: 1px solid white;
    box-shadow: 0 0 25px rgba(255,215,0,0.85);
}

/* เส้นแบ่ง */
.hr-line {
    height: 2px;
    background: linear-gradient(90deg, transparent, #FFD700, transparent);
    margin: 20px 0 35px 0;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<div class="main-title">
    <h1>🚀 DATA SCIENCE GALAXY</h1>
    <h3>Boot Camp: Data Science and Machine Learning</h3>
    <p style="font-size:18px; color:#E5E7EB;">
        7 Day Intensive Hands-on Workshop | NECTEC
    </p>
    <p style="font-size:16px; color:#FFD700;">
        Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python
    </p>
</div>
<div class="hr-line"></div>
""", unsafe_allow_html=True)

st.markdown("## 🌌 เลือกระบบที่ต้องการเข้าสู่ภารกิจ")

# ================= MENU DATA =================
menus = [
    {
        "title": "ระบบคำนวณส่วนลด",
        "desc": "คำนวณส่วนลดตามยอดซื้อแบบอัตโนมัติ",
        "icon": "💰",
        "page": "pages/app1_discount_calc.py"
    },
    {
        "title": "Clean Data อาจารย์",
        "desc": "ตัวอย่างการทำความสะอาดข้อมูลจากอาจารย์",
        "icon": "🧹",
        "page": "pages/clean_customers.py"
    },
    {
        "title": "Clean Data ของผม",
        "desc": "โปรแกรมทำความสะอาดข้อมูลเวอร์ชันของผู้เรียน",
        "icon": "🛠️",
        "page": "pages/clean_appNectec.py"
    },
    {
        "title": "Clean Data ของผม 1",
        "desc": "เวอร์ชันเพิ่มเติมสำหรับทดลองปรับปรุงข้อมูล",
        "icon": "⚙️",
        "page": "pages/clean_appNectec1.py"
    },
    {
        "title": "Transform Data",
        "desc": "แปลงรูปแบบข้อมูลเพื่อเตรียมใช้งาน",
        "icon": "🔄",
        "page": "pages/transform_app.py"
    },
    {
        "title": "EDA APP",
        "desc": "วิเคราะห์ข้อมูลเบื้องต้นด้วยกราฟและสถิติ",
        "icon": "📊",
        "page": "pages/EDA_app.py"
    },
    {
        "title": "Sale Predict",
        "desc": "ระบบทำนายยอดขายด้วย Machine Learning",
        "icon": "📈",
        "page": "pages/sale_predict.py"
    },
    {
        "title": "Truck Predict",
        "desc": "ระบบทำนายข้อมูลรถบรรทุกหรือการขนส่ง",
        "icon": "🚚",
        "page": "pages/truck_predict.py"
    },
    {
        "title": "clustering segment",
        "desc": "clustering segment",
        "icon": "🚚",
        "page": "pages/clustering_segment.py"
    }
]

# ================= MENU LAYOUT =================
cols_per_row = 4

for i in range(0, len(menus), cols_per_row):
    cols = st.columns(cols_per_row)

    for col, menu in zip(cols, menus[i:i + cols_per_row]):
        with col:
            st.markdown(f"""
            <div class="menu-card">
                <div class="menu-title">{menu["icon"]} {menu["title"]}</div>
                <div class="menu-desc">{menu["desc"]}</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                f"เข้าสู่ภารกิจ: {menu['title']}",
                key=f"btn_{i}_{menu['title']}",
                use_container_width=True
            ):
                st.switch_page(menu["page"])

# ================= FOOTER =================
st.markdown("""
<br>
<div style="text-align:center; color:#9CA3AF;">
    ✨ May the Data be with you ✨
</div>
""", unsafe_allow_html=True)
