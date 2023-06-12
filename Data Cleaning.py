# Modules
import pandas as pd

# Import dataframe
kp = pd.read_csv(r'C:\Users\Fery\Desktop\TETRIS Data Analytics\Capstone Project\Datasets\kredit_provinsi.csv')
k_mk = pd.read_csv(r'C:\Users\Fery\Desktop\TETRIS Data Analytics\Capstone Project\Datasets\kredit_modal_kerja_bank.csv')
k_i = pd.read_csv(r'C:\Users\Fery\Desktop\TETRIS Data Analytics\Capstone Project\Datasets\kredit_investasi_bank.csv')
k_k = pd.read_csv(r'C:\Users\Fery\Desktop\TETRIS Data Analytics\Capstone Project\Datasets\kredit_konsumsi_bank.csv')
pdrb = pd.read_csv(r'C:\Users\Fery\Desktop\TETRIS Data Analytics\Capstone Project\Datasets\laju_pdrb.csv')

# Mengecek ada atau tidaknya missing value
# print(kp.isna().sum())
# print(k_mk.isna().sum())
# print(k_i.isna().sum())
# print(k_k.isna().sum())
print(pdrb.isna().sum())
print()

# Detecting missing value
col_pdrb = pdrb.columns.values.tolist()
for i in range(len(col_pdrb)):
    if pdrb[col_pdrb[i]].isna().sum() == 1:
        for j in range(pdrb.shape[0]):
            if pdrb[col_pdrb[i]].isna().loc[j]:
                print(f"Data hilang:\n[tahun,provinsi]: {[col_pdrb[i],pdrb['provinsi'].loc[j]]}")

# Mengisi missing value dengan nilai mean
pdrb.loc[33, 'tahun_2011'], pdrb.loc[33, 'tahun_2012'], pdrb.loc[33, 'tahun_2013'] = 0, 0, 0
pdrb.loc[34, 'tahun_2015'] = pdrb.transpose()[34].loc[col_pdrb[2:]].mean()
print()
print(pdrb.to_string())
