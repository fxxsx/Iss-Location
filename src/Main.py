import pandas as pd
import plotly.express as px

url = 'http://api.open-notify.org/iss-now.json'

df = pd.read_json(url) #read the data

df['latitude'] = df.loc['latitude', 'iss_position'] 
df['longitude'] = df.loc['longitude', 'iss_position'] 
df.reset_index(inplace=True)

df = df.drop(['index', 'message'], axis=1)

def main():
  fig = px.scatter_geo(df, lat='latitude', lon='longitude')
  fig.show()

if __name__ == '__main__':
  main()
