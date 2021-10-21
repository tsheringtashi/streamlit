import streamlit as st
from PIL import Image


img = Image.open("D:/DHI_GIC/pic/logo.png")
st.set_page_config(page_title= "DCIC APP",
                   page_icon=img)


a1, a2, a3,a4, a5, a6,a7, a8, a9,a10 = st.columns(10)
a10.button("LOG OUT")
a5.image(img)
a1.button("MENU")
st.info(":information_source:   You have an invitation waiting :bangbang:")
st.header(":chart_with_upwards_trend: REVENUE SUMMARY")
st.markdown("Key metrics of DOC in Million")
img1, img2, img3,img4, img5, img6,img7, img8, img9,img10 = st.columns(10)
kpi1, kpi2, kpi3,kpi4, kpi5, kpi6,kpi7, kpi8, kpi9,kpi10 = st.columns(10)

imga = Image.open("D:/DHI_GIC/pic/bob.png")
imgb = Image.open("D:/DHI_GIC/pic/bpc.png")
imgc = Image.open("D:/DHI_GIC/pic/bt.png")
imgd = Image.open("D:/DHI_GIC/pic/cdcl.png")
imge = Image.open("D:/DHI_GIC/pic/drukair.png")
imgf = Image.open("D:/DHI_GIC/pic/dgpc.png")
imgg = Image.open("D:/DHI_GIC/pic/kil.png")
imgh = Image.open("D:/DHI_GIC/pic/smcl.png")
imgi = Image.open("D:/DHI_GIC/pic/nrdcl.png")
imgj = Image.open("D:/DHI_GIC/pic/ttpl.png")

img1.image(imga)
img2.image(imgb)
img3.image(imgc)
img4.image(imgd)
img5.image(imge)
img6.image(imgf)
img7.image(imgg)
img8.image(imgh)
img9.image(imgi)
img10.image(imgj)

kpi1.metric(label = "BoB",
            value = 250,
            delta = 2.5)

kpi2.metric(label = "BPC",
            value = 140,
            delta = 9.2)
kpi3.metric(label = "BT",
            value = 250,
            delta = 11.5)
kpi4.metric(label = "CDCL",
            value = 250,
            delta = 0.5)

kpi5.metric(label = "DRUKAIR",
            value = 140,
            delta = 0.2)
kpi6.metric(label = "DGPC",
            value = 250,
            delta = 20.5)
kpi7.metric(label = "KIL",
            value = 250,
            delta = -0.5)

kpi8.metric(label = "SMCL",
            value = 140,
            delta = 0.2)
kpi9.metric(label = "NRDCL",
            value = 250,
            delta = 9.5)
kpi10.metric(label = "TTPL",
            value = 12,
            delta = 15.2)

# chart_data = pd.read_excel("D:/DHI_GIC/deposit_rawdata.xlsx")
# chart_data["Date"] = pd.to_datetime(chart_data["Date"])
#
# chart_df = chart_data.groupby(['Fixed Deposits', 'Recurring Deposits','Current Deposits','Saving Bank Deposits'], as

# st.bar_chart(chart_df)


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    with st.form('Form1'):
        submitted1 = st.form_submit_button('TARGET MANAGEMENT')

with col2:
    with st.form('Form2'):
        submitted2 = st.form_submit_button('PROJECT MANAGEMENT')

with col3:
    with st.form('Form3'):
        submitted1 = st.form_submit_button('TRAINING DEVELOPMENT ')

with col4:
    with st.form('Form4'):
        submitted2 = st.form_submit_button('REPORTS & DATA')

with col5:
    with st.form('Form5'):
        submitted2 = st.form_submit_button('EVENTS TRACKER')


