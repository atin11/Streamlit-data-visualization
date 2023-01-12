import streamlit as st
import pandas as pd

st.set_page_config(layout="wide",
                  page_title="Covid-19 Data")

raw_data = st.beta_container()
confirmed = st.beta_container()
recovered = st.beta_container()
deceased = st.beta_container()
guidelines = st.beta_container()
footer = st.beta_container()

with raw_data:
    st.markdown("<h1 style='text-align: center;'>COVID-19 Daily State Wise Data</h1>", unsafe_allow_html=True)
    st.text("We update this data on a daily basis with help of API provided by https://www.covid19india.org")

    data_r = pd.read_csv("state_wise_daily.csv")
    st.write(data_r)

    selected_state = st.selectbox("Choose the state whose data you want to see", options=['Delhi (DL)',
                                                                                          'Andaman and Nicobar Islands (AN)',
                                                                                          'Andhra Pradesh (AP)',
                                                                                          'Arunachal Pradesh (AR)',
                                                                                          'Assam (AS)',
                                                                                          'Bihar (BR)',
                                                                                          'Chandigarh (CH)',
                                                                                          'Chhattisgarh (CT)',
                                                                                          'Dadra and Nagar Haveli and Daman and Diu (DN)',
                                                                                          'Goa (GA)',
                                                                                          'Gujrat (GJ)',
                                                                                          'Haryana (HR)',
                                                                                          'Himachal Pradesh (HP)',
                                                                                          'Jammu and Kashmir (JK)',
                                                                                          'Jharkhand (JH)',
                                                                                          'Karnataka (KA)',
                                                                                          'Kerela (KL)',
                                                                                          'Ladakh (LA)',
                                                                                          'Lakshadweep (LD)',
                                                                                          'Madhya Pradesh (MP)',
                                                                                          'Maharashtra (MH)',
                                                                                          'Manipur (MN)',
                                                                                          'Meghalaya (ML)',
                                                                                          'Mizoram (MZ)',
                                                                                          'Nagaland (NL)',
                                                                                          'Odisha (OR)',
                                                                                          'Puducherry (PY)',
                                                                                          'Punjab (PB)',
                                                                                          'Rajasthan (RJ)',
                                                                                          'Sikkim (SK)',
                                                                                          'State Unassigned (UN)',
                                                                                          'Tamil Nadu (TN)',
                                                                                          'Telangana (TG)',
                                                                                          'Tripura (TR)',
                                                                                          'Uttar Pradesh (UP)',
                                                                                          'Uttarakhand (UK)',
                                                                                          'West Bengal (WB)'], index=0)
    state = selected_state[-3:-1]

with confirmed:
    st.title("Confirmed Patients")
    st.text("The daily trends of confirmed COVID-19 patients in the state")

    lis_col1, rand_col1 = st.beta_columns(2)
    data1 = pd.read_excel("confirmed.xlsx")
    lis_col1.write(data1[['Date',state]])

    astart1 = rand_col1.empty()
    start1 = astart1.slider("Last N days", 0, 471, (0,471),key="1")

    astart_date1 = rand_col1.empty()
    start_date1 = astart_date1.selectbox("Start Date",options=[("Using Slider Instead"),]+(list(data1["Date"])),index=0,key="1")

    aend_date1 = rand_col1.empty()
    if start_date1!="Using Slider Instead":
        end_date1 = aend_date1.selectbox("End Date",options= [("Using Slider Instead"),]+list(data1["Date"][(list(data1["Date"]).index(start_date1))+1:]),index=0,key="2")
    else:
        end_date1 = aend_date1.selectbox("End Date",options=["Using Slider Instead"],index=0,key="2")

    if start_date1!="Using Slider Instead" and end_date1!="Using Slider Instead":
        start1 = ((list(data1["Date"]).index(start_date1)),(list(data1["Date"]).index(end_date1)))
        start1 = astart1.slider("Last N days", 0, 471, start1,key="1")

    df1 = pd.DataFrame({'Date': data1["Date_YMD"][start1[0]:start1[1]],
                       'Confirmed cases': data1[state][start1[0]:start1[1]]})

    st.line_chart(df1)

with recovered:
    st.title("Recovered Patients")
    st.text("The daily trends of patients recovered from COVID-19 in the state")

    lis_col2, rand_col2 = st.beta_columns(2)
    data2 = pd.read_excel("recovered.xlsx")
    lis_col2.write(data2[['Date',state]])

    astart2 = rand_col2.empty()
    start2 = astart2.slider("Last N days", 0, 471, (0,471),key="2")

    astart_date2 = rand_col2.empty()
    start_date2 = astart_date2.selectbox("Start Date",options=[("Using Slider Instead"),]+(list(data2["Date"])),index=0,key="3")

    aend_date2 = rand_col2.empty()
    if start_date2!="Using Slider Instead":
        end_date2 = aend_date2.selectbox("End Date",options= [("Using Slider Instead"),]+list(data2["Date"][(list(data2["Date"]).index(start_date2))+1:]),index=0,key="4")
    else:
        end_date2 = aend_date2.selectbox("End Date",options=["Using Slider Instead"],index=0,key="4")

    if start_date2!="Using Slider Instead" and end_date2!="Using Slider Instead":
        start2 = ((list(data2["Date"]).index(start_date2)),(list(data2["Date"]).index(end_date2)))
        start2 = astart2.slider("Last N days", 0, 471, start2,key="2")

    df2 = pd.DataFrame({'Date': data2["Date_YMD"][start2[0]:start2[1]],
                       'Recovered cases': data2[state][start2[0]:start2[1]]})

    st.line_chart(df2)

with deceased:
    st.title("Deceased Patients")
    st.text("The daily trends of deceased patients of COVID-19 in the state")

    lis_col3, rand_col3 = st.beta_columns(2)
    data3 = pd.read_excel("deceased.xlsx")
    lis_col3.write(data3[['Date',state]])

    astart3 = rand_col3.empty()
    start3 = astart3.slider("Last N days", 0, 471, (0,471),key="3")

    astart_date3 = rand_col3.empty()
    start_date3 = astart_date3.selectbox("Start Date",options=[("Using Slider Instead"),]+(list(data3["Date"])),index=0,key="5")

    aend_date3 = rand_col3.empty()
    if start_date3!="Using Slider Instead":
        end_date3 = aend_date3.selectbox("End Date",options= [("Using Slider Instead"),]+list(data3["Date"][(list(data3["Date"]).index(start_date3))+1:]),index=0,key="6")
    else:
        end_date3 = aend_date3.selectbox("End Date",options=["Using Slider Instead"],index=0,key="6")

    if start_date3!="Using Slider Instead" and end_date3!="Using Slider Instead":
        start3 = ((list(data3["Date"]).index(start_date3)),(list(data3["Date"]).index(end_date3)))
        start3 = astart3.slider("Last N days", 0, 471, start3,key="3")

    df3 = pd.DataFrame({'Date': data3["Date_YMD"][start3[0]:start3[1]],
                       'Deceased cases': data3[state][start3[0]:start3[1]]})


    st.line_chart(df3)

with guidelines:
    st.subheader("COVID-19 Guidelines")
    myargs = ["Wear a mask", "Stay 6 feet away from others", "Get Vaccinated","Avoid crowds and poorly ventilated spaces","Wash your hands often", "Cover coughs and sneezes","Clean and disinfect"]
    for i in myargs:
        st.info(i)

with footer:
    st.markdown("<h5 style='text-align: center;padding-top:80px ;color: red;'>Designed By Aryan Dawer and Atin Narain</h5>", unsafe_allow_html=True)
