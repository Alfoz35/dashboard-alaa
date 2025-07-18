import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static

# خلفية لون هادي
def add_custom_background():
    st.markdown(
        '''
        <style>
        .stApp {
            background-color: #f0f4f8;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        }
        .report {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            color: #333333;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )

add_custom_background()

data = {
    "المركز": ["السفانية", "منيفة", "دارين", "القطيف", "الدمام", "الخبر", "الزور"],
    "الإجمالي": [95172, 913, 3120178, 2934571, 500000, 450000, 300000],
    "lat": [28.11, 27.40, 26.55, 26.56, 26.42, 26.28, 27.88],
    "lon": [48.65, 48.60, 50.10, 50.01, 50.10, 50.20, 48.63]
}
df = pd.DataFrame(data)

st.set_page_config(page_title="لوحة تحكم أدوات الصيد", layout="wide")

# عنوان واسم الوزارة مع اسمك
st.markdown("""
<div style='text-align: center; margin-bottom: 20px;'>
    <h1 style='color: #007ACC;'>وزارة البيئة والمياه والزراعة</h1>
    <h3>✍️ تصميم وتحليل البيانات: <strong>آلاء الدوسري</strong></h3>
</div>
""", unsafe_allow_html=True)

# تقرير ملون وجذاب
with st.container():
    st.markdown("<div class='report'>", unsafe_allow_html=True)
    st.subheader("📋 التقرير التحليلي للمشرف")
    st.markdown("""
    - **دارين** تسجل أعلى عدد من أدوات الصيد بإجمالي 3,120,178 أداة.
    - **منيفة** الأقل نشاطًا بعدد 913 أداة فقط.
    - متوسط أدوات الصيد لبقية المراكز يتراوح بين 300 ألف إلى 500 ألف.
    - توزع الأدوات يظهر في الخريطة الجغرافية مع دوائر ملونة تعبر عن الكثافة.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# تقسيم الصفحة إلى عمودين: جدول + رسم بياني
col1, col2 = st.columns([1,1])

with col1:
    st.subheader("📊 جدول بيانات أدوات الصيد")
    st.dataframe(df.style.format({"الإجمالي": "{:,.0f}"}), use_container_width=True)

with col2:
    st.subheader("📈 مخطط دائري - نسبة أدوات الصيد حسب المركز")
    fig = px.pie(df, names='المركز', values='الإجمالي',
                 title='نسبة أدوات الصيد حسب المركز',
                 color_discrete_sequence=px.colors.sequential.Teal)
    st.plotly_chart(fig, use_container_width=True)

# خريطة بحجم أصغر مع تحسين المظهر
st.subheader("🗺️ الخريطة الجغرافية للمراكز الساحلية")
map_container = st.container()
with map_container:
    m = folium.Map(location=[26.8, 49.8], zoom_start=8, width='100%', height='400px')
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["lat"], row["lon"]],
            radius=8,
            popup=f"{row['المركز']} - {row['الإجمالي']:,}",
            color='#007ACC',
            fill=True,
            fill_color='#00BFFF',
            fill_opacity=0.8
        ).add_to(m)
    folium_static(m, width=700, height=400)


