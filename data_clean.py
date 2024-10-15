import pandas as pd
import re

data = pd.read_csv('bukukita/data_buku.csv', encoding='utf-8')


data['Penerbit									'] = data ['Penerbit									'].apply(lambda x: " ".join(re.findall(r"\w+", str(x))))
data['Text Bahasa'] = data ['Text Bahasa'].apply(lambda x: " ".join(re.findall(r"\w+", str(x))))

data.to_excel('dataclean_buku.xlsx', index=False)