# data_collect.py 
import streamlit as st 
import pandas as pd 
import requests 
import json 
import pandas as pd 

#app.py에 있떤거 가져옴(잘라내기 이걸 가져와도 app.py에 from으로 이 파일 연결해서 가능 )
# @st.cache_data
# def load_data():
#      SEOUL_PUBLIC_API = st.secrets["api_credentials"]["SEOUL_PUBLIC_API"] #핵심코드.
#      st.write(SEOUL_PUBLIC_API)
#      URL = f'http://openapi.seoul.go.kr:8088/{SEOUL_PUBLIC_API}/json/tbLnOpendataRentV/1/5/'
#      st.write(URL)
#      content = requests.get(URL).json()
#      data = pd.DataFrame(content['tbLnOpendataRentV']['row'])
#      return data 
    
    