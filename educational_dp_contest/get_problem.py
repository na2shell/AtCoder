import urllib.request, json 
import gzip


headers = {"Accept-encoding":"gzip"}
r = urllib.request.Request("https://kenkoooo.com/atcoder/resources/problems.json",headers= headers)
r_tmp = urllib.request.urlopen(r)
res = gzip.GzipFile(fileobj=r_tmp)
text = json.loads(res.read().decode("utf-8"))

#print(text)
#print(text[3]["id"])
problems = []

for s in range(len(text)):
    if(text[s]["contest_id"] == "dp"):
        p = text[s]["title"]
        p1 = p.replace(" ","")
        p2 = p1.replace(".","-")
        print(p2+".py")

