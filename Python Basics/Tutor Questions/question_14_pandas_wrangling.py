# Customer dataset,workout questions.
#
import pandas as pd
# 1.find the number of persons from India

df=pd.read_csv(r"C:\Users\Amjath Hassan\Entri\Live Notes\Python Basics\Tutor Questions\customer",names=["id","fname","lname","age","profession","country"])
# print(df.loc[df['country']=='india'].shape)
# print(len(df.loc[df['country']=='india']))

# 2.display the details of person from us

# print(df.loc[df['country']=='us'])
#
# 3.display fname,lname and age of all persons they are from China

# print(df.loc[df['country']=='china'][['fname','lname','age']])

# 4.display the details of maximum aged person from Ireland.

# print(df.loc[df['country']=='ireland'].sort_values(by='age',ascending=False).head())

# 5.display the profession of minimum aged person from India.

# print(df.loc[df['country']=='india'].sort_values(by='age',ascending=True).head(1)['profession'])

# 6.display the details of all persons their age is > 70


# print(df.loc[df['age']>70])

# 7.display the fname and profession of person their age is >  50 and their country is China.

# print(df.loc[(df['age']>50) & (df['country'] == 'china')][['fname','profession', 'country']])

# 8.display the persons who are piolets

# print(df.loc[df["profession"]=='Pilot'])

# 9.display the details of all teachers from UK

# print(df.loc[(df['profession'] =='Teacher' ) & (df['country'] == 'uk')])

# 10.display the fname,lname of person they are accountant from India.

# print(df.loc[(df['profession'] =='Teacher' ) & (df['country'] == 'uk')][['fname', 'lname']])

# 11.display the details if maxm aged 2 musicians from India.

# print(df.loc[(df["country"]=='india') & (df['profession'] == 'Musician')].sort_values(by="age", ascending=False).head(2))

# 12.check there is any missing values.

# print(df.isnull().sum())

# 13.display the details of teachers in descending order of their age.

# print(df.loc[df["profession"]=='Teacher'].sort_values("age",ascending=False))

# 14.display the details of min aged dancer from India.

# print(df.loc[(df["profession"]=='Dancer') & (df["country"]=='india')].sort_values("age",ascending=True).head(1))

# 15.display the data in the index 50 to 60.

# print(df.iloc[50:61])