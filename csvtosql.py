import sqlite3 as sq
import pandas as pd
conn=sq.connect('database.db')
df=pd.read_csv('file.csv')
print(df)

# datasets in dataframe(df)
#   id    age  gen   ht     wt  ap_hi  ap_lo  chol  gluc  smoke  alco  acti  card
#0    0  18393    2  168   62.0    110     80     1     1      0     0     1     0
#1    1  20228    1  156   85.0    140     90     3     1      0     0     1     0
#2    2  18857    1  165   64.0    130     70     3     1      0     0     0     1
#3    3  17623    2  169   82.0    150    100     1     1      0     0     1     1
#4    4  17474    1  156   56.0    100     60     1     1      0     0     0     0
#5    8  21914    1  151   67.0    120     80     2     2      0     0     0     0
#6    9  22113    1  157   93.0    130     80     3     1      0     0     1     0
#7   12  22584    2  178   95.0    130     90     3     3      0     0     1     1
#8   13  17668    1  158   71.0    110     70     1     1      0     0     1     0

df.to_sql(table_name,conn,index=False)
for line in db.execute('select * from table_name'):
  print(line)

#datasets in database (database.db) in {table_name} table....  
#(0, 18393, 2, 168, 62.0, 110, 80, 1, 1, 0, 0, 1, 0)
#(1, 20228, 1, 156, 85.0, 140, 90, 3, 1, 0, 0, 1, 0)
#(2, 18857, 1, 165, 64.0, 130, 70, 3, 1, 0, 0, 0, 1)
#(3, 17623, 2, 169, 82.0, 150, 100, 1, 1, 0, 0, 1, 1)
#(4, 17474, 1, 156, 56.0, 100, 60, 1, 1, 0, 0, 0, 0)
#(8, 21914, 1, 151, 67.0, 120, 80, 2, 2, 0, 0, 0, 0)
#(9, 22113, 1, 157, 93.0, 130, 80, 3, 1, 0, 0, 1, 0)
#(12, 22584, 2, 178, 95.0, 130, 90, 3, 3, 0, 0, 1, 1)
#(13, 17668, 1, 158, 71.0, 110, 70, 1, 1, 0, 0, 1, 0)

