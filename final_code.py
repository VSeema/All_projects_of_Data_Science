import time
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import time, sleep
import urllib.request
import psycopg2

x_vals=[]
def animate(i):
    # requesting the url allsae.in to open    
    response = urllib.request.urlopen("https://allsafe.in/")

    # fetching status code
    status_code = response.getcode()
    try:
        # establishing connection
        connection = psycopg2.connect(user="postgres",
                                password="#########",
                                host="127.0.0.1",
                                port="5432",
                                database="Allsafe")
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO report(status) VALUES(%s);"""
        record_to_insert =status_code
        cursor.execute("rollback")
        # executing the query
        cursor.execute(postgres_insert_query,(record_to_insert,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into report table")

        # creating empty list to store status code
        status_code_list=[]

        # fetching status from database
        query="""SELECT status FROM report;"""
        cursor.execute(query)
        result = cursor.fetchall();
        # print(result)

        # since fetched result is tuple, appending each status code to status code list
        for i in range(len(result)):
            status_code_list.append(result[i][0])
            
        plt.cla()

        #plotting the line chart
        plt.plot(status_code_list)
        plt.title("Uptime / Downtime live Chart")
        plt.xlabel("Time (in seconds)")
        plt.ylabel("Uptime(200) / Downtime(500)")
        print("status_code_list",status_code_list)

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into report table", error)

#calling animate function using FuncAnimation, interval=1000 means call animate function for every second
ani=FuncAnimation(plt.gcf(),animate,interval =1000)
plt.tight_layout()
plt.show()