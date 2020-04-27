import requests
import pandas as pd
import json

Year = []
employment = []


res = requests.get('http://api.lmiforall.org.uk/api/v1/wf/predict/breakdown/qualification?soc=2033')




res = res.json()

print(res['soc'])






for len1 in range(len(res["predictedEmployment"])):
    print(res['predictedEmployment'][len1])

    for len2 in range(len(res['predictedEmployment'][len1]['breakdown'])):
        print(res['predictedEmployment'][len1]['year'])                             #YEAR
        print(res['predictedEmployment'][len1]['breakdown'][len2]['code'])          #CODE
        print(res['predictedEmployment'][len1]['breakdown'][len2]['name'])          #NAME
        print(res['predictedEmployment'][len1]['breakdown'][len2]['employment'])     #EMPLOYMENT
        try:
            print(res['predictedEmployment'][len1]['breakdown'][len2]['note'])      #NOTE
        except:
            print('No Note')











