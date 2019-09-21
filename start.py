#A graph which show the startups frequency statewise
#Please ignore the comments...did them while testing and trying out different methods
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
df = pd.read_csv("startup_funding.csv")
dfs=pd.DataFrame()
dfd=pd.DataFrame()
dfd['Count'] = df['City  Location'].value_counts()
plt.figure(1)
print(dfd)
dfd['Count'].head(5).plot(kind='bar',rot=0)

# print(df.dtypes)
# print(df.head())
# df=df.fillna(value=0)
# for i in df['Startup Name']:
#     print(i,end=' ')
# for i in df['Amount in USD']:
#     print(i,end=' ')
# print(df['City  Location'].value_counts())

df=df.loc[(df['City  Location'] == 'Delhi') | (df['City  Location'] == 'New Delhi') | (df['City  Location'] == 'Noida') | (df['City  Location'] == 'Gurgaon')]
dfs[['Name','Amount','City']] = df[['Startup Name','Amount in USD','City  Location']]
print(dfs)

#dfs.replace(to_replace ="Undisclosed",value=00)
# dfs['Amount'] = dfs['Amount'].apply(lambda x: str(x.split()[0].replace(',', '')))
#
# dfs['Amount'] = dfs['Amount'].apply(lambda x: str(x.split()[0].replace('+', '')))
# dfs['Amount'] = dfs['Amount'].apply(lambda x: str(x.split()[0].replace('N/A', '')))
# dfs['Amount'] = dfs['Amount'].apply(lambda x: str(x.split()[0].replace('\\\\xc2\\\\xa0', '')))
# for index,i in enumerate(dfs['Amount']):
#     if i == 'Undisclosed' or i=='undisclosed':
#         dfs = dfs.drop([index], axis='rows')
# #
dfs=dfs.dropna()

dfs['Amount'] = dfs['Amount'].apply(lambda x: str(x.split()[0].replace(',', '')))
dfs['Amount']=dfs['Amount'].apply(lambda x: np.where(x.isdigit(),x,'0'))
dfs[['Amount']] = dfs[['Amount']].apply(pd.to_numeric)

print(dfs)

print(dfs.dtypes)

plt.figure(2)
dfs['City'].value_counts().plot(kind='bar',rot=0)

plt.figure(3)
dfs.sort_values("Amount", axis = 0, ascending = False,
                 inplace = True, na_position ='last')

dfs.head(5).plot(kind='bar',x='Name',y='Amount',rot=0)
plt.show()


#print(df)
# df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
#
# df3['A'] = pd.Series(list(range(len(df))))
#
# df3.plot(x='A', y='B')
# plt.show()
