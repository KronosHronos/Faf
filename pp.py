import pandas as pd 
import numpy as np 
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)
 
# Получение one-hot представления без использования get_dummies
one_hot = pd.get_dummies(data['whoAmI'])

# Объединение one-hot представления с исходным DataFrame
data = pd.concat([data, one_hot], axis=1)

data.head()
