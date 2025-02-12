import zipfile
import os

class ZipFileManager:
    def __init__(self, zip_path, extracted_to = "extracted"):
        self.zip_path = zip_path
        self.extracted_to = extracted_to
        self.store_count = dict()
        self.extracted_files =[]
        
    def unzip_and_count(self):
        if not zipfile.is_zipfile(self.zip_path):
            print("Error: The file is not in a Valid ZIP format")
            return 
        os.makedirs(self.extracted_to, exist_ok=True)
        
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.extracted_to)
            self.extracted_files = zip_ref.namelist()
        print("File Extracted Successfully")
            
        for file in self.extracted_files:
            extension = os.path.splitext(file)[1]
            if extension  in self.store_count.keys():
                self.store_count[extension]+=1
            else:
                self.store_count[extension]=1
        for key,value in self.store_count.items():
            print(f"{key} : {value}")
            
    def choose_format(self,file_format):
        matching_files =[os.path.join(self.extracted_to,file) for file in self.extracted_files if file.endswith(file_format)]
        if not matching_files:
            print("No file fount for this format")
            return [] 
        return matching_files