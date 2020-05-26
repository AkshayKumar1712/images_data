import os
import glob
import shutil
import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs
import urllib.request
import json

def download_and_store(url,image_number,faulty_links,non_porn,folder_name):
    if not non_porn:
        images_folder=os.path.join(os.getcwd(),folder_name)

        if not (os.path.exists(images_folder)):
            os.mkdir(images_folder)
        try:
            urllib.request.urlretrieve(url,os.path.join(images_folder,str(image_number)+".jpg"))
        except Exception as e:
            faulty_links.append(url+": "+str(e))
    else:
        images_folder=os.path.join(os.getcwd(),"images_crawled/non_porn")
        if not (os.path.exists(images_folder)):
            os.mkdir(images_folder)
        try:
            urllib.request.urlretrieve(url,os.path.join(images_folder,str(image_number)+".jpg"))
        except Exception as e:
            faulty_links.append(url+": "+str(e))

def open_url_files(limit):
    all_folders=os.listdir("raw_data")
    faulty_links=[]
    current_image_number=1
    for folder in all_folders:
        current_file="raw_data/"+folder+"/urls_"+folder
        count=limit
        try:
            urls_text_file=open(current_file+".txt","r+")
            mixed_file=open("mixed_cateogory_links.txt","a+")
            mixed_file.write("Category: "+current_file)
            while count>0:
                print(str(count)+""+current_file)
                url=urls_text_file.readline()
                mixed_file.write(url)
                # download_and_store(url,current_image_number,faulty_links,False,datetime.today().strftime('%Y-%m-%d'))
                # print("Downloading image no "+str(current_image_number)+" from "+ url)
                count-=1
                # current_image_number+=1
            urls_text_file.close()
        except Exception as e:
            limit+=1
            faulty_links.append(folder+" "+str(e))
            print(e)
    # print("Number of faulty links: "+str(len(faulty_links)))    
    for link in faulty_links:
        faulty_logs_file=open("images_crawled"+"/faulty_links.txt","a+")
        faulty_logs_file.write(link+"\n")

def download_from_root_with_file(file,limit):
    current_number=1000
    try:
        urls_text_file=open(file,"r+")
        current_image_number=1
        # name=1
        name=433

        faulty_links=[]
        url=urls_text_file.readlines()
        for i in range(0,limit):
            download_and_store(url[current_number+i],name,faulty_links,False,"images")
            print("Downloading image no "+str(name)+" from "+ url[current_number+i])
            current_image_number+=1
            name+=1
        urls_text_file.close()
    except Exception as e:
        faulty_links.append(str(e))
        print(str(e))

def readFile():
    try:
        mixed_file=open("mixed_cateogory_links_l.txt","r")
        urls=mixed_file.readlines()
        new_file=open("final_for_db.txt","a+")
        for url in urls:
            print(url)
            if not url.startswith("Category: "):
                new_file.write(url)

    except Exception as e:
        pass
def main():
    # open_url_files(100)
    # readFile()
    # open_url_files(int(input("Enter Number of Images ")))
    download_from_root_with_file("m_genitalia_penis_l.txt",int(input("Enter Number of Images ")))
if __name__ == "__main__":
    main()