from .GlobalValues  import *
from .AddressSpace  import AddressSpace


class RegSpace(AddressSpace):

    def __init__(self,name,size,description='',path='./',bus_width=APG_BUS_WIDTH):
        super().__init__(name=name,size=size,description=description,path=path)
        self.bus_width = bus_width
        #self._name_prefix = 'reg'



    #########################################################################################
    # output generate
    #########################################################################################

    def report_html(self):
        text = self.report_from_template(APG_HTML_FILE_REG_SPACE)
        with open(self.html_path,'w') as f:
            f.write(text)
        for ss in self.sub_space_list:
            ss.report_html()

    def report_chead_core(self):
        chead_name_list = [self.chead_name]
        text = self.report_from_template(APG_CHEAD_FILE_REG_SPACE)
        with open(self.chead_path,'w') as f:
            f.write(text)
        for ss in self.sub_space_list:
            chead_name_list += ss.report_chead_core()
        return chead_name_list

    def report_vhead_core(self):
        vhead_name_list = [self.vhead_name]
        text = self.report_from_template(APG_VHEAD_FILE_REG_SPACE)
        with open(self.vhead_path,'w') as f:
            f.write(text)
        for ss in self.sub_space_list:
            vhead_name_list += ss.report_vhead_core()
        return vhead_name_list