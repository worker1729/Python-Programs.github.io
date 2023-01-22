import pandas as pd
name = ["Mike", "Rachel", "Eunice"]
age = [25, 35, 19]
gender = ["Male", "Female", "Female"]
columns = {"Name": name,
"Age": age, "Gender": gender}
a = pd.DataFrame(columns)
a.to_csv("demo.csv", index=False)
print(a)
