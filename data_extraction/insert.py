import MySQLdb

db = MySQLdb.connect("localhost","root","","tt" )
cursor = db.cursor()

sql1 = 'CREATE DATABASE bot_db'
cursor.execute(sql1)

sql1 = 'CREATE TABLE `bot_db`.`tt` ( `Day` VARCHAR(40) NOT NULL , `Vehicle` VARCHAR(40) NOT NULL , `Mandi_South` TIME NOT NULL , `South_North` TIME NOT NULL , `North_South` TIME NOT NULL , `South_Mandi` TIME NOT NULL , `Remarks` VARCHAR(40) NOT NULL ) ENGINE = InnoDB;'
cursor.execute(sql1)

db.close()

db = MySQLdb.connect (host="localhost",
    user="root",
    passwd="Jigyasha#$",
    db="bot_db",
    local_infile = 1) #Grants permission to write to db from an input file. Without this you get sql Error: (1148, 'The used command is not allowed with this MySQL version')

print("\nConnection to DB established\n")

#The statement 'IGNORE 1 LINES' below makes the Python script ignore first line on csv file
#You can execute the sql below on the mysql bash to test if it works
sqlLoadData = """load data local infile 'output_M.csv' into table tt FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;"""

try:
    curs = db.cursor()
    curs.execute(sqlLoadData)
    db.commit()
    print("SQL execution complete")
    resultSet = curs.fetchall()
except StandardError as e:
    print("Error incurred: ", e)
    db.rollback()
    db.close()

print("Data loading complete.\n")
