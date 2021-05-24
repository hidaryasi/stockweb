import streamlit as st
from Stock_Prediction import stock_predict
from Stock_Prediction import stock_close
from Stock_Prediction import stock_volume
from datetime import datetime
import plotly.graph_objects as go
import streamlit.components.v1 as components
import yfinance as yf
from datetime import datetime
import pandas as pd

st.image('logo1.png')

st.title("Stock Search")
selected_stock = st.text_input("Enter a valid stock ticker....(like: GOOG,AAPL)","BIDU")
button_clicked = st.button("GO")
if button_clicked == "GO":
    main()


#main function
def main():


    stock_data = yf.Ticker(selected_stock)
    st.write( """**Shortname**:  """ + stock_data.info['shortName'])
    st.write( """**Sector**:  """ + stock_data.info['sector'])
    st.write( """**Industry**:  """ + stock_data.info['industry'])
    st.write( """**Market Cap**:  """ + str(stock_data.info['marketCap']))
    st.write( """**Currency**:  """ + stock_data.info['currency'])
    st.write( """**Exchange time zone name**:  """ + stock_data.info['exchangeTimezoneName'])



    st.header("""Daily **Chart** for """ + selected_stock)
    stock_df = stock_data.history(period='1d', start='2020-01-01', end=None)
    fig = go.Figure(data=[go.Candlestick(x=stock_df.index,
                open=stock_df['Open'],
                high=stock_df['High'],
                low=stock_df['Low'],
                close=stock_df['Close'],
                increasing_line_color = 'green' ,
                decreasing_line_color = 'red')])
    fig.update_layout(xaxis_title="Date",
    yaxis_title="Price ($)",
    font=dict(
    family="Courier New, monospace",
    size=12,
    color="black"))
    st.plotly_chart(fig)

    st.header("""Daily **price** for """ + selected_stock)

    today = datetime.today().strftime('%Y-%m-%d')

    stock_lastprice = stock_data.history(period='1y', start='2021-1-1', end=today)
    last_price = stock_lastprice

    if last_price.empty == True:
        st.write("No data available at the moment")
    else:
        st.write(last_price)

    st.sidebar.header("Stock Additional Information")
    st.sidebar.markdown("please choose your option")
    financials = st.sidebar.checkbox("Quarterly Financials")
    if financials:
        st.subheader("""**Quarterly financials** for """ + selected_stock)
        display_financials = (stock_data.quarterly_financials)
        if display_financials.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_financials)

    major_shareholders = st.sidebar.checkbox("Institutional Shareholders")

    if major_shareholders:
        st.subheader("""**Institutional investors** for """ + selected_stock)
        display_shareholders = (stock_data.institutional_holders)
        if display_shareholders.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_shareholders)

    balance_sheet = st.sidebar.checkbox("Quarterly Balance Sheet")
    if balance_sheet:
        st.subheader("""**Quarterly balance sheet** for """ + selected_stock)
        display_balancesheet = (stock_data.quarterly_balance_sheet)
        if display_balancesheet.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_balancesheet)

    cashflow = st.sidebar.checkbox("Quarterly Cashflow")
    if cashflow:
        st.subheader("""**Quarterly cashflow** for """ + selected_stock)
        display_cashflow = (stock_data.quarterly_cashflow)
        if display_cashflow.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_cashflow)

    analyst_recommendation = st.sidebar.checkbox("Analysts Recommendation")
    if analyst_recommendation:
        st.subheader("""**Analysts recommendation** for """ + selected_stock)
        display_analyst_rec = (stock_data.recommendations)
        if display_analyst_rec.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_analyst_rec)

if __name__ == "__main__":
    main()
header = st.sidebar.header("Machine Learning Prediction")
subheader = st.sidebar.subheader("User Input Features")
ticker_predict = st.sidebar.selectbox('What stock do you want to see in LSTM Neural Network predictions for?'
,('AAL','AAPL','ACST','AESE','	AGNC','AIKI','AMAT','AMD','APA','APHA','ASRT','ATOS','AZN','BIDU','BIOL','BNGO','CAN','CDEV','CFMS'
,'CIDM','CLOV','CLVS','CMCSA','CRBP','CSCO','CTRM','CTXR','DBX','DKNG','EBON','FB','FCEL','FPRX','FUTU','GEVO','GILD','GNUS','GOOG','HBAN'
,'HSTO','IDEX','INO','INPX','INTC','IQ','ITRM','JAGX','JD','LI','LKCO','LYFT','MARA','MDLZ','MICT','MIK','MRVL','MSFT','MU','MVIS'
,'NAKD','NKLA','NNDM','NVDA','OCGN','OGI','ONTX','OPEN','OPK','OVID','PDD','PLUG','PTON','PYPL','QCOM','QTT','RETO','RIOT','SABR',
'SDC','SHIP','SIRI','SLGG','SNDL','SNGX','SOLO','SRNE','TELL','TLRY','TNXP','TRCH','TSLA','TTOO','TXMD','UAL','VIAC','VISL','VRM',
'VTRS','WKHS','ZNGA'))
time_steps = st.sidebar.slider('Please,select a range of time step values for the LSTM model.(Try optimizing the model!)',1, 5, (2))
stock_predict(ticker_predict,time_steps)

st.sidebar.image('logo2.png')
st.sidebar.markdown(""" This Website was develop by :
----------------------------------
Nur Hidayati Sihono-2017521460041 .created for Capstone Project Sichuan University,Bachelor Degree""")
st.sidebar.markdown(""" This Project Under supervised:
---------------------------------------
Prof.Li Xuwei-College of Computer Science,Sichuan University""")

st.sidebar.text_input('What do you want to see in the future? feel free to contact us')
st.sidebar.write("""
CONTACT US
----------------------------------------
Email : hidaryas2@gmail.com
----------------------------------------
""" )
