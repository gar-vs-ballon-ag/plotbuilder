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

    with open(argv[1], newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            query = get_name_time(row[0])
            if query[0].startswith("BAR"):
                data = (int(query[1]) / 60000, float(row[1]))
                f1.append(data[1])
                t1.append(data[0])


    print("Arrays created. Displaying Plot...")

    plt.title("Luftdruck")
    plt.xlabel("Zeit in Minuten")
    plt.ylabel("Druck in Bar")

    plt.plot(t1, f1, label="Druck (BMP085)")

    plt.legend(loc="upper right")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
