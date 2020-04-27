import requests
import pandas as pd
import time

socCode= 'soc_code.xlsx'
socCodeRead = pd.read_excel(socCode)


PredictRCU_SocCode = []
PredictRCU_Year = []
PredictRCU_employment = []

def Predict():
    for x in range(len(socCodeRead)):
        x = socCodeRead.loc[x, 'SOC_CODE']
        print('http://api.lmiforall.org.uk/api/v1/wf/predict?soc=' + str(x))
        res = requests.get('http://api.lmiforall.org.uk/api/v1/wf/predict?soc=' + str(x))
        print(res.text)
        res = res.json()

        for x in range(len(res['predictedEmployment'])):
            PredictRCU_SocCode.append(res['soc'])

            print(res['predictedEmployment'][x]['year'])
            PredictRCU_Year.append(res['predictedEmployment'][x]['year'])

            print(res['predictedEmployment'][x]['employment'])
            PredictRCU_employment.append(res['predictedEmployment'][x]['employment'])

            df = pd.DataFrame({'Soc_Code': PredictRCU_SocCode, 'Year': PredictRCU_Year, 'Employment': PredictRCU_employment})

        df.to_excel('Predict.xlsx', sheet_name='Predict')
#------------------------------------------------------------------------------
PredictQualificationRCU_SocCode = []
PredictQualificationRCU_Year = []
PredictQualificationRCU_code = []
PredictQualificationRCU_name = []
PredictQualificationRCU_employment = []
PredictQualificationRCU_note = []

def PredictQualification():
    for x in range(len(socCodeRead)):
        x = socCodeRead.loc[x, 'SOC_CODE']
        print('http://api.lmiforall.org.uk/api/v1/wf/predict/breakdown/qualification?soc=' + str(x))
        res = requests.get('http://api.lmiforall.org.uk/api/v1/wf/predict/breakdown/qualification?soc=' + str(x))
        print(res.text)
        res = res.json()

        for len1 in range(len(res["predictedEmployment"])):
            print(res['predictedEmployment'][len1])

            for len2 in range(len(res['predictedEmployment'][len1]['breakdown'])):

                PredictQualificationRCU_SocCode.append(res['soc'])
                PredictQualificationRCU_Year.append(res['predictedEmployment'][len1]['year'])
                PredictQualificationRCU_code.append(res['predictedEmployment'][len1]['breakdown'][len2]['code'])
                PredictQualificationRCU_name.append(res['predictedEmployment'][len1]['breakdown'][len2]['name'])
                PredictQualificationRCU_employment.append(res['predictedEmployment'][len1]['breakdown'][len2]['employment'])
                try:
                    PredictQualificationRCU_note.append(res['predictedEmployment'][len1]['breakdown'][len2]['note'])
                except:
                    PredictQualificationRCU_note.append('No Note')


            df = pd.DataFrame({'Soc_Code': PredictQualificationRCU_SocCode, 'Year': PredictQualificationRCU_Year, 'Code': PredictQualificationRCU_code, 'Name': PredictQualificationRCU_name , 'Employment': PredictQualificationRCU_employment, 'Note': PredictQualificationRCU_note})

        df.to_excel('PredictQualification.xlsx', sheet_name='PredictQualification')
#------------------------------------------------------------------------------
PredictIndustRCU_SocCode = []
PredictIndustRCU_Year = []
PredictIndustRCU_code = []
PredictIndustRCU_name = []
PredictIndustRCU_employment = []
PredictIndustRCU_note = []

