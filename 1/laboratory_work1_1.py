import pandas as pd

df = pd.read_excel("Laboratory_work1.xlsx") 
print("Стара таблиця:\n", df)

df = df.rename(columns={
    "Імʼя": "Name",
    "Фамілія": "Surname",
    "Вчений ступінь": "Degree"
})

print("Після зміни назви:\n", df)

new_order = ["Surname", "Name", "Degree"]
df = df[new_order]

print("Після перестановки:\n", df)
