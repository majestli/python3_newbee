import  io

f=io.open("abc.txt","wt",encoding="utf-8")

f.write(u"i magine non-english language here")

f.close()

#text = io.open("abc.txt",encoding="utf-8").read()
fr=io.open("abc.txt",encoding="utf-8")
text= fr.read()
print(text)
