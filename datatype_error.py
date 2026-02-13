import pandas as pd
data ={
    "Name": ["sneha", "preeti", "pavithra", "sanjana", "Darshini"],
    "Marks":["85","90","75","80","70"]
}
df=pd.DataFrame(data)
print(df.dtypes) 
df["Marks"]=df["Marks"].astype(int)
print(df.dtypes)
print(df["Marks"].mean())

# Problem 2:
data={
   "joining_date": ["2020-01-01", "2020-02-01", "2020-03-01", "2020-04-01", "2020-05-01"]

}
df = pd.DataFrame(data)
print(df.dtypes)
df["joining_date"]=pd.to_datetime(df["joining_date"])
print(df.dtypes)
print(df["joining_date"].dt.year)

# Problem 3 :
data = {
    "Salary":["50000","60000","55000","Not availabel"]
}
df = pd.DataFrame(data)
print(df.dtypes)

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
print(df)

