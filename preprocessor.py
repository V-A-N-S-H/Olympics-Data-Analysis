import pandas as pd

def preprocess(df, region_df):
    
    # filtering the summer olympics
    df = df[df['Season'] == 'Summer']
    
    # merging the datasets
    df = df.merge(region_df, on='NOC', how='left')

    # dropping duplicates
    df.drop_duplicates(inplace=True)

    # one hot encoding
    df = pd.concat([df, pd.get_dummies(df['Medal'], dtype=int)], axis=1)

    return df