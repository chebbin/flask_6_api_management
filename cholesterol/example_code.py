import requests 
import pandas as pd 

df = pd.DataFrame({
    'hdl': [100, 121, 131, 140],
    'ldl': [80, 50, 80, 75]
})

df[:1]['hdl']


analysis = requests.get(
    url = 'unable to obtain the url',
    params = ({
        "hdl": df[:1]['hdl'],
        "ldl": df[:1]['ldl']
    })
)

analysis.text