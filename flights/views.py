import os
from os.path import join, isfile
from os import listdir
from django.shortcuts import render, redirect
from django.contrib import messages, auth
import csv
from operator import itemgetter

from airport_management_system import settings


def redirect_to_login(request):
    return redirect('flights/login')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/flights/boarding')
        else:
            print('Credentials Invalid')
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/flights/login')


def wanted_fugitives(request):
    img_list = os.listdir("flights/static/images/fugitives/")
    print(img_list)
    context = {"images": img_list}
    return render(request, 'fugitives.html', context)


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

    lines[index + 1][-1] = "Already boarded"
    file.close()

    file = open(file_path, 'w', newline='')
    csvwriter = csv.writer(file, delimiter=';')

    sorted_lines = sorted(lines[1:], key=itemgetter(5), reverse=True)  # sort without header
    sorted_lines.insert(0, lines[0])
    print(sorted_lines)
    csvwriter.writerows(sorted_lines)
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


def flight_list(request):
    print(flight_files())
    context = flight_files()
    return render(request, 'flight_list.html', {'flights': context})


def flight_files():
    files_path = "FlightFiles/"
    files = [(f.removesuffix('.csv'), f.removesuffix('.csv').removeprefix("Flight-no-"))
             for f in listdir(files_path)
             if isfile(join(files_path, f))]
    return files
