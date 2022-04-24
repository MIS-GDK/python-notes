import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

titanic = pd.read_csv(r"C:\Users\Administrator\Desktop\titanic.csv")

# print(titanic)

# titanic.to_excel(
#     r"C:\Users\Administrator\Desktop\titanic.xlsx",
#     sheet_name="titanic",
#     index=False,
# )

titanic2 = pd.read_excel(
    r"C:\Users\Administrator\Desktop\titanic.xlsx", sheet_name="titanic"
)
# print(titanic2.info())
# print(titanic2)
# age_sex = titanic[["age", "sex"]]

# print(titanic[["age", "sex"]].shape)

# print(titanic[titanic["age"] > 28])
# print(titanic2[titanic2["age"].notna()])
adult_names = titanic2.loc[titanic2["age"] > 20, "name"]
print(adult_names)
