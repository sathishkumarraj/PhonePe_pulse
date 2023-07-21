from git.repo.base import Repo
import os
import json
import pandas as pd

# Clone the data

os.environ["GIT_PYTHON_REFRESH"] = "quiet"
Repo.clone_from("https://github.com/PhonePe/pulse.git", "D:\PhonePe_Pulse\Clone data")

# Phonepe data extraction

# def aggregated_transcation_state():
path1 = "D:/PhonePe_Pulse/Clone data/data/aggregated/transaction/country/india/state/"
agg_trans_list = os.listdir(path1)

columns1 = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [],
            'Transaction_amount': []}
for state in agg_trans_list:
    cur_state = path1 + state + "/"
    agg_year_list = os.listdir(cur_state)

    for year in agg_year_list:
        cur_year = cur_state + year + "/"
        agg_file_list = os.listdir(cur_year)

        for file in agg_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            A = json.load(data)

            try:

                for i in A['data']['transactionData']:
                    name = i['name']
                    count = i['paymentInstruments'][0]['count']
                    amount = i['paymentInstruments'][0]['amount']
                    columns1['Transaction_type'].append(name)
                    columns1['Transaction_count'].append(count)
                    columns1['Transaction_amount'].append(amount)
                    columns1['State'].append(state)
                    columns1['Year'].append(year)
                    columns1['Quarter'].append(int(file.strip('.json')))

            except Exception as e:
                print(f"Problem occured while extracting: {str(e)}")

aggr_trans_df = pd.DataFrame(columns1)



# def aggregated_user_state():

path2 = "D:/PhonePe_Pulse/Clone data/data/aggregated/user/country/india/state/"
agg_user_list = os.listdir(path2)

columns2 = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'Count': [],
            'Percentage': []}
for state in agg_user_list:
    cur_state = path2 + state + "/"
    agg_year_list = os.listdir(cur_state)

    for year in agg_year_list:
        cur_year = cur_state + year + "/"
        agg_file_list = os.listdir(cur_year)

        for file in agg_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            B = json.load(data)
            try:
                for i in B["data"]["usersByDevice"]:
                    brand_name = i["brand"]
                    counts = i["count"]
                    percents = i["percentage"]
                    columns2["Brands"].append(brand_name)
                    columns2["Count"].append(counts)
                    columns2["Percentage"].append(percents)
                    columns2["State"].append(state)
                    columns2["Year"].append(year)
                    columns2["Quarter"].append(int(file.strip('.json')))

            except Exception as e:
                pass

aggr_usr_df = pd.DataFrame(columns2)



# def map_transcation_state():
path3 = "D:/PhonePe_Pulse/Clone data/data/map/transaction/hover/country/india/state/"
map_trans_list = os.listdir(path3)

columns3 = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Count': [],
            'Amount': []}

for state in map_trans_list:
    cur_state = path3 + state + "/"
    map_year_list = os.listdir(cur_state)

    for year in map_year_list:
        cur_year = cur_state + year + "/"
        map_file_list = os.listdir(cur_year)

        for file in map_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            C = json.load(data)

            try:

                for i in C["data"]["hoverDataList"]:
                    district = i["name"]
                    count = i["metric"][0]["count"]
                    amount = i["metric"][0]["amount"]
                    columns3["District"].append(district)
                    columns3["Count"].append(count)
                    columns3["Amount"].append(amount)
                    columns3['State'].append(state)
                    columns3['Year'].append(year)
                    columns3['Quarter'].append(int(file.strip('.json')))

            except Exception as e:
                pass

map_trans_df = pd.DataFrame(columns3)



# def map_user_state():
path4 = "D:/PhonePe_Pulse/Clone data/data/map/user/hover/country/india/state/"
map_user_list = os.listdir(path4)

columns4 = {"State": [], "Year": [], "Quarter": [], "District": [],
            "RegisteredUser": [], "AppOpens": []}

for state in map_user_list:
    cur_state = path4 + state + "/"
    map_year_list = os.listdir(cur_state)

    for year in map_year_list:
        cur_year = cur_state + year + "/"
        map_file_list = os.listdir(cur_year)

        for file in map_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            D = json.load(data)

            try:

                for i in D["data"]["hoverData"].items():
                    district = i[0]
                    registereduser = i[1]["registeredUsers"]
                    appOpens = i[1]['appOpens']
                    columns4["District"].append(district)
                    columns4["RegisteredUser"].append(registereduser)
                    columns4["AppOpens"].append(appOpens)
                    columns4['State'].append(state)
                    columns4['Year'].append(year)
                    columns4['Quarter'].append(int(file.strip('.json')))

            except Exception as e:
                pass

map_usr_df = pd.DataFrame(columns4)



# def top_transcation_state():
path5 = "D:/PhonePe_Pulse/Clone data/data/top/transaction/country/india/state/"

top_trans_list = os.listdir(path5)
columns5 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [], 'Transaction_count': [],
            'Transaction_amount': []}

for state in top_trans_list:
    cur_state = path5 + state + "/"
    top_year_list = os.listdir(cur_state)

    for year in top_year_list:
        cur_year = cur_state + year + "/"
        top_file_list = os.listdir(cur_year)

        for file in top_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            E = json.load(data)

            try:

                for i in E['data']['pincodes']:
                    name = i['entityName']
                    count = i['metric']['count']
                    amount = i['metric']['amount']
                    columns5['Pincode'].append(name)
                    columns5['Transaction_count'].append(count)
                    columns5['Transaction_amount'].append(amount)
                    columns5['State'].append(state)
                    columns5['Year'].append(year)
                    columns5['Quarter'].append(int(file.strip('.json')))

            except Exception as e:
                pass

