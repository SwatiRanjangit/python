import pandas as pd

data = pd.read_csv("C:/Users/Swati Ranjan/PycharmProjects/pythonProject1/emp.csv")
data.to_html('emp.html')
print("data converted into html file")
