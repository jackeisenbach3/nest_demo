from base_page import Base_Page
from signin_object import Signin_Object
from header_object import Header_Object
from product_object import Product_Object
from blog_object import Blog_Object
from footer_object import Footer_Object

class Main_Page(Base_Page, 
                Header_Object, 
                Signin_Object, 
                Product_Object, 
                Blog_Object, 
                Footer_Object):
    "Page object for the Main page"
 
    def start(self):
        print "going to start now ..."
        '''
        self.url = ""
        self.open(self.url)
        '''

