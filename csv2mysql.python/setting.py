tables = {
  "user": {
     "csv_file": "data\company.csv",
     "mapping": {
       "username" : 1,
       "name" : 2,
       "email": 3,
       "password":4,
       "address":5,
       "tel":6,
     }
  }
}



import_type = {
  "sql_generate": True,
  "import_data": True
}

output_dir = "out"

mysql_info = {
  "user": "root",
  "password":"root",
  "host": "localhost",
  "port": 3306,
  "database": "todays_medicine_for_web_v2"
}