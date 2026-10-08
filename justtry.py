import pandas as pd

df = pd.read_csv("car_purchasing_data.csv", index_col="Customer Name")

# print(df.loc['Pearl'])

# name = input("Enter a name: ")

# try:
#     print(df.loc[name, ['age', 'salary']])
# except:
#     print(f"{name} does not exists")

# high_salary = df[df['salary'] >= 80000]
# print(high_salary)

# print()
# print()

# FILTER
# old_age = df[df['age'] > 50]
# print(old_age)

# filter_1 = df[(df['age'] > 50) & (df['salary'] > 80000)]
# print(filter_1)

# print()
# print()

# filter_2 = df[(df['gender'] == 0 | (df['debt'] > 9000))]
# print(filter_2)

# AGGREGATE FUNCTIONS
# whole data frame
# print(df.mean(numeric_only=True))
# print()
# print(df.sum(numeric_only=True))
# print()
# print(f"minimum of the numeric only:\n{df.min(numeric_only=True)}")
# print()
# print(f"maximun of the numeric only:\n{df.max(numeric_only=True)}")
# print()
# print(df.count())

# for a single column
# print(f"mean of age: {df['age'].mean()}")
# print(f"sum of age: {df['age'].sum()}")
# print(f"minimun debt: {df['debt'].min()}")
# print(f"maximum salary: {df['salary'].max()}")
# print(f"Total number of emails: {df['Customer e-mail'].count()}")

# group_1 = df.groupby("gender")
# # print(group_1['debt'].mean())
# # print(group_1['debt'].sum())
# # print(group_1['debt'].min())
# # print(group_1['debt'].max())
# print(group_1['Customer e-mail'].count())

# DATA CLEANING
#df = df.drop(columns=['Country', 'gender'])
# dropna (drop not available): columns with NaN values
# fillna ( fill not available) : columns with NaN values
# str.lower() : all strings to lower
#.replace({:}) : replace text in the dataframe. usually a dictionary

print(df)