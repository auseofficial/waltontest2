import pandas as pd
import json

data = {
    'a': [10, 20, 10, 30, 40, 50, 40, 70],
    'b': [20, 30, 70, 60, 10, 20, 80, 10]
}

df = pd.DataFrame(data)

a_unique = df.a.unique()
b_unique = df.b.unique()

df_sum_unique = df.values.sum()
df_average_unique = df.mean()

to_be_json_dict = dict(df_average_unique)
to_be_json_dict['sum'] = float(df_sum_unique)


with open('output.json', 'w') as output:
    json.dump(to_be_json_dict, output)