import pandas as pd

df = pd.read_csv('miasta.csv')

print(df)

dict={'Rok':2010, 'Gdansk':460, 'Poznan':555, 'Szczecin':405}

df = df.append(dict, ignore_index=True)

print(df)

df.to_csv('miasta.csv', index=False)