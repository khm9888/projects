#unit13 - 친구의 친구 찾기

#vertex,edge

friend_info =dict()

friend_info["Summer"] = ["John","Justin","Mike"]
friend_info["Justin"] = ["Summer","May","John","Mike"]
friend_info["Mike"] = ["Summer","Justin"]
friend_info["May"] = ["Kim","Justin"]
friend_info["Kim"] = ["May"]
friend_info["John"] = ["Summer","Justin"]
friend_info["Tom"] = ["Jerry"]
friend_info["Jerry"] = ["Tom"]

print(friend_info)

def find_friends(friend_info,name):
    qu = []
    done = []
    qu.append((name,0))
    done.append(name)
    while qu:
        friend,d = qu.pop(0)
        print(friend,d)
        for x in friend_info[friend]:
            if x not in done:
                qu.append((x,d+1))
                done.append(x)
    return done 
print(find_friends(friend_info,"Tom"))
print(find_friends(friend_info,"Summer"))

#연습문제 15-1

vertex_dict = dict()

vertex_dict[1] = [2,3]
vertex_dict[2] = [1,4,5]
vertex_dict[3] = [1]
vertex_dict[4] = [2]
vertex_dict[5] = [2]

def find_vertex(node_num):
    qu=list()
    done=list()
    qu.append(node_num)
    done.append(node_num)
    while qu:
        find_num = qu.pop(0)
        print(find_num)
        for num in vertex_dict[find_num]:
            if num not in done:
                qu.append(num)
                done.append(num) 
    return done

find_vertex(1)

#15-2 과정 생략합니다.
    
