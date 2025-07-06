
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv(r"C:\Users\USER\Documents\all_recs.csv (1)")
df.head()
Date	Location	Victim	Industry	Actor Location	Actor	Motive	Type	Sub-Type	Year
0	31/12/2022	Iran (Islamic Republic of)	State-run Iranian Websites	Public Administration	Undetermined	Undetermined	Protest	Disruptive	External Denial of Services	2022
1	31/12/2022	United States of America	Housing Authority of the City of Los Angeles (...	Public Administration	Undetermined	LockBit 3.0	Financial	Exploitative	Undetermined	2022
2	30/12/2022	Poland	Polish Parliament	Public Administration	Russian Federation	NoName057(16)	Protest	Disruptive	External Denial of Services	2022
3	30/12/2022	United States of America	CentraState Healthcare System	Health Care and Social Assistance	Undetermined	Undetermined	Undetermined	Disruptive	Undetermined	2022
4	30/12/2022	Iran (Islamic Republic of)	Iran Airlines	Transportation and Warehousing	Ukraine	rootkitsecurity	Protest	Disruptive	External Denial of Services	2022
year_order=df["Year"].value_counts().index
location_order=df['Location'].value_counts().index
motive_order=df['Motive'].value_counts().index
industry_order=df["Industry"].value_counts().index
df.describe()
Date	Location	Victim	Industry	Actor Location	Actor	Motive	Type	Sub-Type	Year
count	6687	6689	6689	6689	6689	6689	6689	6689	6685	6689
unique	1525	138	6175	21	36	437	10	5	63	6
top	22/04/2022	United States of America	Cartoon Network	Public Administration	Undetermined	Undetermined	Financial	Exploitive	Exploitation of Application Server	2022
freq	67	3439	14	1139	5569	4469	4541	3260	2026	1918
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6689 entries, 0 to 6688
Data columns (total 10 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0   Date            6687 non-null   object
 1   Location        6689 non-null   object
 2   Victim          6689 non-null   object
 3   Industry        6689 non-null   object
 4   Actor Location  6689 non-null   object
 5   Actor           6689 non-null   object
 6   Motive          6689 non-null   object
 7   Type            6689 non-null   object
 8   Sub-Type        6685 non-null   object
 9   Year            6689 non-null   object
dtypes: object(10)
memory usage: 522.7+ KB
plt.figure(figsize=(20,8))
plt.title("Attacck Frequency by Year")
sns.countplot(data=df,y="Year",order=year_order)
plt.xticks(rotation=45)
(array([   0.,  250.,  500.,  750., 1000., 1250., 1500., 1750., 2000.,
        2250.]),
 [Text(0, 0, ''),
  Text(0, 0, ''),
  Text(0, 0, ''),
  Text(0, 0, ''),
  Text(0, 0, ''),
  Text(0, 0, ''),
  Text(0, 0, ''),
  Text(0, 0, ''),
  Text(0, 0, ''),
  Text(0, 0, '')])
