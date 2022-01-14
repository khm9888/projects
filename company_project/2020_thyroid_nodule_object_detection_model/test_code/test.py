values=[[1,5],[6,2],[3,3]]

# v=sorted(values,key= lambda  v : values[0],reverse=True)
# v=sorted(values,key= lambda  v : values[1],reverse=False)

v= sorted(values,key= lambda  v : v[0],reverse=True)
print(v)