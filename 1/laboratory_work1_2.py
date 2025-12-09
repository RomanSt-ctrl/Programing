import pandas as pd

df = pd.read_excel("Laboratory_work1.xlsx")

description = df.describe(include='all')     
correlation = df.corr(numeric_only=True)      

with pd.ExcelWriter("analysis_results.xlsx") as writer:
    description.to_excel(writer, sheet_name="Description")
    correlation.to_excel(writer, sheet_name="Correlation")

print("Файл 'analysis_results.xlsx' успішно створено!")

print("====== Описова статистика (лист 1) ======")
print(description)

print("\n====== Кореляційна матриця (лист 2) ======")
print(correlation)

