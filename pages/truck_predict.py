import streamlit as st
import pandas as pd
import joblib
from datetime import datetime, timedelta
import plotly.express as px

# ================= PAGE CONFIG =================
st.set_page_config(
    layout="wide",
    page_title="Space Logistics Prediction",
    page_icon="🚛"
)

# ================= CSS STYLE =================
st.markdown("""
<style>
/* พื้นหลังอวกาศ */
.stApp {
    background:
        radial-gradient(circle at 15% 20%, rgba(255,255,255,0.28) 1px, transparent 2px),
        radial-gradient(circle at 75% 25%, rgba(0,191,255,0.30) 1px, transparent 2px),
        radial-gradient(circle at 45% 75%, rgba(255,215,0,0.25) 1px, transparent 2px),
        linear-gradient(135deg, #020617 0%, #081A3A 45%, #000000 100%);
    background-size: 170px 170px, 260px 260px, 340px 340px, cover;
    color: #F8FAFC;
}

/* ซ่อนแถบบางส่วนของ Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* กล่องหัวเรื่อง */
.hero-box {
    padding: 35px 30px;
    border-radius: 28px;
    background: linear-gradient(135deg, rgba(14,165,233,0.18), rgba(250,204,21,0.13));
    border: 1px solid rgba(250,204,21,0.45);
    box-shadow: 0 0 35px rgba(14,165,233,0.30), inset 0 0 25px rgba(250,204,21,0.08);
    text-align: center;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 48px;
    font-weight: 900;
    color: #FACC15;
    text-shadow: 0 0 18px rgba(250,204,21,0.95);
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 20px;
    color: #BAE6FD;
    text-shadow: 0 0 12px rgba(56,189,248,0.9);
}

.hero-desc {
    font-size: 16px;
    color: #E0F2FE;
    margin-top: 8px;
}

/* กล่อง Section */
.section-card {
    padding: 22px;
    border-radius: 22px;
    background: rgba(2, 6, 23, 0.78);
    border: 1px solid rgba(56,189,248,0.35);
    box-shadow: 0 0 22px rgba(56,189,248,0.18);
    margin-bottom: 20px;
}

/* หัวข้อ */
h1, h2, h3 {
    color: #FACC15 !important;
}

[data-testid="stMarkdownContainer"] p {
    color: #E5E7EB;
}

/* Metric Card */
.metric-card {
    padding: 18px;
    border-radius: 18px;
    background: linear-gradient(145deg, rgba(15,23,42,0.92), rgba(30,41,59,0.76));
    border: 1px solid rgba(125,211,252,0.40);
    box-shadow: 0 0 18px rgba(14,165,233,0.18);
    text-align: center;
}

.metric-title {
    color: #BAE6FD;
    font-size: 14px;
    margin-bottom: 6px;
}

.metric-value {
    color: #FACC15;
    font-size: 30px;
    font-weight: 900;
    text-shadow: 0 0 10px rgba(250,204,21,0.75);
}

/* ปุ่ม */
.stButton > button {
    width: 100%;
    border-radius: 16px;
    border: 1px solid #FACC15;
    background: linear-gradient(90deg, #0F172A, #1E3A8A);
    color: #FACC15;
    font-weight: 800;
    padding: 14px 20px;
    box-shadow: 0 0 14px rgba(250,204,21,0.28);
    transition: 0.25s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #FACC15, #F97316);
    color: #020617;
    border: 1px solid #FFFFFF;
    box-shadow: 0 0 28px rgba(250,204,21,0.85);
    transform: scale(1.01);
}

/* Upload box */
[data-testid="stFileUploader"] {
    background: rgba(15,23,42,0.75);
    border: 1px dashed rgba(56,189,248,0.55);
    border-radius: 18px;
    padding: 12px;
}

/* Dataframe / Editor */
[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid rgba(56,189,248,0.25);
}

/* เส้นแบ่ง */
.space-line {
    height: 2px;
    background: linear-gradient(90deg, transparent, #38BDF8, #FACC15, transparent);
    margin: 20px 0 30px 0;
}
</style>
""", unsafe_allow_html=True)


# ================= HERO HEADER =================
st.markdown("""
<div class="hero-box">
    <div class="hero-title">🚛 SPACE LOGISTICS COMMAND CENTER</div>
    <div class="hero-subtitle">Logistics Service Time Prediction & Scheduling</div>
    <div class="hero-desc">
        ระบบพยากรณ์เวลาบริการรถบรรทุก และจัดตารางคิวแบบอัจฉริยะในสไตล์ศูนย์บัญชาการอวกาศ
    </div>
</div>
<div class="space-line"></div>
""", unsafe_allow_html=True)


# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    try:
        model = joblib.load("model/service_time_model.pkl")
        return model
    except FileNotFoundError:
        st.error("❌ ไม่พบไฟล์โมเดล `model/service_time_model.pkl` กรุณาตรวจสอบ path ของไฟล์โมเดล")
        st.stop()
    except Exception as e:
        st.error(f"❌ โหลดโมเดลไม่สำเร็จ: {e}")
        st.stop()


loaded_model = load_model()

st.success("✅ ระบบพร้อมใช้งาน: โหลดโมเดล `service_time_model.pkl` สำเร็จแล้ว")


# ================= INPUT SECTION =================
st.markdown("""
<div class="section-card">
    <h3>📝 Mission Input: ข้อมูลรถบรรทุกที่ต้องการพยากรณ์</h3>
    <p>อัปโหลดไฟล์ CSV หรือใช้ข้อมูลเริ่มต้น จากนั้นเลือกแถวที่ต้องการนำไปพยากรณ์</p>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "📂 เลือกไฟล์ CSV ที่มีข้อมูลรถบรรทุก",
    type=["csv"]
)

df_for_editor = pd.DataFrame()

if uploaded_file is not None:
    try:
        df_uploaded = pd.read_csv(uploaded_file)

        bool_cols = [
            "Truck_Type_4-Wheel",
            "Truck_Type_6-Wheel",
            "Operation_Type_Pickup"
        ]

        for col in bool_cols:
            if col in df_uploaded.columns:
                df_uploaded[col] = df_uploaded[col].astype(bool)

        if "Company_Name" not in df_uploaded.columns:
            df_uploaded.insert(
                0,
                "Company_Name",
                [f"รถบรรทุก {i + 1}" for i in range(len(df_uploaded))]
            )

        if "Select" not in df_uploaded.columns:
            df_uploaded.insert(0, "Select", True)

        st.success("✅ อัปโหลดไฟล์สำเร็จ สามารถแก้ไขข้อมูลในตารางด้านล่างได้")
        df_for_editor = df_uploaded

    except Exception as e:
        st.error(f"❌ เกิดข้อผิดพลาดในการอ่านไฟล์ CSV: {e}")
        st.stop()

else:
    df_for_editor = pd.DataFrame({
        "Company_Name": [
            "บริษัทขนส่ง A", "บริษัทโลจิสติกส์ B", "บริษัทขนส่ง C", "บริษัทขนส่ง D",
            "บริษัทโลจิสติกส์ E", "บริษัทขนส่ง F", "บริษัทโลจิสติกส์ G", "บริษัทขนส่ง H",
            "บริษัทขนส่ง I", "บริษัทโลจิสติกส์ J"
        ],
        "Available_Docks": [3, 1, 2, 5, 4, 3, 2, 1, 5, 2],
        "Total_Cartons": [150, 200, 100, 250, 180, 120, 300, 90, 220, 170],
        "SKU_Count": [3, 2, 4, 3, 2, 3, 4, 1, 3, 2],
        "Truck_Type_4-Wheel": [False, False, True, False, False, True, False, True, False, False],
        "Truck_Type_6-Wheel": [True, False, False, True, False, False, False, False, True, False],
        "Operation_Type_Pickup": [True, False, False, True, False, True, False, False, True, False]
    })

    df_for_editor.insert(0, "Select", True)


# ================= DATA EDITOR =================
st.markdown("### 🛰️ ตารางข้อมูลรถบรรทุก")

loaded_unseen_data = st.data_editor(
    df_for_editor,
    key="unseen_data_editor",
    num_rows="dynamic",
    hide_index=True,
    use_container_width=True,
    column_config={
        "Select": st.column_config.CheckboxColumn(
            "เลือก",
            help="เลือกรายการที่ต้องการพยากรณ์",
            default=True
        ),
        "Company_Name": st.column_config.TextColumn("บริษัท / รถบรรทุก"),
        "Available_Docks": st.column_config.NumberColumn("จำนวน Dock ที่ว่าง", min_value=0),
        "Total_Cartons": st.column_config.NumberColumn("จำนวน Carton", min_value=0),
        "SKU_Count": st.column_config.NumberColumn("จำนวน SKU", min_value=0),
        "Truck_Type_4-Wheel": st.column_config.CheckboxColumn("รถ 4 ล้อ"),
        "Truck_Type_6-Wheel": st.column_config.CheckboxColumn("รถ 6 ล้อ"),
        "Operation_Type_Pickup": st.column_config.CheckboxColumn("Pickup")
    }
)

selected_for_prediction = loaded_unseen_data[
    loaded_unseen_data["Select"] == True
].drop(columns=["Select"])

if selected_for_prediction.empty:
    st.warning("⚠️ กรุณาเลือกข้อมูลรถบรรทุกอย่างน้อย 1 แถวเพื่อทำการพยากรณ์")
    st.stop()


# ================= DASHBOARD METRICS =================
total_trucks = len(loaded_unseen_data)
selected_trucks = len(selected_for_prediction)
total_cartons = int(selected_for_prediction["Total_Cartons"].sum())

col_m1, col_m2, col_m3 = st.columns(3)

with col_m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">รถทั้งหมดในระบบ</div>
        <div class="metric-value">{total_trucks}</div>
    </div>
    """, unsafe_allow_html=True)

