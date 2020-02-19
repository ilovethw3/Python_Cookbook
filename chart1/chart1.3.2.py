from collections import deque
def search(lines,pattern,history=5):
    previous_lines=deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

with open('somefile.txt') as f:
    for line,previlnes in search(f,'python',5):
        for pline in previlnes:
            print(pline,end='')
        print(line,end='')
        print('-'*20)