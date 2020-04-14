import requests
import pandas as pd 

url = 'https://covidtracking.com/api/states'

response = requests.request("GET", url)
data = response.json()


def prepareData():
    populationData = pd.read_excel('populationExcel.xlsx', 0)
    for x in range (0, len(populationData.columns)):
        populationData.rename({"Unnamed: " + str(x): str(x)}, axis="columns", inplace=True)

    trash = 'table with row headers in column A and column headers in rows 3 through 4. (leading dots indicate sub-parts)'
    populationData.rename({trash: str(0)}, axis="columns", inplace=True)

    populationData = populationData.drop(['1', '2','3','4','5','6','7','8','9','10','11'], axis=1)
    populationData = populationData.drop([0,1,2,3,4,5,63,61, 60 , 59], axis=0)
    populationData.rename({'0': 'states'}, axis="columns", inplace=True)
    populationData.rename({'12': 'population'}, axis="columns", inplace=True)
    populationData.index = populationData['states']
    populationData = populationData.drop(columns='states')  
    return populationData
    
def getPopulation(input):
    state = "." + input
    data = prepareData()
    return int(data.at[state, 'population'])



def getState(state):
    for index,list in enumerate(data):
        if list['state'] == state:
            return list

def getTotalCases(state):
    index = getState(state)
    return int(index['positive'])

def getTotalDeaths(state):
    index = getState(state)
    return int(index['death'])

def getDeathRate(state):
    return (getTotalDeaths(state)/getTotalCases(state)) * 100 

print(getPopulation(input("what state?")))