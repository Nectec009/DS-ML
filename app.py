%%writefile home_app.py
import streamlit as st

st.set_page_config(page_title="TCP Beverage Analytics", layout="wide", page_icon="🥤")

# --- Professional Business Styling ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;700&display=swap');
    html, body, [class*=\"css\"]  {
        font-family: 'Sarabun', sans-serif;
    }
    .hero-section {
        background: linear-gradient(135deg, #0052D4, #4364F7, #6FB1FC);
        padding: 60px 20px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .nav-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        transition: 0.3s;
        border: 1px solid #eee;
        height: 100%;
    }
    .nav-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border-color: #007AFF;
    }
    .icon-circle {
        width: 80px;
        height: 80px;
        background: #f0f7ff;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 20px;
        font-size: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
    <div class='hero-section'>
        <h1 style='color: white; font-size: 3.5rem; margin-bottom: 10px;'>🥤 Beverage Insights Portal</h1>
        <p style='font-size: 1.2rem; opacity: 0.9;'>ระบบวิเคราะห์ข้อมูลและจัดการคลังเครื่องดื่มอัจฉริยะ สำหรับ Boot Camp DS&ML</p>
    </div>
""", unsafe_allow_html=True)

# --- Quick Access Menu ---
st.subheader("🚀 บริการและเครื่องมือวิเคราะห์")

col1, col2, col3, col4 = st.columns(4)

menu_items = [
    {"icon": "💰", "label": "ระบบคำนวณส่วนลด", "page": "pages/app1_discount_calc.py", "desc": "วิเคราะห์โปรโมชั่นตามยอดซื้อ", "col": col1},
    {"icon": "🧪", "label": "ศูนย์จัดการข้อมูล", "page": "pages/clean_customers.py", "desc": "มาตรฐานการคลีนโดยวิทยากร", "col": col2},
    {"icon": "✨", "label": "Nectec Workspace", "page": "pages/clean_appNectec.py", "desc": "ระบบคลีนข้อมูลเวอร์ชันปรับปรุง", "col": col3},
    {"icon": "📊", "label": "Ranking Dashboard", "page": "pages/clean_appNectec1.py", "desc": "จัดอันดับยอดขายรายพื้นที่", "col": col4}
]

for item in menu_items:
    with item["col"]:
        st.markdown(f"""
            <div class='nav-card'>
                <div class='icon-circle'>{item['icon']}</div>
                <h3>{item['label']}</h3>
                <p style='color: #666; font-size: 0.9rem; min-height: 40px;'>{item['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"เข้าใช้งาน {item['label']}", key=item['page'], use_container_width=True):
            st.switch_page(item['page'])

st.divider()

# --- Info Section ---
info_col1, info_col2 = st.columns([1, 2])
with info_col1:
    st.image("https://www.tcp.com/wp-content/uploads/2021/01/logo-tcp-red.png", width=150)
with info_col2:
    st.markdown("""
    ### 🐂 เกี่ยวกับหลักสูตร
    **Nectec 7-Day Intensive Workshop** ออกแบบมาเพื่อยกระดับทักษะด้านข้อมูล
    โดยเน้นการปฏิบัติงานจริงกับชุดข้อมูลธุรกิจเครื่องดื่มระดับโลก
    """)

st.caption("© 2024 TCP Group & Nectec Bootcamp | มจพ. ปราจีนบุรี")
