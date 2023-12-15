import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# กำหนดรูปแบบ CSS
st.markdown(
    """
    <style>
        .stButton > button {
            background-color: #4caf50; /* สีพื้นหลังของปุ่ม */
            color: #fff; /* สีข้อความของปุ่ม */
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        .stButton > button:hover {
            background-color: #45a049; /* สีพื้นหลังของปุ่มเมื่อชี้เข้าไป */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ตัวอย่างโค้ด Streamlit ที่ใช้งาน CSS
st.title('การทดสอบเขียนเว็บด้วย Python')
st.header('Wichai Thongprao')
st.subheader('สาขาเทคโนโลยีสารสนเทศ')
st.markdown("----")

col1, col2 = st.columns(2)
with col1:
    st.image('./img/ART.jpg', width=150)
with col2:
    st.image('./img/iris.jpg', width=150)

html_1 = """
<div class="st-ba">
    <center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)

dt = pd.read_csv('./data/iris.csv')
st.write(dt.head(10))

dt1 = dt['petal.length'].sum()
dt2 = dt['petal.width'].sum()
dt3 = dt['sepal.length'].sum()
dt4 = dt['sepal.width'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])

button_show_chart = st.button("show bar chart")
if button_show_chart:
    st.bar_chart(dx2)
    st.write("Not show bar chart")

html_2 = """
<div class="st-ba">
    <center><h5>การทำนายคลาสดอกไม้</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)

ptlen = st.slider("กรุณาเลือกข้อมูล petal.length", 0, 10)
ptwd = st.slider("กรุณาเลือกข้อมูล petal.width", 0, 10)

splen = st.number_input("กรุณาเลือกข้อมูล sepal.length")
spwd = st.number_input("กรุณาเลือกข้อมูล sepal.width")

button_predict = st.button("ทำนายผล")
if button_predict:
    X = dt.drop('variety', axis=1)
    y = dt.variety
    Knn_model = KNeighborsClassifier(n_neighbors=3)
    Knn_model.fit(X, y)

    x_input = np.array([[ptlen, ptwd, splen, spwd]])
    prediction = Knn_model.predict(x_input)

    if prediction[0] == "Setosa":
        st.image("./img/im.jpg", width=150)
        st.header("Setosa")
    elif prediction[0] == "Versicolor":
        st.image("./img/imm.jpg", width=150)
        st.header("Versicolor")
    else:
        st.image("./img/i.jpg", width=150)
        st.header("Verginiga")

    st.write("ไม่ทำนายผล")
else:
    st.write("ไม่ทำนายผล")
