from django.shortcuts import render
from django.contrib import messages
import csv


def login_me(request):
    return render(request, 'login.html', {'name': 'Userrito'})


def read_flight_file(flight_number):
    file_path = 'FlightFiles/Flight-no-' + flight_number + '.csv'
    file = open(file_path)
    csvreader = csv.reader(file, delimiter=';')

    header = next(csvreader)
    rows = []

    row_index = 0
    for row in csvreader:
        rows.append((row, row_index))
        row_index += 1

    file.close()

    if 'Boarded' not in header:
        file = open(file_path, 'w', newline='')
        header.append("Boarded")

        for row, index in rows:
            row.append("False")

        csvwriter = csv.writer(file, delimiter=';')
        print(header)
        csvwriter.writerow(header)

        for row, index in rows:
            csvwriter.writerow(row)
        file.close()

    return header, rows


def newboarded(flight_number, index):
    file_path = 'FlightFiles/Flight-no-' + flight_number + '.csv'
    file = open(file_path)
    r = csv.reader(file, delimiter=';')
    lines = list(r)

    lines[index+1][-1] = "Already boarded"
    file.close()

    file = open(file_path, 'w', newline='')
    csvwriter = csv.writer(file, delimiter=';')

    csvwriter.writerows(lines)
    file.close()


def boarding(request, flight_number):
    try:
        if request.method == 'POST':
            boarded = request.POST.get("resently_boarded", None)
            newboarded(flight_number, int(boarded))

        header, rows = read_flight_file(flight_number)
    except FileNotFoundError:
        header = []
        rows = []
        messages.info(request, "There is no data about such a flight")

    return render(request, 'boarding.html', {'flight_number': flight_number, 'header': header, 'rows': rows})
