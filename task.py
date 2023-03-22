import random
 import pandas as pd
 import numpy as np

 lst = ['robot'] * 10
 lst += ['human'] * 10
 random.shuffle(lst)
 data = pd.DataFrame({'whoAmI': lst})
 print(data)
 # Создаем новый DataFrame со всеми возможными значениями и заполняем нулями
 categories = pd.DataFrame({'whoAmI': data['whoAmI'].unique()})
 one_hot = pd.DataFrame(np.zeros((len(categories), len(categories))))

 # Заполняем one_hot соответствующими значениями
 for i, categ in enumerate(categories['whoAmI']):
     one_hot.iloc[i][categ] = 1

 # Добавляем столбцы one_hot к исходному DataFrame
 for i, categ in enumerate(categories['whoAmI']):
     data[categ] = np.where(data['whoAmI'] == categ, 1, 0)

 print(data.head(20))