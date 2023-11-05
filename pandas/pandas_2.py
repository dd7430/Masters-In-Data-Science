import pandas as pd

veg = ["Onion", "Tomato", "Potato"]

f = pd.Series(veg, index=["a","b","c"]) #using .series() function the list is turned to a series

print(f)