with col_m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">รถที่เลือกพยากรณ์</div>
        <div class="metric-value">{selected_trucks}</div>
    </div>
    """, unsafe_allow_html=True)

with col_m3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Carton รวม</div>
        <div class="metric-value">{total_cartons}</div>
    </div>
    """, unsafe_allow_html=True)


# ================= START TIME =================
st.markdown("### ⏱️ Launch Time: กำหนดเวลาเริ่มต้นสำหรับจัดตาราง")

col1, col2 = st.columns(2)

if "start_date" not in st.session_state:
    st.session_state.start_date = datetime.now().date()

if "start_time" not in st.session_state:
    st.session_state.start_time = datetime.now().time()

with col1:
    date_input = st.date_input(
        "เลือกวันที่เริ่มต้นการประมวลผล",
        value=st.session_state.start_date,
        key="scheduling_date_input"
    )

with col2:
    time_input = st.time_input(
        "เลือกเวลาเริ่มต้นการประมวลผล",
        value=st.session_state.start_time,
        key="scheduling_time_input"
    )

st.session_state.start_date = date_input
st.session_state.start_time = time_input

start_processing_time = datetime.combine(
    st.session_state.start_date,
    st.session_state.start_time
)

st.info(
    f"🚀 เวลาเริ่มต้นการประมวลผล: "
    f"**{start_processing_time.strftime('%Y-%m-%d %H:%M:%S')}**"
)


# ================= PREDICTION =================
st.markdown("<div class='space-line'></div>", unsafe_allow_html=True)

