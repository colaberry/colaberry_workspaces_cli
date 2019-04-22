import csv


def read_csv(file):
    list_of_user = list()
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            list_of_user.append(row[0])

    return list_of_user

