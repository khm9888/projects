#순차적 모델이여야 함

#모델 save / load
model.save(__file__[:-3]+".h5")
name = __file__.split('\\')[-1][:-3]
model = load_model(__file__[:-len(__file__.split("\\")[-1])]+f"{name}.h5") # 실제로 가져올 때는 이름 바꿔야함