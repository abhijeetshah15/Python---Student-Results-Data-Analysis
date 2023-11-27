# Abhijeet Shah
# Students Data Analysis Project
# CSV Data Source: Kaggle

# IMPORTS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------CREATING DATAFRAME-------------------------

df = pd.read_csv("StudentsData.csv")

# Printing first 5 rows using 'head()'
print(df.head())

# Printing numeric values data using 'describe()'
print(df.describe())

# Printing data types and non-null counts of columns using 'info()'
print(df.info())

# Printing total number of null values in each column using 'isnull()' and 'sum()'
print(df.isnull().sum())


# -------------------------OPTIMIZING DATA--------------------------

# Dropping the first column 'Unnamed' using 'drop()' - axis = 1 (vertical)
df = df.drop("Unnamed: 0", axis = 1)
print(df.head()) 

# -----------------------------ANALYSIS-----------------------------

# 1. Gender Distribution
plt.figure(figsize = (5, 5))
ax = sns.countplot(data = df, x = "Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()

        # Analysis: The number  of Female students is more than the number of male students


# 2. Relationship between Parents' education and student's scores
gb = df.groupby("ParentEduc").agg({"MathScore":'mean', "ReadingScore":'mean', "WritingScore":'mean'})
print(f"\n\n\nRelationship Between Parents' Education and Student's Scores\n\n{gb}")
plt.figure(figsize = (13, 6))
sns.heatmap(gb, annot = True)
plt.title("Relationship Between Parents' Education and Student's Scores")
plt.show()

        # Analysis: From the above chart, we have concluded that parents' education have a good impact on the student's scores.
        
# 3. Relationship between Parents' marital status on student's scores
gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean', "ReadingScore":'mean', "WritingScore":'mean'})
print(f"\n\n\nRelationship Between Parents' Marital Status and Student's Scores\n\n{gb1}")
plt.figure(figsize = (10, 6))
sns.heatmap(gb1, annot = True)
plt.title("Relationship Between Parents' Marital Status and Student's Scores")
plt.show()

        # Analysis: From the above analysis, we can understand that there is no/negligible impact of parents' marital status on student's scores.

# 4. Finding outliers of Math Score, Reading Score, and Writing Score
sns.boxplot(data = df, x = "MathScore")
plt.show()

sns.boxplot(data = df, x = "ReadingScore")
plt.show()

sns.boxplot(data = df, x = "WritingScore")
plt.show()

        #Analysis: From the above data, we can say that Math is comparatively a more difficult subject than Reading and Writing.

# 5. Distribution of Ethnic Groups
groupA = df.loc[(df["EthnicGroup"] == "group A")].count()
groupB = df.loc[(df["EthnicGroup"] == "group B")].count()
groupC = df.loc[(df["EthnicGroup"] == "group C")].count()
groupD = df.loc[(df["EthnicGroup"] == "group D")].count()
groupE = df.loc[(df["EthnicGroup"] == "group E")].count()

groups_Labels = ["Group A", "Group B", "Group C", "Group D", "Group E"]
groups_List = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]
plt.pie(groups_List, labels = groups_Labels, autopct = "%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()

    #Analysis: From the above chart, we can see that Group C is the majority and Group A is the minority.

