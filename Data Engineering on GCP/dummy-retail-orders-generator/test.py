import pandas as pd

d = [{"name":"Avinash","id":1},
     {"name":"Avi","id":2}]

df=pd.DataFrame(d)

print(df.head(5))

df.to_json(indent=False,lines=True,path_or_buf="json_output_1234567890.json",orient='records')