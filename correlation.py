import numpy as np
import plotly.express as pe
import csv

with open ('data.csv') as file:
    f=csv.DictReader(file)
    fig=pe.scatter(f,x='Coffee in ml', y='sleep in hours')
    fig.show()

def dataSource(path):
    coffee=[]
    sleep=[]
    with open(path) as pf:
        csv_reader=csv.DictReader(pf)
        for row in csv_reader:
            coffee.append(int(row['Coffee in ml']))
            sleep.append(int(row['sleep in hours']))
                
    return {"x" : coffee, "y": sleep}

def findCorrelation(source):
    correlation=np.corrcoef(source['x'],source['y'])
    print("Correlation between hourse of sleep and the coffee intake is:  \n\t",correlation[0,1])

def main():
    path='data.csv'
    source=dataSource(path)
    findCorrelation(source)

main()