top_trans_df = pd.DataFrame(columns5)



# def top_user_state():
path6 = "D:/PhonePe_Pulse/Clone data/data/top/user/country/india/state/"
top_user_list = os.listdir(path6)
columns6 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [],
            'RegisteredUsers': []}

for state in top_user_list:
    cur_state = path6 + state + "/"
    top_year_list = os.listdir(cur_state)

    for year in top_year_list:
        cur_year = cur_state + year + "/"
        top_file_list = os.listdir(cur_year)

        for file in top_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            F = json.load(data)

            try:

                for i in F['data']['pincodes']:
                    name = i['name']
                    registeredUsers = i['registeredUsers']
                    columns6['Pincode'].append(name)
                    columns6['RegisteredUsers'].append(registeredUsers)
                    columns6['State'].append(state)
                    columns6['Year'].append(year)
                    columns6['Quarter'].append(int(file.strip('.json')))

            except Exception as e:
                pass

top_user_df = pd.DataFrame(columns6)


# # def top_transcation_state_pincode():
# top_trans_st_path = r"D:\PhonePe_Pulse\Clone data\data\top\transaction\country\india\state"
# top_trans_st_dir = os.listdir(top_trans_st_path)
#
# top_trans_pin_dict = {
#         'state': [],
#         'pincode': [],
#         'year': [],
#         'quater': [],
#         'total_transcation_count': [],
#         'total_transcation_amount': []
#     }
#
# for state in top_trans_st_dir:
#         state_path = f"{top_trans_st_path}\\{state}\\"
#         state_years = os.listdir(state_path)
#         for year in state_years:
#             state_year_path = f"{state_path}{year}\\"
#             json_files = os.listdir(state_year_path)
#             for json_file in json_files:
#                 json_file_path = state_year_path + json_file
#                 read_json = open(json_file_path, 'r')
#                 load_json = json.load(read_json)
#
#                 try:
#                     pincodes = load_json['data']['pincodes']
#
#                     for data in pincodes:
#                         pincode = data['entityName']
#                         count = data['metric']['count']
#                         amount = data['metric']['amount']
#                         top_trans_pin_dict['pincode'].append(pincode)
#                         top_trans_pin_dict['total_transcation_count'].append(count)
#                         top_trans_pin_dict['total_transcation_amount'].append(amount)
#                         top_trans_pin_dict['state'].append(state
#                                                            .replace('-', ' '))
#                         top_trans_pin_dict['year'].append(year)
#                         top_trans_pin_dict['quater'].append('q' + json_file.strip('.json'))
#
#                 except Exception as e:
#                     pass
#
# top_trans_pin_df = pd.DataFrame(top_trans_pin_dict)
#
#
#
# # def top_user_state_pincode():
# top_usr_st_path = r"D:\PhonePe_Pulse\Clone data\data\top\user\country\india\state"
# top_usr_st_dir = os.listdir(top_usr_st_path)
#
# top_usr_pin_dict = {
#         'state': [],
#         'pincode': [],
#         'year': [],
#         'quater': [],
#         'registered_user': []
#     }
#
# for state in top_usr_st_dir:
#         state_path = f"{top_usr_st_path}\\{state}\\"
#         state_years = os.listdir(state_path)
#         for year in state_years:
#             state_year_path = f"{state_path}{year}\\"
#             json_files = os.listdir(state_year_path)
#             for json_file in json_files:
#                 json_file_path = state_year_path + json_file
#                 read_json = open(json_file_path, 'r')
#                 load_json = json.load(read_json)
#
#                 try:
#                     pincodes = load_json['data']['pincodes']
#
#                     for data in pincodes:
#                         pincode = int(data['name'])
#                         registered_user = int(data['registeredUsers'])
#                         top_usr_pin_dict['pincode'].append(pincode)
#                         top_usr_pin_dict['registered_user'].append(registered_user)
#                         top_usr_pin_dict['state'].append(state.replace('-', ' '))
#                         top_usr_pin_dict['year'].append(int(year))
#                         top_usr_pin_dict['quater'].append('q' + json_file.strip('.json'))
#
#                 except Exception as e:
#                     pass
#
# top_usr_pin_df = pd.DataFrame(top_usr_pin_dict)



# conver to CSV file

def save_dataframe_as_csv(dataframe, folder_path, file_name):
    csv_file_path = os.path.join(folder_path, f"{file_name}.csv")
    dataframe.to_csv(csv_file_path, index=False)

def save_all_dataframes_as_csv():
    directory_path = r"D:\PhonePe_Pulse\CSV files"

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    folder_name = "phoenpe data csv files"
    folder_path = os.path.join(directory_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    save_dataframe_as_csv(aggr_trans_df, folder_path, "aggr_trans_df")
    save_dataframe_as_csv(aggr_usr_df, folder_path, "aggr_usr_df")
    save_dataframe_as_csv(map_trans_df, folder_path, "map_trans_df")
    save_dataframe_as_csv(map_usr_df, folder_path, "map_usr_df")
    save_dataframe_as_csv(top_trans_df, folder_path, "top_trans_df")
    save_dataframe_as_csv(top_user_df, folder_path, "top_user_df")
    # save_dataframe_as_csv(top_trans_pin_df, folder_path, "top_trans_pin_df")
    # save_dataframe_as_csv(top_usr_pin_df, folder_path, "top_usr_pin_df")


save_all_dataframes_as_csv()

