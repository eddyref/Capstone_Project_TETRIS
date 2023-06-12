# Modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from numerize import numerize
import geopandas as gpd

# Import dataframe
kp = pd.read_csv(r'C:\Users\Fery\Desktop\TETRIS Data Analytics\Capstone Project\Datasets\kredit_provinsi.csv')
k_mk = pd.read_csv(r'C:\Users\Fery\Desktop\TETRIS Data Analytics\Capstone Project\Datasets\kredit_modal_kerja_bank.csv')
k_i = pd.read_csv(r'C:\Users\Fery\Desktop\TETRIS Data Analytics\Capstone Project\Datasets\kredit_investasi_bank.csv')
k_k = pd.read_csv(r'C:\Users\Fery\Desktop\TETRIS Data Analytics\Capstone Project\Datasets\kredit_konsumsi_bank.csv')
pdrb = pd.read_csv(r'C:\Users\Fery\Desktop\TETRIS Data Analytics\Capstone Project\Datasets\laju_pdrb.csv')
# indo_map = gpd.read_file(r'C:\Users\Fery\Desktop\TETRIS Data Analytics\Capstone Project\Batas Provinsi SHP\Batas Provinsi.shp')

# # Mengisi missing value dengan nilai mean
col_pdrb = pdrb.columns.values.tolist()
pdrb.loc[33, 'tahun_2011'], pdrb.loc[33, 'tahun_2012'], pdrb.loc[33, 'tahun_2013'] = 0, 0, 0
pdrb.loc[34, 'tahun_2015'] = pdrb.transpose()[34].loc[col_pdrb[2:]].mean()

# Lookup dataframe
# print(kp.head())
# print(pdrb.head())
# print(k_k.head())
# print(k_i.head())
# print(k_mk.head())

# # Visualisasi data kredit menurut provinsi
kp_pivot = kp.pivot(index='provinsi', columns='tahun', values='kredit').reset_index()
#
# kp_pivot.plot(
#     x='provinsi',
#     kind='barh',
#     stacked=True,
#     colormap='tab20c_r'
# )
#
# plt.title('Jumlah Rata-Rata Kredit per Tahun Tiap Provinsi')
# plt.xlabel('Jumlah Kredit (Milyar Rupiah)')
# plt.ylabel('')
# plt.xscale('log')
# plt.show()

# Visualisasi Hubungan Kredit dan PDRB
pdrb.columns = ['no.', 'provinsi', 'tahun_2011', 'tahun_2012', 'tahun_2013', 'tahun_2014', 'tahun_2015',
                'tahun_2016', 'tahun_2017', 'tahun_2018', 'tahun_2019', 'tahun_2020', 'tahun_2021', 'tahun_2022']
kp_pdrb = pd.melt(pdrb, id_vars=['no.', 'provinsi'], var_name='tahun', value_name='PDRB')
# print(kp_pdrb.join(kp[kp['tahun'] >= 2011].reset_index(), on='provinsi'))
kp_n = kp[kp['tahun'] >= 2011].reset_index()
data = kp_pdrb.join(kp_n, on='provinsi')
print(data)
# sns.scatterplot(
#     data=kp_pdrb,
#     x=
# )


# # Visualisasi Kredit Berdasarkan Jenis Penggunaan
# k_k_tahun = k_k.groupby('tahun').sum()
# k_i_tahun = k_i.groupby('tahun').sum()
# k_mk_tahun = k_mk.groupby('tahun').sum()
# k_k_tahun['jenis'] = ['konsumsi' for i in range(k_k_tahun.shape[0])]
# k_i_tahun['jenis'] = ['investasi' for j in range(k_i_tahun.shape[0])]
# k_mk_tahun['jenis'] = ['modal kerja' for k in range(k_mk_tahun.shape[0])]
#
# k_jenis = pd.concat([k_k_tahun, k_i_tahun, k_mk_tahun]).reset_index()
# k_pivot = k_jenis.pivot(index='tahun', columns='jenis', values='kredit').reset_index()
#
# k_pivot.plot(
#     x='tahun',
#     kind='bar',
#     stacked=True,
#     colormap='tab20c_r'
# )
#
# x_ax = [0.5*i*(10**6) for i in range(1, 11)]
#
# plt.title('Jumlah Rata-Rata Kredit per Tahun Berdasarkan Jenis Penggunaan')
# plt.xticks(rotation=0)
# plt.yticks(x_ax, [numerize.numerize(n) for n in x_ax])
# plt.ylabel('Jumlah Kredit (Milyar Rupiah)')
# plt.xlabel('Tahun')
#
# plt.show()