def PredictIndust():
    for x in range(len(socCodeRead)):
        x = socCodeRead.loc[x, 'SOC_CODE']
        print('http://api.lmiforall.org.uk/api/v1/wf/predict/breakdown/industry?soc=' + str(x))
        res = requests.get('http://api.lmiforall.org.uk/api/v1/wf/predict/breakdown/industry?soc=' + str(x))
        print(res.text)
        res = res.json()

        for len1 in range(len(res["predictedEmployment"])):
            print(res['predictedEmployment'][len1])

            for len2 in range(len(res['predictedEmployment'][len1]['breakdown'])):

                PredictIndustRCU_SocCode.append(res['soc'])
                PredictIndustRCU_Year.append(res['predictedEmployment'][len1]['year'])
                PredictIndustRCU_code.append(res['predictedEmployment'][len1]['breakdown'][len2]['code'])
                PredictIndustRCU_name.append(res['predictedEmployment'][len1]['breakdown'][len2]['name'])
                PredictIndustRCU_employment.append(res['predictedEmployment'][len1]['breakdown'][len2]['employment'])
                try:
                    PredictIndustRCU_note.append(res['predictedEmployment'][len1]['breakdown'][len2]['note'])
                except:
                    PredictIndustRCU_note.append('No Note')


            df = pd.DataFrame({'Soc_Code': PredictIndustRCU_SocCode, 'Year': PredictIndustRCU_Year, 'Code': PredictIndustRCU_code, 'Name': PredictIndustRCU_name , 'Employment': PredictIndustRCU_employment, 'Note': PredictIndustRCU_note})

        df.to_excel('PredictIndust.xlsx', sheet_name='PredictIndust')
#------------------------------------------------------------------------------

PredictStatusRCU_SocCode = []
PredictStatusRCU_Year = []
PredictStatusRCU_code = []
PredictStatusRCU_name = []
PredictStatusRCU_employment = []
PredictStatusRCU_note = []

def PredictStatus():
    for x in range(len(socCodeRead)):
        x = socCodeRead.loc[x, 'SOC_CODE']
        print('http://api.lmiforall.org.uk/api/v1/wf/predict/breakdown/status?soc=' + str(x))
        res = requests.get('http://api.lmiforall.org.uk/api/v1/wf/predict/breakdown/status?soc=' + str(x))
        print(res.text)
        res = res.json()

        for len1 in range(len(res["predictedEmployment"])):
            print(res['predictedEmployment'][len1])

            for len2 in range(len(res['predictedEmployment'][len1]['breakdown'])):

                PredictStatusRCU_SocCode.append(res['soc'])
                PredictStatusRCU_Year.append(res['predictedEmployment'][len1]['year'])
                PredictStatusRCU_code.append(res['predictedEmployment'][len1]['breakdown'][len2]['code'])
                PredictStatusRCU_name.append(res['predictedEmployment'][len1]['breakdown'][len2]['name'])
                PredictStatusRCU_employment.append(res['predictedEmployment'][len1]['breakdown'][len2]['employment'])
                try:
                    PredictStatusRCU_note.append(res['predictedEmployment'][len1]['breakdown'][len2]['note'])
                except:
                    PredictStatusRCU_note.append('No Note')


            df = pd.DataFrame({'Soc_Code': PredictStatusRCU_SocCode, 'Year': PredictStatusRCU_Year, 'Code': PredictStatusRCU_code, 'Name': PredictStatusRCU_name , 'Employment': PredictStatusRCU_employment, 'Note': PredictStatusRCU_note})

        df.to_excel('PredictStatus.xlsx', sheet_name='PredictStatus')
