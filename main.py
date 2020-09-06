import flightradar24

fr = flightradar24.Api()



'''查询所有航空公司
airlines = fr.get_airlines()

for value in airlines.values():
	print(airlines)
'''



'''查询航空公司的所有在天上的航班
airline = 'CSC' # Turkish Airlines
flights = fr.get_flights(airline)
for value in flights.values():
	if isinstance(value,list):
		print(value)


'''

'''
     |  get_airlines(self)
     |
     |  get_airports(self)
     |
     |  get_flight(self, flight_id)
     |
     |  get_flights(self, airline)
     |
     |  get_zones(self)
'''