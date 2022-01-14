print("loss")
print(loss)
print("r2")
print(r2)
print("y_test[:10]")
print(y_test[:10])
print("y_pre[:10]")
print(y_pre[:10])



#############################################################

# # 결과 텍스트 파일로 저장하기 - acc
name=__file__.split("\\")[-1]
path=__file__[:-len(name)]+"results/"+f"{name}.txt"

#새로 쓸지, 아니면 추가할지 _ 없으면 새로 생성한다.
mode="a"
with open(path,mode,encoding="utf-8") as file:
    
    file.write("\n")
    file.write("-"*20+"\n")
    file.write(f"{name}\n")

    file.write("\n")
    file.write("조건추가\n")
    file.write(f"epochs\n")
    file.write(f"{epochs}\n")
    
    file.write("\n")
    file.write("loss\n")
    file.write(f"{loss}\n")
    file.write("acc\n")
    file.write(f"{acc}\n")

    file.write("\n")
    file.write("y_test[:10]\n")
    file.write(f"{y_test[:10]}\n")
    file.write("y_pre[:10]\n")
    file.write(f"{y_pre[:10]}\n")
    file.write("-"*20+"\n")
    file.write("\n")


##################################################################





# # dict_cnt.txt 생성
# path = "dict_cnt.txt"
# with open(path,"w",encoding="utf-8") as file:
#     file.write("dict_cnt = {}\n")


# # print("loss")
# # print(loss)
# # print("r2")
# # print(r2)
# # print("y_test[:10]")
# # print(y_test[:10])
# # print("y_pre[:10]")
# # print(y_pre[:10])




