import csv

with open("latin-core-list.csv", 'r') as file, open('popularity.py', 'a') as file2:
    file2.write("popularity = [")
    csv_reader = csv.reader(file, delimiter=',')
    lineNum = 0
    for row in csv_reader:
        print(row[0])
        length = len(row)
        word = row[0]
        frequency = row[(length-1)]
        file2.write("['{}', '{}'],\n".format(word, frequency))
    file2.write("]")
        