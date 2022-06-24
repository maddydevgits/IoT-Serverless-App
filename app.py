from enum import auto
import streamlit as st
import requests
import json
import time
import streamlit.components.v1 as components
from streamlit_autorefresh import st_autorefresh


api1='https://api.thingspeak.com/channels/1778887/fields/1.json?results=1'
api2='https://api.thingspeak.com/channels/1778887/fields/2.json?results=1'

api1result=requests.get(api1)
api1result=json.loads(api1result.text)
api1result=(api1result['feeds'][0])
api1result=int(api1result['field1'])
print(api1result)
   
st.title('IoT Serverless APP')

col1,col2=st.columns(2)
if api1result==1:
    col1.image('images/green.jpg')
    a=col1.button('Bulb1 Off')
else:
    col1.image('images/red.jpg')
    a=col1.button('Bulb1 On')


if a==True and api1result==1:
    while True:
        res=requests.get('https://api.thingspeak.com/update?api_key=94RKOKI1H4EFY6CL&field1=0')
        if int(res.text)!=0:
            break
        time.sleep(1)
    st.experimental_rerun()

elif a==True and api1result==0:
    while True:
        res=requests.get('https://api.thingspeak.com/update?api_key=94RKOKI1H4EFY6CL&field1=1')
        if int(res.text)!=0:
            break
        time.sleep(1)
    st.experimental_rerun()
