import pandas
data = pandas.read_csv('50_states.csv')
print(data)
print(data.state)
bien = data[data['state'] == 'Michigan']
print(bien.x)