import pandas as pd

Data ={
    "Customer_ID":[101,102,103,104,104],
    "Name":["Sneha","Preeti","Rohit","Sneha","Pavi"],
    "Purchase":[1000,3700,3789,3893,1010]

}
df = pd.DataFrame(Data)
print(df)

# TO FIND DUPLICATE DATA
print(df.duplicated())

# to find duplicate daa based on rows
print(df[df.duplicated()])
df_clean = df.drop_duplicates()
print(df_clean)

print(df.duplicated(subset="Customer_ID"))
print(df.drop_duplicates())
print(df.drop_duplicates(keep="last"))
print(df.drop_duplicates(keep=False))
