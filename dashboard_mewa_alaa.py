
import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from PIL import Image

# ---------- إعدادات واجهة ----------
st.set_page_config(page_title="داشبورد أدوات الصيد", layout="wide")
st.markdown("""
    <style>
        .main {background-color: #f2f9fa;}
        .block-container {padding: 2rem;}
        .title-style {
            background-color: #006176; color: white; padding: 1rem; border-radius: 8px; text-align: center;
        }
        .section {
            background-color: white; padding: 1.5rem; border-radius: 10px; margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# ---------- الشعار ----------
col1, col2 = st.columns([1, 8])
with col1:
    st.image("https://www.mewa.gov.sa/ar/Ministry/AboutMinistry/PublishingImages/MinistryLogo.png", width=100)
with col2:
    st.markdown("<div class='title-style'><h2>وزارة البيئة والمياه والزراعة</h2><h4>لوحة تحليل أدوات الصيد الساحلية</h4></div>", unsafe_allow_html=True)

# ---------- الشريط الجانبي ----------
with st.sidebar:
    st.markdown("### ℹ️ معلومات")
    st.markdown("**اسم المصممة:** آلاء الدوسري")
    st.markdown("**المجال:** تحليل البيانات")
    st.markdown("**المشروع:** أدوات الصيد حسب المراكز")
    st.markdown("---")
    st.markdown("© وزارة البيئة والمياه والزراعة")

# ---------- نبذة ----------
st.markdown("<div class='section'><h4>نبذة عن المشروع:</h4><p>يهدف هذا المشروع إلى تحليل بيانات أدوات الصيد المستخدمة في عدد من المراكز الساحلية، وذلك باستخدام تقنيات تحليل البيانات وتصورها. تشمل النتائج عرض إجمالي الأدوات، تحديد المركز الأعلى والأدنى في الاستخدام، ورؤية تفاعلية جغرافية للبيانات.</p></div>", unsafe_allow_html=True)

# ---------- البيانات ----------
data = {
    "المركز": ["السفانية", "منيفة", "دارين", "القطيف"],
    "الإجمالي": [95172, 913, 3120178, 2934571],
    "lat": [28.11, 27.4, 26.55, 26.56],
    "lon": [48.65, 48.6, 50.10, 50.01]
}
df = pd.DataFrame(data)

# ---------- رسم بياني ----------
fig = px.bar(df.sort_values("الإجمالي", ascending=False),
             x="المركز", y="الإجمالي",
             color="المركز",
             color_discrete_sequence=px.colors.sequential.Teal,
             title="إجمالي أدوات الصيد لكل مركز")
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig, use_container_width=True)

# ---------- جدول ----------
st.markdown("<div class='section'><h4>الجدول الإحصائي:</h4></div>", unsafe_allow_html=True)
st.dataframe(df[["المركز", "الإجمالي"]].sort_values("الإجمالي", ascending=False), use_container_width=True)

# ---------- خريطة ----------
st.markdown("<div class='section'><h4>الخريطة الجغرافية:</h4></div>", unsafe_allow_html=True)
m = folium.Map(location=[26.9, 49.7], zoom_start=7)
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=10,
        popup=f"{row['المركز']} - {row['الإجمالي']}",
        color="blue",
        fill=True,
        fill_opacity=0.7
    ).add_to(m)
st_folium(m, width=700)

# ---------- التوصيات ----------
st.markdown("<div class='section'><h4>التوصيات:</h4><ul><li>تركيز الجهود في المراكز ذات النشاط العالي كدارين والقطيف.</li><li>إعادة تقييم فعالية أدوات الصيد في المناطق ذات الأرقام المنخفضة.</li><li>مزيد من جمع البيانات التفصيلية سنويًا لرفع كفاءة التحليل.</li></ul></div>", unsafe_allow_html=True)

# ---------- التوقيع ----------
st.markdown("<br><div style='text-align:center;color:#006176;font-weight:bold;'>تصميم وتحليل البيانات: آلاء الدوسري 💙</div>", unsafe_allow_html=True)
