import pandas as pd

def count_categories(data,pathologist,category):
    return data[(data["Bethesda Cathegory"]==category)&(data["CYTOPATHOLOGIST"]== pathologist)].shape[0]

def count_cases(data,pathologist):
    return data[data["CYTOPATHOLOGIST"]==pathologist].shape[0]

def count_by_result(data,pathologist,result):
    return data[(data["RESULT"]==result)&(data["CYTOPATHOLOGIST"]== pathologist)].shape[0]
