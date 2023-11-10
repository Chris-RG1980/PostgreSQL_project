import psycopg2
from config import config

# read connection parameters
params = config()


# connect to "chinook" database
connection = psycopg2.connect(**params)


# build a cursor object of the database
cursor = connection.cursor()


# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only the albums with "ArtistID" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all tracks where the composer is "Queen" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - Select all tracks where the composer is "Gene Simmons" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Gene Simmons"])

# Query 8 - Select all tracks where the composer is "Test" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Test"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
