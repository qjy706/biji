name=[['sada','dsadaszxc','adazx'],['zxczq','asdadz','asdaqqeq']]

L=[]
for i in name:
    for x in i:
        if x.count('a') >= 2:
            L.append(x)
print(L)



l=[x for i in name for x in i if x.count('a') >= 2]
print(l)