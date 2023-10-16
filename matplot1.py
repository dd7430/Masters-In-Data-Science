import matplotlib.pyplot as plt
years = [1950,1960,1970,1980,1990, 2000,2010,2020]
gdp = [300.2, 597.1, 80.6, 1057.4, 3986.5, 9817.1, 13246.5, 29468.1]

plt.plot(years, gdp, color="blue", marker= "o", linestyle = "solid")

plt.title("Nominal GDP")

plt.ylabel("Billions of $")
plt.show()