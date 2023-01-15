import csv
from sys import argv
import matplotlib.pyplot as plt
from Utils import get_name_time


def main():
    if len(argv) < 1:
        print("Please put the filename as parameter.")

    f1 = []
    t1 = []

    f3 = []
    t3 = []

    with open(argv[1], newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            query = get_name_time(row[0])
            if query[0].startswith("F1") or query[0].startswith("BAR"):
                data = (int(query[1]) / 60000, float(query[0].split(":")[1]))
                if query[0].startswith("F1"):
                    f1.append(data[1])
                    t1.append(data[0])
                elif query[0].startswith("BAR"):
                    f3.append(data[1])
                    t3.append(data[0])

    print("Arrays created. Displaying Plot...")

    plt.title("Außen(Blau DHT22)- und Innentemperatur(Rot BMP180)")
    plt.xlabel("Zeit in Minuten")
    plt.ylabel("Temperatur in °C")

    plt.plot(t1, f1, label="Außentemperatur (DHT22)")
    plt.plot(t3, f3, label="Innentemperatur (BMP085)")

    plt.legend(loc="upper right")
    plt.show()


if __name__ == "__main__":
    main()
