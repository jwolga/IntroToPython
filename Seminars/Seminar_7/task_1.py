'''
Есть код:

transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой 
список
transormed_values = list(map(transformation, values))if values == transformed_values:
         print(‘ok’)else:
         print(‘fail’)
- В переменную transformation нужно прописать 
такую функцию, что бы в переменной transformed_values 
получилась копия списка values
'''
transformation = lambda el: el*2
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transformed_values = list(map(transformation, values))
print(transformed_values)
if values == transformed_values:
        print('ok')
else:
         print('fail')