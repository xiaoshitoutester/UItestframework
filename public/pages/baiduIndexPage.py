#coding=utf-8

from public.common import basepage

class BaiduIndexPage(basepage.Page):

    def into_baidu_page(self):
        """打开百度首页"""
        self.dr.open('http://www.baidu.com')
    def input_search_key(self,values):
        """输入搜索关键词"""
        self.dr.clear_type('id->kw',values)

    def click_search_button(self):
        """点击搜索按钮"""
        self.dr.click('id->su')

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()