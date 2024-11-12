from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'data/test_data.CSV'
df = pd.read_csv(file_path, encoding='cp949')

@api_view(['GET',])
def invert(request):
    data = df.to_dict('records')
    return JsonResponse({
        'data' : data,
    })

@api_view(['GET',])
def preprocess(request):
    preprocessed_df = df.fillna('NULL')
    data = preprocessed_df.to_dict('records')
    return JsonResponse({
        'data' : data,
    })


@api_view(['GET',])
def age(request):
    new_df = df.copy()
    mean_age = new_df['나이'].mean()

    new_df['평균과의 차이'] = abs(new_df['나이'] - mean_age)
    sorted_df = new_df.sort_values(by=['평균과의 차이']).head(10)

    sorted_df = sorted_df.to_dict('records')
    return JsonResponse({  
        'sorted_df': sorted_df,
        })