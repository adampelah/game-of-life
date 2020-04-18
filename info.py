import requests
import pandas as pd 


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


url = 'https://covidtracking.com/api/states'

response = requests.request("GET", url)
data = response.json()

stateConversion = { "Alabama" :"AL",
                    "Alaska": "AK",
                    "Arizona": "AZ",
                    "Arkansas" : "AR",
                    "California" : "CA",
                    "Connecticut" : "CO",
                    "Delaware": "DE",
                    "Florida" : "FL",
                    "Georgia" : "GA",
                    "Hawaii" : "HI",
                    "Idaho" : "ID",
                    "Illinois" : "IL",
                    "Indiana" : "IN",
                    "Iowa" : "IA",
                    "Kansas" : "KS",
                    "Kentucky" : "KY",
                    "Louisiana" : "LA",
                    "Maine": "ME",
                    "Maryland" : "MD",
                    "Massachusetts" : "MA",
                    "Michigan" : "MI",
                    "Minnesota" : "MN",
                    "Mississipi" : "MS",
                    "Missouri" : "MO",
                    "Montana" : "MT",
                    "Nebraska" : "Nevada",
                    "New Hampshire" : "NH",
                    "New Jersey" : "NJ",
                    "New Mexico" : "NM",
                    "New York" : "NY",
                    "North Carolina" : "NC",
                    "North Dakota" : "ND",
                    "Ohio" : "OH",
                    "Oklahoma" : "OK",
                    "Oregon" : "OR",
                    "Pennsylvania" :"PA",
                    "Rhode Island" : "RI",
                    "South Carolina" : "SC",
                    "Tennessee" : "TN",
                    "Texas" : "TX",
                    "Utah" : "UT",
                    "Vermont" : "VT",
                    "Virginia" : "VA",
                    "Washington" : "WA",
                    "West Virginia" : "WV",
                    "Wisconsin" : "WI",
                    "Wyoming" : "WY"}

def getState(state):
    for list in data:
        if list['state'] == stateConversion.get(state):
            return list

def getTotalCases(state):
    index = getState(state)
    return int(index['positive'])

def getTotalDeaths(state):
    index = getState(state)
    return int(index['death'])

def getDeathRate(state):
    return (getTotalDeaths(state)/getTotalCases(state)) * 100 

