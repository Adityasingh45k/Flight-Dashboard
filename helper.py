import mysql.connector


class DB:
    def __init__(self):

        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Deepanshu',
                database='indigo'
            )
            self.mycursor = self.conn.cursor()
            print("connection established")
        except:
            print("connection error")
        # self.mycursor.execute("Create Database indigo")
        # self.conn.commit()
    def fetch_city(self):
        city=[]
        self.mycursor.execute("""select distinct(destination)from indigo.flights
                                  union 
                                 select distinct(source)from indigo.flights""")
        data=self.mycursor.fetchall()
        print(data)
        for i in data:
            city.append(i[0])
        return city
    def fetch_all_flight(self,source,destination):
        self.mycursor.execute("""select Airline,Route,Dep_Time,Duration,Price from indigo.flights where source='{}' and destination='{}'""".format(source,destination))
        data=self.mycursor.fetchall()
        return data
    def fetch_frequency(self):
        airline=[]
        freq=[]
        x = "select airline,count(*) from indigo.flights group By airline;"
        self.mycursor.execute(x)

        data=self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            freq.append(item[1])
        return airline,freq
    def busy(self):
        self.mycursor.execute("""
        select source, count(*) from(select source from indigo.flights Union All select destination from indigo.flights)
        as t group by source
        order by count(*) desc
        """)
        city = []
        freq = []
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            freq.append(item[1])
        return city, freq
    def daily(self):
        self.mycursor.execute("""
        select Date_of_Journey, count(*) from indigo.flights group by Date_of_Journey
        """)
        dailye = []
        freq = []
        data = self.mycursor.fetchall()
        for item in data:
            dailye.append(item[0])
            freq.append(item[1])
        return dailye, freq