if st.button("🚀 Launch Prediction: ทำการพยากรณ์และจัดตารางคิว"):
    st.markdown("## 🔮 Prediction Result: ผลการพยากรณ์")

    X_unseen_for_prediction = selected_for_prediction.drop(
        columns=["Company_Name"],
        errors="ignore"
    )

    expected_model_columns = [
        "Available_Docks",
        "Total_Cartons",
        "SKU_Count",
        "Truck_Type_4-Wheel",
        "Truck_Type_6-Wheel",
        "Operation_Type_Pickup"
    ]

    missing_cols = set(expected_model_columns) - set(X_unseen_for_prediction.columns)

    if missing_cols:
        st.error(
            "❌ ข้อมูลไม่มีคอลัมน์ที่จำเป็นสำหรับการทำนาย: "
            + ", ".join(missing_cols)
        )
        st.stop()

    X_unseen_for_prediction = X_unseen_for_prediction[expected_model_columns]

    try:
        predictions = loaded_model.predict(X_unseen_for_prediction)

    except ValueError as e:
        st.error(
            f"❌ เกิดข้อผิดพลาดในการทำนาย: {e} "
            "กรุณาตรวจสอบว่าคอลัมน์ตรงกับตอนฝึกโมเดล"
        )
        st.stop()

    prediction_results = selected_for_prediction.copy()
    prediction_results["Predicted_Service_Min"] = predictions

    prediction_results["Predicted_Service_Min"] = prediction_results[
        "Predicted_Service_Min"
    ].round(2)

    st.dataframe(
        prediction_results,
        use_container_width=True,
        hide_index=True
    )

    # ================= SCHEDULING =================
    st.markdown("## 🗓️ Space Dock Queue: ตารางเวลาการจัดคิวรถบรรทุก")

    scheduling_df = prediction_results.copy()
    scheduling_df = scheduling_df.sort_values(
        by="Predicted_Service_Min"
    ).reset_index(drop=True)

    current_available_time = start_processing_time
    suggested_arrival_times = []
    completion_times = []

    for _, row in scheduling_df.iterrows():
        suggested_arrival_times.append(current_available_time)

        service_duration = timedelta(
            minutes=float(row["Predicted_Service_Min"])
        )

        current_completion_time = current_available_time + service_duration
        completion_times.append(current_completion_time)

        current_available_time = current_completion_time

    scheduling_df["Suggested_Arrival_Time"] = suggested_arrival_times
    scheduling_df["Completion_Time"] = completion_times

    display_df = scheduling_df.copy()
    display_df["Suggested_Arrival_Time"] = display_df[
        "Suggested_Arrival_Time"
    ].dt.strftime("%Y-%m-%d %H:%M:%S")

    display_df["Completion_Time"] = display_df[
        "Completion_Time"
    ].dt.strftime("%Y-%m-%d %H:%M:%S")

    display_cols = [
        "Company_Name",
        "Available_Docks",
        "Total_Cartons",
        "SKU_Count",
        "Predicted_Service_Min",
        "Suggested_Arrival_Time",
        "Completion_Time"
    ]

    st.dataframe(
        display_df[display_cols],
        use_container_width=True,
        hide_index=True
    )

    # ================= RESULT METRICS =================
    total_service_min = float(scheduling_df["Predicted_Service_Min"].sum())
    avg_service_min = float(scheduling_df["Predicted_Service_Min"].mean())
    finish_time = scheduling_df["Completion_Time"].max()

    col_r1, col_r2, col_r3 = st.columns(3)

    with col_r1:
        st.metric("เวลาบริการรวม", f"{total_service_min:.2f} นาที")

    with col_r2:
        st.metric("เวลาเฉลี่ยต่อคัน", f"{avg_service_min:.2f} นาที")

    with col_r3:
        st.metric("คาดว่าจะเสร็จทั้งหมด", finish_time.strftime("%H:%M:%S"))

    # ================= GANTT CHART =================
    st.markdown("## 📊 Galaxy Gantt Chart: แผนภาพตารางคิวรถบรรทุก")

    scheduling_df["Task"] = (
        scheduling_df["Company_Name"]
        + " | "
        + scheduling_df["Predicted_Service_Min"].round(2).astype(str)
        + " นาที"
    )

    fig_gantt = px.timeline(
        scheduling_df,
        x_start="Suggested_Arrival_Time",
        x_end="Completion_Time",
        y="Task",
        color="Predicted_Service_Min",
        color_continuous_scale=px.colors.sequential.Turbo,
        title="🚛 Space Logistics Queue Scheduling",
        labels={
            "Suggested_Arrival_Time": "เวลาที่ควรมาถึง",
            "Completion_Time": "เวลาที่บริการเสร็จ",
            "Task": "รถบรรทุก / บริษัท",
            "Predicted_Service_Min": "เวลาบริการที่คาดการณ์ (นาที)"
        },
        hover_name="Company_Name"
    )

    fig_gantt.update_yaxes(autorange="reversed")

    fig_gantt.update_layout(
        template="plotly_dark",
        height=620,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(2,6,23,0.70)",
        font=dict(color="#E5E7EB"),
        title_font=dict(size=24, color="#FACC15"),
        xaxis_title="เวลา",
        yaxis_title="ลำดับรถ",
        coloraxis_colorbar=dict(
            title="นาที",
            title_font_color="#FACC15",
            tickfont_color="#E5E7EB"
        )
    )

    fig_gantt.update_traces(
        marker_line_color="rgba(255,255,255,0.85)",
        marker_line_width=1
    )

    st.plotly_chart(fig_gantt, use_container_width=True)


# ================= HOW TO USE =================
st.markdown("""
<div class="section-card">
    <h3>📌 วิธีใช้งาน</h3>
    <ol>
        <li>อัปโหลดไฟล์ CSV หรือใช้ข้อมูลเริ่มต้น</li>
        <li>ตรวจสอบ แก้ไข และเลือกข้อมูลรถบรรทุกที่ต้องการพยากรณ์</li>
        <li>เลือกวันที่และเวลาเริ่มต้น</li>
        <li>กดปุ่ม <b>Launch Prediction</b></li>
        <li>ดูผลลัพธ์ตารางคิวและ Gantt Chart</li>
    </ol>
</div>
""", unsafe_allow_html=True)


# ================= BACK HOME =================
if st.button("🏠 กลับหน้าหลัก"):
    st.switch_page("app.py")
