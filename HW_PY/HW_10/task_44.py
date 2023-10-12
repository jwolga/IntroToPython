'''
В ячейке ниже представлен код генерирующий
 DataFrame, которая состоит всего из 1 столбца.
   Ваша задача перевести его в one hot вид. 
   Сможете ли вы это сделать без get_dummies?
'''
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
columns = data['whoAmI'].unique()
one_hot_data = pd.DataFrame(0, index=data.index, columns=columns)

for column in columns:
    one_hot_data.loc[data['whoAmI'] == column, column] = 1
print(data)
print(one_hot_data)
