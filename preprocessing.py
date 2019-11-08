import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_path = 'data/'


def subcategorise(df):
    category_cut = df[df['category_name'].str.count('/') > 2.0]['category_name'].str.extract(
        r'(^[^\/]*\/[^\/]*\/[^\/]*)')
    temp = pd.concat([category_cut[0], df[df['category_name'].str.count('/') == 2.0]['category_name']]).str.split('/',
                                                                                                                  expand=True)
    df['category'] = temp[0]
    df['subcategory'] = temp[1]
    df['subsubcategory'] = temp[2]


train_set = pd.read_csv(data_path + 'train.tsv', delimiter='\t')
subcategorise(train_set)
print(train_set.head(10))
