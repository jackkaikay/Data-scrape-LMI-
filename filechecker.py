import requests
import pandas as pd

socCode = 'soc_code.xlsx'
socCodeRead = pd.read_excel(socCode)

print(socCodeRead)

RCU_SocCode = []
RCU_Year = []
RCU_employment = []


res = requests.get('http://api.lmiforall.org.uk/api/v1/wf/predict?soc=1252')
print(res.text)

res = res.json()

for x in range(len(res['predictedEmployment'])):
    RCU_SocCode.append(res['soc'])

    print(res['predictedEmployment'][x]['year'])
    RCU_Year.append(res['predictedEmployment'][x]['year'])

    print(res['predictedEmployment'][x]['employment'])
    RCU_employment.append(res['predictedEmployment'][x]['employment'])

print(RCU_Year)
print(RCU_employment)


df = pd.DataFrame({'Soc_Code':RCU_SocCode, 'Year':RCU_Year,'Employment':RCU_employment})

print(df)

df.to_excel('Predict.xlsx', sheet_name='Predict')
