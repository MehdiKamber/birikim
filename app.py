import streamlit as st
from pages.hakan_birikim import HakanBirikim

st.title('Konut Birikimi Hesaplama')

birikim_miktari = st.number_input('Aylik Birikim Miktari (₺)', value=3000)
ev_fiyati = st.number_input('Ev Fiyati (₺)', value=1250000)
kira_geliri = st.number_input('Kira Geliri (₺)', value=8000)
pesinat_orani = st.slider('Pesinat Orani (%)', min_value=0.1, max_value=1.0, value=0.2, step=0.05)
kredi_suresi = st.slider('Kredi Suresi (Yil)', min_value=1, max_value=30, value=15)

hakan = HakanBirikim(birikim_miktari, ev_fiyati, kira_geliri, pesinat_orani, kredi_suresi)
daire_sayisi, kira_geliri_toplam = hakan.ev_satinalma()

st.subheader(f"65 yasina kadar alinan toplam daire sayisi: {daire_sayisi}")
st.subheader(f"Toplam kira geliri: {kira_geliri_toplam} ₺")