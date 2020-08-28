import argparse
import os
import re
from file_manager import file_manager

parser=argparse.ArgumentParser()
parser.add_argument('args',nargs='*')
args=parser.parse_args()

def createtype():
    print("The name of type :",end=' ')
    thenameoftype=input()
    print("The number of fields :",end=' ')
    thenumberoffields=input()
    thenameoffields=[]
    thenameoffields.append(str(int(thenumberoffields)))
    for i in range(0,int(thenumberoffields)):
        print('The name of field',i,":",end=' ')
        x=input()
        thenameoffields.append({x})
    with open("system_catalog.txt","a+",encoding="utf-8") as systemcatalog:
        systemcatalog.write(thenameoftype)
        systemcatalog.write(' ')
        for x in thenameoffields:
            systemcatalog.write(' ')
            systemcatalog.write(str(x))
        systemcatalog.write('\n')
        systemcatalog.close()
    filename=thenameoftype+'.txt'
    with open(filename,'w+') as f:
        f.write('0')
    return

def deletetype():
    print("The name of type you want to delete :",end=" ")
    thenameoftype=input()
    systemcatalogread=open("system_catalog.txt","r")
    lines=systemcatalogread.readlines()
    systemcatalogread.close()
    systemcatalogread2=open("system_catalog.txt","w")

    for line in lines:
        if line.split(' ')[0]!=thenameoftype:
            systemcatalogread2.write(line)
        else:
            for root,directories,files in os.walk('./'):
                for file in files:
                    if file.split('.')[0]==thenameoftype:
                        os.remove(file)
                break
    systemcatalogread2.close()
    return

def listalltypes():
    alltypes=open("system_catalog.txt",encoding="utf-8")
    for line in alltypes.readlines():
        print(line)

def createrecord():
    print("The name of type :",end=' ')
    thenameoftype=input()
    print("The key of record :",end=' ')
    keyofrecord=input()
    thesystemcatalog=open("system_catalog.txt",encoding="utf-8")
    lines=thesystemcatalog.readlines()
    fieldvalues=[]
    filename=thenameoftype+'.txt'
    for line in lines:
        tt=line.split(' ')
        if tt[0]==thenameoftype:
                fieldsize=int(tt[2])
                pageheader=re.findall("\d*",tt[len(tt)-1])
                for i in re.findall(".*?{(.*?)}",line):
                     if i!='\n':
                            print(i,':',end='')
                            temp=input()
                            fieldvalues.append(str(temp))
    instanceofrecord=""
    instanceofrecord=instanceofrecord+keyofrecord
    for i in fieldvalues:
        instanceofrecord=instanceofrecord+' ' + str({i})
    instanceofrecord=instanceofrecord+'\n'
    myfile=file_manager(filename)
    temp=myfile.to_find_proper_page()
    pagenumer=temp.pop()
    page=temp
    page[0]=int(page[0])+1
    a=""
    a=str(page[0])+'\n'
    page[0]=a
    for i in range(0,len(page)):
        if page[i]=='\n':
             page[i]=instanceofrecord
             break
        elif i==len(page)-1:
            page.append(instanceofrecord)
    myfile.to_write_into_file_in_proper_page(page,pagenumer)

def deleterecord():
    print("The name of type :",end=' ')
    thenameoftype=input()
    print("The key of record :",end=' ')
    keyofrecord=input()
    filename=thenameoftype+'.txt'
    aa=1
    run=True
    while run:
        filem=file_manager(filename)
        page=[]
        page=filem.to_delete_record(aa)
        for i in range(1,len(page)):
            if  page[i].split(' ')[0]==keyofrecord:
                page[0]=str(int(re.findall("\d*",page[0])[0])-1)+'\n'
                page[i]='\n'
                filem.to_write_into_file_in_proper_page(page,aa)
                run=False
                break
        aa=aa+1
def searchrecord():
    print("The name of type :",end=' ')
    thenameoftype=input()
    print("The key of record :",end=' ')
    keyofrecord=input()
    filename=thenameoftype+'.txt'
    number=1
    aa=True
    while aa:
        filem=file_manager(filename)
        page=[]
        page=filem.to_find_wanted_page(number)
        if len(page)==0:
            print("Not Found")
        for line in page:
            if line.split(' ')[0]==keyofrecord:
                print('Primary key',end=' ')
                d=open('system_catalog.txt','r',encoding='utf-8').readlines()
                for k in d:
                    if k.split(' ')[0]==thenameoftype:
                        for p in re.findall(".*?{(.*?)}",k):
                            print(p,end=' ')
                        print('\n')
                        print(line.split(' ')[0],end=' ')
                        for p in re.findall(".*?{(.*?)}",line):
                            print(p,end=' ')
                aa=False
                break
        number=number+1
def listrecord():
    print("The name of type :",end=' ')
    thenameoftype=input()
    filename=thenameoftype+'.txt'
    aa=True
    number=1
    print('Primary key',end=' ')
    d=open('system_catalog.txt','r',encoding='utf-8').readlines()
    for k in d:
            if k.split(' ')[0]==thenameoftype:
                for p in re.findall(".*?{(.*?)}",k):
                    print(p,end=' ')
                print('\n')
    while aa:
        filem=file_manager(filename)
        page=[]
        page=filem.to_find_wanted_page(number)
        if len(page)==0:
            aa=False
        else:
            for m in range(1,len(page)):
                    rr=page[m].split(' ')[0]
                    if rr!='\n':
                        print(rr,end=' ')
                    for p in re.findall(".*?{(.*?)}",page[m]):
                        print(p,end=' ')
                    if rr!='\n':
                        print('\n')

        number=number+1
def main():
    if args.args[0]=="new type":
        createtype()
    elif args.args[0]=="delete type":
        deletetype()
    elif args.args[0]=="list all types":
        listalltypes()
    elif args.args[0]=="create record":
        createrecord()
    elif args.args[0]=="delete record":
        deleterecord()
    elif args.args[0]=="search record":
        searchrecord()
    elif args.args[0]=="list all record":
        listrecord()
    else:
        print("please enter what you do ")
if __name__ == "__main__":
    main()