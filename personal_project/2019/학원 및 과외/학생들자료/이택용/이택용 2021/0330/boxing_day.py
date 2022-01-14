def read_boxes(text_file):
    dict_word = dict()
    with open(text_file,"r") as file:
        f=file.readlines()
        for i in f:
            # print(i.strip().split(","))
            key, value = i.strip().split(",")
            dict_word[key]=value

    assert set(dict_word.keys())==set(dict_word.values()), "invalid boxes"
    return dict_word

def cycle(word,read_boxes):
    first_word = word
    words = list()
    words.append(word)
    assert word in read_boxes, "invalid item"
    while read_boxes[word] and read_boxes[word]!=first_word:
        word = read_boxes[word]
        words.append(word)
    
    return tuple(words)
    

def longest_cycle(read_boxes):
    cnt = 0
    for word in read_boxes.keys():
        l=len(cycle(word,read_boxes))
        if l>cnt:
            cnt = l
    return cnt


boxes = read_boxes('boxes01.txt')
# input(boxes)
v=boxes
# {'guitar': 'conga', 'saxophone': 'banjo', 'conga': 'maracas', 'drum set': 'saxophone', 'trumpet': 'guitar', 'bass guitar': 'trombone', 'synthesizer': 'trumpet', 'banjo': 'drum set', 'trombone': 'bass guitar', 'maracas': 'synthesizer'}

v= cycle('guitar', boxes)
# ('guitar', 'conga', 'maracas', 'synthesizer', 'trumpet')
# v= cycle('saxophone', boxes)
# ('saxophone', 'banjo', 'drum set')
# v= cycle('bass guitar', boxes)
# ('bass guitar', 'trombone')
# v= cycle('clarinet', boxes)
# Traceback (most recent call last):
# AssertionError: invalid item

v= longest_cycle(boxes)
# 5

# v= read_boxes('boxes02.txt')  # 2x same label
# Traceback (most recent call last):
# AssertionError: invalid boxes
# v= read_boxes('boxes03.txt')  # 2x same content
# Traceback (most recent call last):
# AssertionError: invalid boxes
# v= read_boxes('boxes04.txt')  # labels differ from contents
# Traceback (most recent call last):
# AssertionError: invalid boxes

print(v)