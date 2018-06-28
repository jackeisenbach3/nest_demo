from base_page import Base_Page
import locators


class Product_Object:
    "Page Object for the table"
    
    #locators

    def get_all_text(self):
        "Get the text within the table"
        table_text = []
        row_doms = self.get_elements(self.rows_xpath)
        for index,row_dom in enumerate(row_doms):
            row_text = []
            cell_doms = self.get_elements(self.cols_relative_xpath%(index+1))
            for cell_dom in cell_doms:
                row_text.append(self.get_dom_text(cell_dom))
            table_text.append(row_text)

        return table_text

    
    def get_num_rows(self):
        "Get the total number of rows in the table"
        #NOTE: We do not count the header row
        row_doms = self.get_elements(self.rows_xpath)

        return len(row_doms)


    def get_num_cols(self):
        "Return the number of columns"
        #NOTE: We just count the columns in the header row
        col_doms = self.get_elements(self.cols_header)

        return len(col_doms)


    def get_column_text(self,column_name):
        "Get the text within a column"
        pass

    def get_column_names(self):
        "Return a list with the column names"
        column_names = []
        col_doms = self.get_elements(self.cols_header)
        for col_dom in col_doms:
            column_names.append(self.get_dom_text(col_dom))

        return column_names


    def check_cell_text_present(self,text,column_name='all'):
        "Check if the text you want is present in a cell"
        result_flag = False
        if column_name == 'all':
            table_text = self.get_all_text()
        else:
            table_text = [self.get_column_text(column_name)]
        for row in table_text:
            for col in row:
                if col == text:
                    result_flag = True
                    break
            if result_flag is True:
                break

        return result_flag

    
    def check_name_present(self,name):
        "Check if the supplied name is present anywhere in the table"
        return self.check_cell_text_present(name,column_name='name')


    def print_table_text(self):
        "Print out the table text neatly"
        column_names = self.get_column_names()
        table_text = self.get_all_text()

        self.write('||'.join(column_names))
        for row in table_text:
            self.write('|'.join(row))
