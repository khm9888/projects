    name=__file__.split("\\")[-1][:-3] #py확장자 포함 미포함
    submission.to_csv(f"./data/dacon/comp1/{name}_{size}_{str(mae)[:5]}_{learning_rate}.csv", header = ["hhb", "hbo2", "ca", "na"], index = True, index_label="id" )