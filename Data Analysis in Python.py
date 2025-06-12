import pandas as pd

# Step 1: Load the Excel file correctly into df
df = pd.read_excel("c:/Users/Admin/Downloads/SharkTank_Cleaned.xlsx")

# Step 2: Add Founder Count column
df['Founder Count'] = df['Founders'].apply(lambda x: len(str(x).split(',')))

# Step 3: Print the updated DataFrame or save it
print(df[['Startup', 'Founders', 'Founder Count']])

# Optional: Save to a new Excel file
df.to_excel("c:/Users/Admin/Downloads/Updated_SharkTank_Cleaned.xlsx", index=False)
industry_funding = df.groupby('Industry')['Funding Amount (INR Cr)'].sum().sort_values(ascending=False)
print(industry_funding)
stage_analysis = df.groupby('Stage')['Funding Amount (INR Cr)'].agg(['count', 'mean', 'sum'])
print(stage_analysis)
founder_trend = df.groupby('Founder Count')['Funding Amount (INR Cr)'].mean()
print(founder_trend)
founder_trend = df.groupby('Founder Count')['Funding Amount (INR Cr)'].mean()
print(founder_trend)
industry_funding.to_csv("industry_funding.csv")
stage_analysis.to_csv("stage_analysis.csv")
founder_trend.to_csv("founder_trend.csv")
