# Import Pandas 
import pandas as pd

# Create a simple data frame
data = {
    'rocket': [
        'Falcon 1'
        , 'Falcon 9'
        , 'Falcon Heavy'
    ],
    'launches':[5, 100, 3],
}


# Dump dataframe
df = pd.DataFrame(data)

# print(df)
# print(df['rocket'])


# Filter rows
falcon9_df = df[df['rocket'] == 'Falcon 9']
print(falcon9_df)

# Add columns
df['success_rate'] = [.4, .90, 1]
print(df)


# only show > 5 launches
gt_5_launches = df[df['launches'] > 5]
print(gt_5_launches)
