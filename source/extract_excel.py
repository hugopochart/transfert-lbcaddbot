import pandas as pd
from datetime import datetime, timedelta
import re

# use to have the departement in function of (city + code_postal)
def code_pos(code_pos):
    return re.findall('\d+', code_pos)[0][0:2]

# use to put the code_postal at the end of the title
def code_post_for_ad(title, code_pos):
    code_pos = re.findall('\d+', code_pos)[0][0:2]
    # title = title[:-1]
    title += " " + code_pos
    return title

def ads_from_excel():
    file = 'Tracktor - LBC - Publication Annonces.xlsx'
    xl = pd.ExcelFile(file)

    df = xl.parse('bot')
    df0 = df.loc[:, 'titre annonce']
    df1 = df.loc[:, 'Descriptions annonces']
    df2 = df.loc[:, 'Prix']
    df3 = df.loc[:, 'Localité']

    f3 = df3[0].split(',')
    size = df0.size
    dfads = []
    for x in range(0, size):
        f3 = df3[x].split(',')
        size_f3 = len(f3)
        for y in range(0, size_f3):
            dfend = [code_post_for_ad(df0[x], f3[y]), df1[x], df2[x], define_city_by_date(str(f3[y]))]
            dfads.append(dfend)
    # print(dfads)
    return dfads

# generate a hash by code_postal as key and cities as values
def generate_city_hash():
    file = 'Tracktor - LBC - Publication Annonces.xlsx'
    xl = pd.ExcelFile(file)
    df = xl.parse('villes_dpt_bot')
    df0 = df.loc[:, 'Departement']
    df1 = df.loc[:, 'ville']
    df2 = df.loc[:, 'date']
    hash_created = {}
    size = df0.size
    for x in range(0, size):
        if df0[x] in hash_created:
            hash_created[df0[x]].append([df2[x], df1[x]])
        else:
            hash_created[df0[x]] = []
            hash_created[df0[x]].append([df2[x], df1[x]])
    return hash_created

# return the city in function of postal_code and current_date
def define_city_by_date(code_postal):
    code_pos1 = code_pos(code_postal)
    hash_city = generate_city_hash()
    size = len(hash_city[int(code_pos1)])
    for x in range(0, size):
        current_city = hash_city[int(code_pos1)][x]
        if ((datetime.now() >= current_city[0]) and (datetime.now() <= (current_city[0]) +  timedelta(days=15))):
            return current_city[1]
    return hash_city[int(code_pos1)][0][1]
