import os
import sys 


def changeHeaderWeb(folder):
        encode = "utf-8"
        
        for file in os.listdir(folder):
            if file == "index.html":
                folderName = folder.split("/")[-1]
                xOriginal = "X-Original-Url: https://"+folderName+"/"+'\r\n\r\n'
                f = open(folder + "/" + file,encoding=encode)
                try:
                    data= readlines()
                except:
                    f.close()
                    encode = "ISO-8859-1"
                    f = open(folder + "/" + file,encoding=encode)
                    data = f.readlines()
                docTypeIndex = 0
                header=""
                for i in range(len(data)):
                    if "X-Original-Url" in data[i]:
                        continue
                    if "Transfer-Encoding: chunked" in data[i]:
                        continue
                    if "Alternate-Protocol" in data[i]:
                        continue
                    if "DOCTYPE" in data[i].upper():
                        docTypeIndex = i
                        break
                    header+=data[i]
                contents = "".join(data[docTypeIndex:])
                header+=xOriginal
                contents = header+contents
                contents = contents.encode(encode)


                with open(folder+'/'+file , mode='wb') as fw:
                    fw.write(contents)
                f.close()



target_dir = os.sys.argv[1]

subfolders = [ f.path for f in os.scandir(target_dir) if f.is_dir() ]
print(subfolders)
for i in subfolders:
    if "www" in i:
        changeHeaderWeb(i)










