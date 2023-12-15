import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# 1. การจัดหน้าเว็บ
st.set_page_config(
    page_title="Web App ทดสอบด้วย Python",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

# 2. การเรียงลำดับและจัดหน้า Element
with st.sidebar:
    st.subheader("ตัวเลือก")
    ptlen = st.slider("ข้อมูล petal.length", 0, 10)
    ptwd = st.slider("ข้อมูล petal.width", 0, 10)
    splen = st.number_input("ข้อมูล sepal.length")
    spwd = st.number_input("ข้อมูล sepal.width")
    show_chart = st.checkbox("แสดงกราฟ")

# 3. การใช้ Widget ที่เหมาะสม
if show_chart:
    st.bar_chart(dx2)

# 4. การแยกฟังก์ชัน
def show_statistics_chart():
    # แสดงสถิติข้อมูลดอกไม้
    st.markdown(html_1, unsafe_allow_html=True)
    st.write(dt.head(10))
    if show_chart:
        st.bar_chart(dx2)

def make_prediction():
    # ทำนายผล
    X = dt.drop('variety', axis=1)
    y = dt.variety
    Knn_model = KNeighborsClassifier(n_neighbors=3)
    Knn_model.fit(X, y)
    x_input = np.array([[ptlen, ptwd, splen, spwd]])
    prediction = Knn_model.predict(x_input)
    st.write(prediction)

    # แสดงรูปภาพตามคลาสที่ทำนาย
    if prediction[0] == "Setosa":
        st.image("./img/im.jpg")
        st.header("Setosa")
    elif prediction[0] == "Versicolor":
        st.image("./img/imm.jpg")
        st.header("Versicolor")
    else:
        st.image("./img/immm.jpg")
        st.header("Verginiga")

# 5. การให้คำอธิบาย
st.title('การทดสอบเขียนเว็บด้วย Python')
st.header('Wichai Thongprao')
st.subheader('สาขาเทคโนโลยีสารสนเทศ')
st.markdown("----")

col1, col2 = st.columns(2)
with col1:
    st.image('./img/ART.jpg')
with col2:
    st.image('./img/iris.jpg')

show_statistics_chart()

html_2 = """
<div style="background-color:#FFBF00;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายคลาสดอกไม้</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

make_prediction()
