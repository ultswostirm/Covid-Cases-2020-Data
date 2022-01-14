import pandas as panda
import plotly_express as plot

data=panda.read_csv("CovidData.csv")

chart=plot.line(data,x="date",y="cases",color="country",title="Covid Cases In Each Country")

chart.show()