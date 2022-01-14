xgb.save_model("./model/xgb_save/__file__[-15:-3].dat")

xgb2=XGBClassifier()

xgb2.load_model(f"./model/xgb_save/{__file__[-15:-3].dat}")