#!/usr/bin/env python
# tary, 14:49 2018/10/18

import os
import oss2
import time
import sys


bucket_name = sys.argv[1]


class log_uploader():
    def __init__(self):
        self.access_key_id = "xxx"
        self.access_key_secret = "xxx"
        self.bucket_name = bucket_name
        self.endpoint = "oss-cn-hangzhou.aliyuncs.com"
        self.auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        self.bucket = oss2.Bucket(self.auth, self.endpoint, self.bucket_name)

        
        
    def uploadfile(self,logfileName, filePath):
        realfilepath = logfileName
        print(realfilepath)
        try:
            oss2.resumable_upload(self.bucket, logfileName, filePath)
            time.sleep(0.1)

            file_exist_check = self.bucket.object_exists(logfileName)
#            print file_exist_check
            if file_exist_check != True:
                return False
        except Exception as e:
            print(e)
            return False

        return True  
    

    def downloadfile(self,need_file_prex):
        try:
            for object_info in oss2.ObjectIterator(self.bucket,need_file_prex):
                print(object_info.key)
                self.bucket.get_object_to_file(object_info.key, object_info.key) 
        except:
            print ("Error")

    
    def deletefile(self,need_file_prex):
        for obj in oss2.ObjectIterator(self.bucket, prefix="4016"):
        
            print (obj.key)
            self.bucket.delete_object(obj.key)        
    
    def download_delete(self,need_file_prex):
        try:
            for object_info in oss2.ObjectIterator(self.bucket,need_file_prex):
                print(object_info.key)
                self.bucket.get_object_to_file(object_info.key, object_info.key)
                self.bucket.delete_object(object_info.key) 
        except:
            print ("Error")
        
    
    def search(self,need_file_prex):
        try:
            for object_info in oss2.ObjectIterator(self.bucket,need_file_prex):
                print(object_info.key)
        except:
            print ("Error")
            s
    def copyfile(self):
        d_bucket = oss2.Bucket(self.auth, "oss-cn-hangzhou.aliyuncs.com", '102991313')
        for object_info in oss2.ObjectIterator(self.bucket,prefix="11399"):
            print(object_info.key)
            d_bucket.copy_object("mestestbak",object_info.key,object_info.key)
            

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} filename filepath")
        quit(1)
        
    uploader = log_uploader()
    
    # uploadfile
    if sys.argv[2] == "uploader":
        if sys.argv[3] != "" and sys.argv[4] != "":
            uploader.uploadfile(sys.argv[3],sys.argv[4])
            quit(0)
        else:
            quit(2)
    
    # search
    elif sys.argv[2] == "search":
        if sys.argv[3] != "" and sys.argv[4] == "0":
            uploader.search(sys.argv[3])
            quit(0)
        else:
            quit(2)
    
    # downloadfile
    elif sys.argv[2] == "downloadfile":
        if sys.argv[3] != "" and sys.argv[4] == "0":
            uploader.downloadfile(sys.argv[3])
            quit(0)
        else:
            quit(2)       
    else:     
        quit(2)
    
#    uploader.copyfile()
#    uploader.deletefile()    
#    uploader.downloadfile()
#    uploader.download_delete()
    
    