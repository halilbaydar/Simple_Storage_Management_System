from disk_manager import disk_manager
import re
class file_manager:
    file_name=""
    page_content=[]
    page_number=0

    def __init__(self,file_name):
        self.file_name=file_name

    def to_find_proper_page(self):
        disk=disk_manager(1,self.file_name)
        page=[]
        page=disk.to_get_page()
        while True:
            if page==[]:
                disk.to_create_new_page()
                return ['0\n','\n',disk.page_number]
            size=int(re.findall("\d*",page[0])[0])
            if size<19:
                page.append(disk.page_number)
                return page
            else:
                disk=disk_manager(disk.page_number+1,self.file_name)
                page=disk.to_get_page()

    def to_find_wanted_page(self,page_number):
        self.page_number=page_number
        disk=disk_manager(self.page_number,self.file_name)
        return disk.to_get_page()

    def to_delete_record(self,page_number):
        self.page_number=page_number
        disk=disk_manager(self.page_number,self.file_name)
        page=[]
        page=disk.to_get_page()
        return page

    def to_write_into_file_in_proper_page(self,page_content,page_number):
        self.page_content=page_content
        self.page_number=page_number
        disk=disk_manager(page_number,self.file_name)
        disk.to_write_into_page(self.page_content)

    def delete_Type(self):
        disk=disk_manager(1,self.file_name)
        disk.delete_type()
