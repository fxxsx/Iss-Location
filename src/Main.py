import pandas as pd
import plotly.express as px
url = 'http://api.open-notify.org/iss-now.json' #create a variable
df = pd.read_json(url) #read the data
df['latitude'] = df.loc['latitude', 'iss_position']   #create a new column that consists of latitude and iss_position
df['longitude'] = df.loc['longitude', 'iss_position'] #same here but this time it's longitude
df.reset_index(inplace=True)
df = df.drop(['index', 'message'], axis=1) #drop the index and the message, they are not needed
fig = px.scatter_geo(df, lat='latitude', lon='longitude')  #scatter the DataFrame
fig.show() #show where the ISS is
