import pandas as pd

i = 0

train = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/train_{i}.csv")
val = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/val_{i}.csv")
test = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/test_{i}.csv")


train.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/train.csv",index=0)
val.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/val.csv",index=0)
test.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/test.csv",index=0)
