import pandas as pd
import numpy as np

# Generate dummy data
np.random.seed(42)
data = {
    'income': np.random.randint(20000, 150000, 200),
    'essential_spending': np.random.randint(10000, 80000, 200),
    'discretionary_spending': np.random.randint(2000, 40000, 200),
    'savings': np.random.randint(1000, 40000, 200)
}
df = pd.DataFrame(data)

# Label based on rule
def label_financial_health(row):
    savings_rate = row['savings'] / row['income']
    if savings_rate >= 0.2:
        return 'Healthy'
    elif 0.1 <= savings_rate < 0.2:
        return 'Moderate'
    else:
        return 'Poor'

df['financial_health'] = df.apply(label_financial_health, axis=1)
print(df.head())

df.to_csv('dummy_financial_data.csv', index=False)