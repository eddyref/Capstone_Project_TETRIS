import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numerize import numerize
from adjustText import adjust_text
import geopandas as gpd

st.set_page_config(page_title="Capstone Project Dashboard", layout="wide")

st.title('Pengaruh Pemberian Kredit Sebagai Pemicu Pertumbuhan Produk Regional Domestik Bruto')

# Import dataframe
kp = pd.read_csv('https://raw.githubusercontent.com/Fery-K/Capstone_Project_TETRIS/master/Datasets/kredit_provinsi.csv')
k_mk = pd.read_csv('https://raw.githubusercontent.com/Fery-K/Capstone_Project_TETRIS/master/Datasets/kredit_modal_kerja_bank.csv')
k_i = pd.read_csv('https://raw.githubusercontent.com/Fery-K/Capstone_Project_TETRIS/master/Datasets/kredit_investasi_bank.csv')
k_k = pd.read_csv('https://raw.githubusercontent.com/Fery-K/Capstone_Project_TETRIS/master/Datasets/kredit_konsumsi_bank.csv')
pdrb = pd.read_csv('https://raw.githubusercontent.com/Fery-K/Capstone_Project_TETRIS/master/Datasets/pdrb.csv')

# Impute missing value
pdrb.loc[33, 'tahun_2011'], pdrb.loc[33, 'tahun_2012'] = 0, 0

# Visualization
# Figure Setting
plt.rcParams['figure.dpi'] = 120
plt.rcParams['figure.figsize'] = 6, 10

# Input By User
bydata1 = 2002
bydata2 = 2022

# Data Prep
kp_pivot = kp.pivot(index='provinsi', columns='tahun', values='kredit').reset_index()

# Plotting
kp_pivot.plot(
    x='provinsi',
    y=kp_pivot.loc[:, bydata1:bydata2].columns,
    kind='barh',
    stacked=True,
    colormap='tab20c')


# Plot Setting
plt.title('Jumlah Rata-Rata Kredit per Tahun Tiap Provinsi')
plt.xlabel('Jumlah Kredit (Milyar Rupiah)')
plt.ylabel('')
plt.xscale('log')
plt.show()