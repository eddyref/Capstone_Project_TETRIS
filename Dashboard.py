import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numerize import numerize
from adjustText import adjust_text
import geopandas as gpd

st.set_page_config(page_title="Capstone Project Dashboard", layout="wide")

st.title('Pengaruh Pemberian Kredit Sebagai Pemicu Pertumbuhan Produk Regional Domestik Bruto')