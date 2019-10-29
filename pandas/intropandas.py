import pandas
df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns = ["price","Age","Value"],index = ["first","second"])

print("output of Pandas Dataframe :\n",df1,"\n")

mean = df1.mean();

print("output of Pandas Data mean for each col :\n",mean,"\n")

meanall = df1.mean().mean();

print("output of Pandas Data mean for all col :\n",meanall,"\n")

meanprice = df1.price.mean();

print("output of Pandas Data mean for price col :\n",meanprice,"\n")