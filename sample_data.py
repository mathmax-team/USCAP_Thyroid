"""File to generate sample data for testing."""
from datetime import date, timedelta, datetime
import random
import math
import pandas as pd
import numpy as np


#Initialization of variables
days = 90
amplitude = 20
displacement = 50
noise = 0.4
day = date.today().day
month = date.today().month
year = date.today().year

if month == 1:
    year = year - 1
    month = 12

last_month_date = date(year, month -1, day)
last_week_date = date.today() - timedelta(days = 7)
last_year_date = date.today() - timedelta(days = 365)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Initial Lists
test_type = ['liquid based', 'conventional','another type', 'fourth type', 'just another']
adequacy_list = [{'satisfactory': 'Yes'},{'satisfactory': 'No', 'processed': 'Not processed'},{'satisfactory': 'No', 'processed': 'processed'}]
results_list = ['negative', 'ASC-US', 'ASC-H', 'LSIL', 'MSIL', 'SCC', 'AC', 'JJJ', 'KKK', 'LLL']
genotype_list = ['16','18']


#tree map data
# # Second Graph definition
tree_values = [100, 40, 60, 30, 30]
tree_labels = ["Satisfactory","Yes", "No", "Processed", "Not Processed"]
tree_parents = ["", "Satisfactory", "Satisfactory", "No", "No"]


#Data Generator
def sin_data_generate(N,A,S,R):
    """To generate sinusoidal data."""
    x = np.arange(0,N,1)
    noise = []
    for j in range(N):
        noise.append(R*random.choice(range(-3,3)))
    noise = np.array(noise)
    y = A*np.sin(30*x/(2*math.pi))+S
    y = y + noise
    return [x,y]

initial_df = pd.DataFrame()
test_df = pd.DataFrame(columns=['day', 'type', 'adequacy', 'result', 'mvp', 'cytology', 'hystology'])
choices = ['true positive', 'false positive', 'false negative', 'true negative']

def get_test_quality(cytology, hystology):
    """Get quality test based on cytology and hystology results."""
    if cytology == 'positive' and hystology == 'positive':
        test_quality = 'true positive'
    if cytology == 'positive' and hystology == 'negative':
        test_quality = 'false positive'
    if cytology == 'negative' and hystology == 'positive':
        test_quality = 'false negative'
    if cytology == 'negative' and hystology == 'negative':
        test_quality = 'true negative'
    return test_quality



def generate_sample_data():
    """Create Sample data."""
    for type in test_type:
        test_data = sin_data_generate(days, random.randint(5, 20), random.randint(20,50), noise)
        final = datetime.now()
        initial = final - timedelta(days=days-1)
        daterange = pd.date_range(initial, final, freq='D')
        initial_df['day'] = daterange
        initial_df[type] = test_data[1].astype(int)

    for type in test_type:
        type_list_samples = initial_df[type].values
        for index, number in enumerate(type_list_samples):
            for sample in range(number):
                day = initial_df['day'].iloc[index]
                adequacy = random.choices(adequacy_list)[0]
                result = random.choices(results_list, weights=[0.2, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1,0.1,0.1, 0.1])[0]
                mvp = random.choices(genotype_list)[0]
                cytology = random.choices(['positive', 'negative'], weights=[0.8, 0.2])[0]
                hystology = random.choices(['positive', 'negative'], weights=[0.8, 0.2])[0]
                test_quality = get_test_quality(cytology, hystology)
                new_row = {'day': day,'type': type, 'adequacy': adequacy, 'result': result, 'mvp': mvp, 'cytology': cytology, 'hystology': hystology, 'test_quality': test_quality }
                new_df = pd.DataFrame([new_row])
                test_df = pd.concat([test_df, new_df], axis=0, ignore_index=True)
                new_df.reset_index()
        print(test_df.tail(5))

    initial_df.to_csv('test_type_count_Camilo.csv')
    test_df.to_csv('test_dataframe_Camilo.csv')
#generate_sample_data()