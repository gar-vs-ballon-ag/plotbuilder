import csv
from sys import argv
import matplotlib.pyplot as plt
from Utils import get_name_time


def main():
    if len(argv) < 1:
        print("Please put the filename as parameter.")
        exit(1)

    f1 = []
    t1 = []

    t2 = []
    f2 = []

    f3 = []
    t3 = []

    with open(argv[1], newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            query = get_name_time(row[0])
            if query[0].startswith("F1") or query[0].startswith("F2") or query[0].startswith("BAR"):
                data = (int(query[1]) / 60000, float(query[0].split(":")[1]))
                if query[0].startswith("F1"):
                    f1.append(data[1])
                    t1.append(data[0])
                elif query[0].startswith("F2"):
                    f2.append(data[1])
                    t2.append(data[0])
                elif query[0].startswith("BAR"):
                    f3.append(data[1])
                    t3.append(data[0])

    print("Arrays created. Displaying Plot...")

    plt.title("Außen- und Innentemperatur, Vergleich von DHT22 und BMP085")
    plt.xlabel("Zeit in Minuten")
    plt.ylabel("Temperatur in °C")

    plt.plot(t1, f1, label="Außen DHT22")
    plt.plot(t2, f2, label="Innen DHT22")
    plt.plot(t3, f3, label="Innen BMP085")

    plt.legend(loc="upper right")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
