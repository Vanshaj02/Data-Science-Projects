import numpy as np
import pandas as pd
import pickle
import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))

st.title("Rainfall Predictor")
st.markdown("It predicts the annual rainfall probability in different places.")

locations = {
    'ANDAMAN & NICOBAR ISLANDS': 0,
    'ARUNACHAL PRADESH': 1,
    'ASSAM & MEGHALAYA': 2,
    'NAGA MANI MIZO TRIPURA': 21,
    'SUB HIMALAYAN WEST BENGAL & SIKKIM': 28,
    'GANGETIC WEST BENGAL': 10,
    'ORISSA': 23,
    'JHARKHAND': 15,
    'BIHAR': 3,
    'EAST UTTAR PRADESH': 9,
    'WEST UTTAR PRADESH': 35,
    'UTTARAKHAND': 31,
    'HARYANA DELHI & CHANDIGARH': 12,
    'PUNJAB': 24,
    'HIMACHAL PRADESH': 13,
    'JAMMU & KASHMIR': 14,
    'WEST RAJASTHAN': 34,
    'EAST RAJASTHAN': 8,
    'WEST MADHYA PRADESH': 33,
    'EAST MADHYA PRADESH': 7,
    'GUJARAT REGION': 11,
    'SAURASHTRA & KUTCH': 26,
    'KONKAN & GOA': 17,
    'MADHYA MAHARASHTRA': 19,
    'MATATHWADA': 20,
    'VIDARBHA': 32,
    'CHHATTISGARH': 4,
    'COASTAL ANDHRA PRADESH': 5,
    'TELANGANA': 30,
    'RAYALSEEMA': 25,
    'TAMIL NADU': 29,
    'COASTAL KARNATAKA': 6,
    'NORTH INTERIOR KARNATAKA': 22,
    'SOUTH INTERIOR KARNATAKA': 27,
    'KERALA': 16,
    'LAKSHADWEEP': 18
}

years = [year for year in range(1950, 2020)]

col3, col4 = st.columns(2)
col5, col6 = st.columns(2)


place = st.selectbox(label='Location', options=locations.keys())
place = locations[place]

with col3:
    range1 = st.slider(label='January-February', min_value=0.00, max_value=1.00)

with col4:
    range2 = st.slider(label='March-May', min_value=0.00, max_value=1.00)

with col5:
    range3 = st.slider(label='June-September', min_value=0.00, max_value=1.00)

with col6:
    range4 = st.slider(label='October-December', min_value=0.00, max_value=1.00)

data = pd.DataFrame(
    data=np.array([place, range1, range2, range3, range4]).reshape(1, 5),
    columns=['SUBDIVISION', 'Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec']
)

def predict():
    value = model.predict(data)[0]
    if value == 2:
        status = "High"

    elif value == 1:
        status = "Medium"

    else:
        status = "Low"
        
    st.subheader(f"Probability: {status}")

st.button(label='Output', on_click=predict)