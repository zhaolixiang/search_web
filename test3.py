with open('urls.txt') as f:
    x=[]
    for y in f.readlines():
        x.append(y.strip())
    print(x)
