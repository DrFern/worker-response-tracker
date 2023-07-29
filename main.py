import pandas as pd
import openpyxl

dataframe = pd.read_excel('/Users/rajeshshah/Desktop/Banking/arnav_input_file.xlsx')
#step_dict = dataframe.to_dict()
#or key in step_dict:
#    print(key)

for i in dataframe.index:
    # , dataframe['StepType'][i]
    if dataframe['StepType'][i] == 'good step':
        print(dataframe['StepRep'][i], "- ", end="")
        print(dataframe['StepType'][i], "- ", end="")
        print(dataframe['StepTime'][i])
    else:
        pass
print("\n\n")
print(dataframe)
