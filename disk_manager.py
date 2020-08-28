import re
import os

class disk_manager:
    page_size=19
    file_name=""
    page_number=0

    def __init__(self,page_number,file_name):
        self.file_name=file_name
        self.page_number=page_number

    def to_write_into_page(self,page_content):
        f=open(self.file_name,'r',encoding='utf-8')
        temp_file=open("temp.txt","a+",encoding='utf-8')
        for i in range(0,(self.page_number-1)*self.page_size+(self.page_number-1)):
            temp_file.write(f.readline())
        for j in page_content:
            temp_file.write(str(j))
            f.readline()
        while True:
            line=f.readline()
            if line=="":
                break
            else:
                temp_file.write(line)
        for root,directories,files in os .walk('./'):
            run=False
            for file in files:
                if file==self.file_name:
                    f.close()
                    os.remove(file)
                    temp_file.close()
                    os.rename("./temp.txt",self.file_name)
                    run=True
                    break
            if run:
                break
    def to_get_page(self):
        f=open(self.file_name,'r',encoding="utf-8")
        for m in range(0,self.page_number-1):
            line=f.readline()
            if line=='\n':
                 while line=='\n':
                    line=f.readline()
            size_temp=int(re.findall("\d*",line)[0])
            for k in range(0,size_temp):
                line=f.readline()
                if line=='\n':
                    while line=='\n':
                        line=f.readline()
        page=[]
        ss=f.readline()
        if ss=='\n':
            while ss=='\n':
                ss=f.readline()
        elif ss=="":
            return []
        size_temp=int(re.findall("\d*",ss)[0])
        page.append(str(size_temp))
        while size_temp>0:
            uu=f.readline()
            if uu!='\n' and uu!="":
                size_temp=size_temp-1
            page.append(uu)
        if len(page)==1:
            page.append('\n')
        return page
    def to_create_new_page(self):
        f=open(self.file_name,"a+",encoding='utf-8')
        f.write('0')
        f.write("\n")