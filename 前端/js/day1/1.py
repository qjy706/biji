text1='asdsadasdsadsadasdasdsa dsadasda\nasdas dasdsadsadsa\nasdasdsadsadsasadsadaadasa\nwqeasdasdzxcsadafdfsg\nasdasdqwesafdasfq\nasdasdasewqrqwrwqerqwasdfsa\nasfdsafsafsafdsafasfwqrzfasdrfweqhyter'
text2='asdsadsadsa dsaxzcsafwtertrhd\nwa safsfdsfgfdsgdsfgfdsgdsgds\nasfsafafkjhljlhjhfsadfqwrfsf\nfsdafsadfsadfsadfwqrsfasfwdcsg'
L=[]
list1=text1.splitlines()
list2=text2.splitlines()
word1=[column for column in list1 if column and column.isspace()]
word2=[column for column in list2 if column and column.isspace()]
len1 = len(word1)
len2 = len(word2)
for step in range(max(len1,len2)):
    if step < len1 and step < len2:
        col1 = word1[step].split()
        col2 = word2[step].split()
        if col1 != col2:
            return 