import csv
import mysql.connector
import sys
import os
import setting

# Mysqlへの接続情報
connect = mysql.connector.connect(
  user=setting.mysql_info["user"],
  password=setting.mysql_info["password"],
  host=setting.mysql_info["host"],
  port=setting.mysql_info["port"],
  database=setting.mysql_info["database"],
  charset='utf8'
)
cursor = connect.cursor()

def to_data(v):
  if v.lower() in ("yes", "true"):
    return '1'
  elif v.lower() in ("no", "false"):
    return '0'
  elif v.startswith('\'') or v.startswith('"'):
    return v
  else:
    return '\'{}\''.format(v)

if (setting.tables):
  for table in setting.tables.keys():
    isExist = os.path.exists(setting.output_dir)
    if not isExist:
      os.makedirs(setting.output_dir)
    print("---------------------------------------------------------------------------------")
    print("table: ", table)
    print("csv_file: ", setting.tables[table]["csv_file"])
    with open(setting.tables[table]["csv_file"],'r',encoding="utf-8") as infile, \
      open(setting.output_dir + "/" + table + '.sql', 'w', encoding='utf-8') as sql_file:
      reader = csv.DictReader(infile)
      for row in reader:
        #print(dict(row).values())
        #print("cols: ", cols)
        mapping_cols = setting.tables[table]["mapping"].keys()
        #print("mapping_cols: ", mapping_cols)
        mapping_cols_csv = setting.tables[table]["mapping"].values()
        #print("mapping_cols_csv: ", mapping_cols_csv)
        cols = list(dict(row).values())
        #print(len(cols))
        insert_data = [to_data(cols[i-1].strip()) for i in mapping_cols_csv]
        #print("insert_data: ", insert_data)
        sql_insert = 'INSERT INTO ' + table + ' (' + ','.join(mapping_cols) + ') values(' + ','.join(insert_data) + ');'
        if setting.import_type["import_data"]:
          try:
            cursor.execute(sql_insert)
          except Exception as e:
            print(sql_insert)
            print(e)


        if setting.import_type["sql_generate"]:
          print(sql_insert, file=sql_file)
'''

      lines = infile.read().splitlines()

      count = 0
      for line in lines:
        cols = line.split(',')
        #print("cols: ", cols)
        if count > 0:
          #print("cols: ", cols)
          mapping_cols = setting.tables[table]["mapping"].keys()
          #print("mapping_cols: ", mapping_cols)
          mapping_cols_csv = setting.tables[table]["mapping"].values()
          #print("mapping_cols_csv: ", mapping_cols_csv)
          insert_data = ['\'{}\''.format(cols[i-1]) for i in mapping_cols_csv]
          #print("insert_data: ", insert_data)
          sql_insert = 'INSERT INTO ' + table + ' (' + ','.join(mapping_cols) + ') values(' + ','.join(insert_data) + ');'
          if setting.import_type["import_data"]:
            try:
              cursor.execute(sql_insert)
            except:
              print(sql_insert)
              print('Error')
            

          if setting.import_type["sql_generate"]:
            print(sql_insert, file=sql_file)

        count = count + 1
'''
# DB操作の終了。
cursor.close()
# insert処置後のcommitも。
connect.commit()
connect.close()
