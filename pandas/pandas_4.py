import pandas as pd

g = pd.DataFrame([['tomato',30],['potato',50], ['onion', 40]], columns=['vegetables', 'rate'])

#pd.DataFrame is used to create a multidimensional data and converts the list to a dataframe
#columns is used to name the dataframe above.

print(g)