#!/usr/bin/python3.7

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="user",
    password="correcthorsebatterystaple",
    database="movies"
)

cursor = db.cursor()

with open("mysql.sql") as file:
    queries = list(x.strip()+";" for x in file.read().split(";\n"))

qCount = len(queries)

for i, query in enumerate(queries):
    print(f"[{i}/{qCount}] - {query}")
    cursor.execute(query)