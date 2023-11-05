import pandas as pd

df = pd.read_csv("titanic.csv")

#print(df)

#print(df.head(8)) # to print the top 8 data in the df

#print(df.tail(3)) # to print the last 3 data in the df

#print(df.describe()) #gives the description of the data in mathematical form. Only numerical data is considered.

#print(df.info()) # to find the type of the data and the necessary data in the df

print(df.isnull().sum()) #returns a DataFrame object where all the values are replaced with a Boolean value True for NULL values, and otherwise False.

num = df['Age'].mean() # finding the mean of age
print(num) # printing the mean of age

#print(df['Age']) # printing only the age in the df

df['Age'] = df['Age'].fillna(num)

print(df['Age'])

#print(df[['Age','Survived','Sex']])

#print(df[df.index == 0]) #indexing of the df

#print(df[df.index.isin(range(10,15))])

#print(df.loc[10:15]) #similar to index. LOC means location

#print(df.loc[1]) 

#print(df.loc[[10,15,20,25]])

#when indexing or usiing loc for multiple elements make sure that [[]] brackets are used.

#print(df.iloc[10:15]) #same as index

#cp = df.loc[10:15,['Age','Survived','Sex']]
#print(cp)

#print(df.iloc[10:15,-1])

#print(df.query('Sex == "female" and Age > 50')) # query is used to print the required data by giving conditions and specific value

#grouping

#zed = df.groupby(['Sex']).size().plot(kind = 'bar')
#print(zed)

#print(df.groupby(['Sex','Pclass','Survived']).size())

#print(df.pivot_table("Survived", index=['Pclass','Sex'])) #pivot_table is used to visualise the table more efficiently

# date time

ack = pd.Timestamp(year = 2023, day = 27, month = 7, hour = 23, minute=23)

print(ack)

print(pd.Timestamp('2023-07-07'))

ad = pd.Timestamp("June 26, 2023")
print(ad)

print(ad.month_name())
print(ad.day_name())
print(ad.year)
print(ad.day_of_week)
