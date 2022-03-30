#백준 문제 긁어오기

from urllib.request import Request, urlopen
import bs4

# q_num=1000
q_num = input("문제번호는?")
# q_name=input("문제이름은?")
url = f"https://www.acmicpc.net/problem/{q_num}"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
source = urlopen(req).read()
source_bs4 = bs4.BeautifulSoup(source, "html.parser")

title = source_bs4.find('title').string
q_name = title.split(":")[-1].lstrip()
# print(title)
name = __file__.split("\\")[-1]
# folder=__file__[:-len(name)-1].split("\\")[-1]

path = __file__[:-len(name)] + f"beakjoon_{q_name}_{q_num}_tier.py"
# path=__file__[:-len(name)]+f"beakjoon__{q_num}_tier.py"
# print(path)

with open(path, "w", encoding="utf-8") as file:

    file.write("'''")
    file.write("\n")
    file.write(f"--url--\n")
    file.write(f"{url}\n")
    file.write("\n")
    file.write("--title--\n")
    file.write(f"{title}\n")
    file.write("\n")
    file.write("--problem_description--\n")
    text_0 = source_bs4.find('div', id="problem_description").find_all('p')
    print(text_0)
    for t in text_0:
        texts = t.string.split(". ")
        for text in texts:
            file.write(f"{text}\n")
    file.write("\n")

    file.write("--problem_input--\n")
    text_0 = source_bs4.find('div', id="problem_input").find_all('p')
    for t in text_0:
        texts = t.string.split(". ")
        for text in texts:
            file.write(f"{text}\n")
    file.write("\n")

    file.write("--problem_output--\n")
    text_0 = source_bs4.find('div', id="problem_output").find_all('p')
    for t in text_0:
        # print(t.string)
        if t.string is None:
            pass
        else:
            texts = t.string.split(". ")
            for text in texts:
                file.write(f"{text}\n")
    file.write("\n")
    file.write("'''")
