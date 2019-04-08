import pandas as pd

class DataManager:
    data_dir = None

    def __init__(self, data_dir="./"):
        self.data_dir = data_dir

    # private method
    def create_tables(self):
        import pickle

        # platform_info
        table_name = "PLATFORM_INFO"
        with open(self.data_dir + table_name, "wb") as table_fp:
            header = ["PLATFORM_INFO_ID", "PLATFORM_NAME", "PLATFORM_URL", "PLATFORM_DESCRIPTION", "REG_DATE",
                      "UPDATE_DATE"]
            table = []
            table.append(header)
            pickle.dump(table, table_fp)

        # platform_dic
        table_name = "PLATFORM_DIC"
        with open(self.data_dir + table_name, "wb") as table_fp:
            header = ["PLATFORM_DIC_ID", "PLATFORM_INFO_ID", "PLATFORM_SIMILAR"]
            table = []
            table.append(header)
            pickle.dump(table, table_fp)

        # brand_info
        table_name = "BRAND_INFO"
        with open(self.data_dir + table_name, "wb") as table_fp:
            header = ["BRAND_INFO_ID", "PLATFORM_INFO_ID", "BRAND_NAME", "BRAND_URL", "BRAND_DESCRIPTION", "REG_DATE",
                      "UPDATE_DATE"]
            table = []
            table.append(header)
            pickle.dump(table, table_fp)

        # brand_dic
        table_name = "BRAND_DIC"
        with open(self.data_dir + table_name, "wb") as table_fp:
            header = ["BRAND_DIC_ID", "BRAND_INFO_ID", "BRAND_SIMILAR"]
            table = []
            table.append(header)
            pickle.dump(table, table_fp)

    def get_primary_key(self, table_name):
        df = self.select_all_from_table(table_name)
        id_column = table_name.upper() + "_ID"
        primary_key = None
        if len(df) < 1:
            primary_key = str(1)
        else:
            current_latest_pk = df[len(df) - 1:len(df)][id_column]
            primary_key = str(int(current_latest_pk) + 1)
        return primary_key

    def get_id_with_column(self, table_name, column_name, column_value):
        df = self.select_all_from_table(table_name)
        id_column = table_name.upper() + "_ID"
        id_value = str(int(df[df[column_name] == column_value][id_column]))
        return id_value

    def select_all_from_table(self, table_name, df=True):
        import pickle
        import os

        table = None
        if os.path.isfile(self.data_dir + table_name):
            with open(self.data_dir + table_name, "rb") as table_fp:
                table = pickle.load(table_fp)
        else:
            table = []
            statement = "Table {table_name} has not been created".format(table_name=table_name)
            print(statement)

        if df:
            df = pd.DataFrame(table[1:], columns=table[0])
            return df
        else:
            return table

    def insert_platform_info(self, platform_info_instance):
        # TODO : DB write가 될 때까지 txt로 대체
        import datetime
        import pickle
        import os

        table_name = "PLATFORM_INFO"
        current_time = datetime.datetime.now().__str__()
        table = self.select_all_from_table(table_name, df=False)
        platform_info_id = self.get_primary_key(table_name)

        with open(self.data_dir + table_name, "wb") as table_fp:
            platform_name = platform_info_instance["platform_name"]
            platform_url = platform_info_instance["platform_url"]
            platform_description = platform_info_instance["platform_description"]
            reg_date = current_time
            update_date = current_time
            row = [platform_info_id, platform_name, platform_url, platform_description, reg_date, update_date]

            if row in table:
                statement = "Duplicated Row exists"
                print(statement)
            else:
                table.append(row)

            pickle.dump(table, table_fp)

        statement = "Row Inserted into {table_name};\n\t{row}".format(table_name=table_name, row=row)
        print(statement)

    def insert_platform_dic(self, platform_dic_instance):
        # TODO : DB write가 될 때까지 txt로 대체
        import datetime
        import pickle
        import os

        table_name = "PLATFORM_DIC"
        current_time = datetime.datetime.now().__str__()
        table = self.select_all_from_table(table_name, df=False)
        platform_dic_id = self.get_primary_key(table_name)

        with open(self.data_dir + table_name, "wb") as table_fp:
            platform_info_id = platform_dic_instance["platform_info_id"]
            platform_similar = platform_dic_instance["platform_similar"]
            row = [platform_dic_id, platform_info_id, platform_similar]

            if row in table:
                statement = "Duplicated Row exists"
                print(statement)
            else:
                table.append(row)

            pickle.dump(table, table_fp)

        statement = "Row Inserted into {table_name};\n\t{row}".format(table_name=table_name, row=row)
        print(statement)

    def insert_brand_info(self, brand_info_instance):
        # TODO : DB write가 될 때까지 txt로 대체
        import datetime
        import pickle
        import os

        table_name = "BRAND_INFO"
        current_time = datetime.datetime.now().__str__()
        table = self.select_all_from_table(table_name, df=False)
        brand_info_id = self.get_primary_key(table_name)

        with open(self.data_dir + table_name, "wb") as table_fp:
            platform_info_id = brand_info_instance["platform_info_id"]
            brand_name = brand_info_instance["brand_name"]
            brand_url = brand_info_instance["brand_url"]
            brand_description = brand_info_instance["brand_description"]
            reg_date = current_time
            update_date = current_time
            row = [brand_info_id, platform_info_id, brand_name, brand_url, brand_description, reg_date, update_date]

            if row in table:
                statement = "Duplicated Row exists"
                print(statement)
            else:
                table.append(row)

            pickle.dump(table, table_fp)

        statement = "Row Inserted into {table_name};\n\t{row}".format(table_name=table_name, row=row)
        print(statement)

    def insert_brand_dic(self, brand_dic_instance):
        # TODO : DB write가 될 때까지 txt로 대체
        import datetime
        import pickle
        import os

        table_name = "BRAND_DIC"
        current_time = datetime.datetime.now().__str__()
        table = self.select_all_from_table(table_name, df=False)
        brand_dic_id = self.get_primary_key(table_name)

        with open(self.data_dir + table_name, "wb") as table_fp:
            brand_info_id = brand_dic_instance["brand_info_id"]
            brand_similar = brand_dic_instance["brand_similar"]
            row = [brand_dic_id, brand_info_id, brand_similar]

            if row in table:
                statement = "Duplicated Row exists"
                print(statement)
            else:
                table.append(row)

            pickle.dump(table, table_fp)

        statement = "Row Inserted into {table_name};\n\t{row}".format(table_name=table_name, row=row)
        print(statement)