import csv

csv_file_path = 'sensor_data'
file_num = 1

with open(csv_file_path + str(file_num) + '.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Time', 'aMag', 'gMag', 'ang', 'bpm', 'but'])