#------------------------------------------------------------------------------
PredictRegionRCU_SocCode = []
PredictRegionRCU_Year = []
PredictRegionRCU_code = []
PredictRegionRCU_name = []
PredictRegionRCU_employment = []
PredictRegionRCU_note = []
def PredictRegion():
    for x in range(len(socCodeRead)):
        x = socCodeRead.loc[x, 'SOC_CODE']
        print('http://api.lmiforall.org.uk/api/v1/wf/predict/breakdown/region?soc=' + str(x))
        res = requests.get('http://api.lmiforall.org.uk/api/v1/wf/predict/breakdown/region?soc=' + str(x))
        print(res.text)
        res = res.json()

        for len1 in range(len(res["predictedEmployment"])):
            print(res['predictedEmployment'][len1])

            for len2 in range(len(res['predictedEmployment'][len1]['breakdown'])):

                PredictRegionRCU_SocCode.append(res['soc'])
                PredictRegionRCU_Year.append(res['predictedEmployment'][len1]['year'])
                PredictRegionRCU_code.append(res['predictedEmployment'][len1]['breakdown'][len2]['code'])
                PredictRegionRCU_name.append(res['predictedEmployment'][len1]['breakdown'][len2]['name'])
                PredictRegionRCU_employment.append(res['predictedEmployment'][len1]['breakdown'][len2]['employment'])
                try:
                    PredictRegionRCU_note.append(res['predictedEmployment'][len1]['breakdown'][len2]['note'])
                except:
                    PredictRegionRCU_note.append('No Note')


            df = pd.DataFrame({'Soc_Code': PredictRegionRCU_SocCode, 'Year': PredictRegionRCU_Year, 'Code': PredictRegionRCU_code, 'Name': PredictRegionRCU_name , 'Employment': PredictRegionRCU_employment, 'Note': PredictRegionRCU_note})

        df.to_excel('PredictRegion.xlsx', sheet_name='PredictRegion')
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
PredictGenderRCU_SocCode  = []
PredictGenderRCU_Year = []
PredictGenderRCU_code = []
PredictGenderRCU_name = []
PredictGenderRCU_employment = []
PredictGenderRCU_note = []
def PredictGender():
    for x in range(len(socCodeRead)):
        x = socCodeRead.loc[x, 'SOC_CODE']
        print('http://api.lmiforall.org.uk/api/v1/wf/predict/breakdown/gender?soc=' + str(x))
        res = requests.get('http://api.lmiforall.org.uk/api/v1/wf/predict/breakdown/gender?soc=' + str(x))
        print(res.text)
        res = res.json()

        for len1 in range(len(res["predictedEmployment"])):
            print(res['predictedEmployment'][len1])

            for len2 in range(len(res['predictedEmployment'][len1]['breakdown'])):

                PredictGenderRCU_SocCode.append(res['soc'])
                PredictGenderRCU_Year.append(res['predictedEmployment'][len1]['year'])
                PredictGenderRCU_code.append(res['predictedEmployment'][len1]['breakdown'][len2]['code'])
                PredictGenderRCU_name.append(res['predictedEmployment'][len1]['breakdown'][len2]['name'])
                PredictGenderRCU_employment.append(res['predictedEmployment'][len1]['breakdown'][len2]['employment'])
                try:
                    PredictGenderRCU_note.append(res['predictedEmployment'][len1]['breakdown'][len2]['note'])
                except:
                    PredictGenderRCU_note.append('No Note')


            df = pd.DataFrame({'Soc_Code': PredictGenderRCU_SocCode, 'Year': PredictGenderRCU_Year, 'Code': PredictGenderRCU_code, 'Name': PredictGenderRCU_name , 'Employment': PredictGenderRCU_employment, 'Note': PredictGenderRCU_note})

        df.to_excel('PredictGender.xlsx', sheet_name='PredictGender')
#------------------------------------------------------------------------------

RepDemRCU_SocCode = []
RepDemRCU_sYear = []
RepDemRCU_eYear = []
RepDemRCU_employment = []

def RepDemRCU():
    for x in range(len(socCodeRead)):
        x = socCodeRead.loc[x, 'SOC_CODE']
        print('http://api.lmiforall.org.uk/api/v1/wf/replacement_demand?soc=' + str(x))
        res = requests.get('http://api.lmiforall.org.uk/api/v1/wf/replacement_demand?soc=' + str(x))
        print(res.text)
        res = res.json()

        for x in range(len(res['predictedEmployment'])):
            RepDemRCU_SocCode.append(res['soc'])

            RepDemRCU_sYear.append(res['predictedEmployment'][x]['start_year'])

            RepDemRCU_eYear.append(res['predictedEmployment'][x]['end_year'])

            RepDemRCU_employment.append(res['predictedEmployment'][x]['rate'])

            df = pd.DataFrame({'Soc_Code': RepDemRCU_SocCode,  'Start_Year': RepDemRCU_sYear, 'end_year': RepDemRCU_eYear, 'rate': RepDemRCU_employment})

        df.to_excel('RepDemRCU.xlsx', sheet_name='RepDemRCU')
#------------------------------------------------------------------------------

#-----------------------------------------------------
# RUN CODE HERE ------- PICK WHAT DATA YOU NEED ------
#-----------------------------------------------------
RepDemRCU()

