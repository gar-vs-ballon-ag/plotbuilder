import csv
from sys import argv
import matplotlib.pyplot as plt
from Utils import get_name_time


def main():
    if len(argv) < 1:
        print("Please put the filename as parameter.")

    fr = []
    tr = []

    tg = []
    fg = []

    fb = []
    tb = []

    ff = []
    tf = []

    with open(argv[1], newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            query = get_name_time(row[0])
            if query[0].startswith("L") or query[0].startswith("F2") or query[0].startswith("BAR"):
                data = (int(query[1]) / 60000, float(query[0].split(":")[1]))
                if query[0].startswith("LR"):
                    fr.append(data[1])
                    tr.append(data[0])
                elif query[0].startswith("LG"):
                    fg.append(data[1])
                    tg.append(data[0])
                elif query[0].startswith("LB"):
                    fb.append(data[1])
                    tb.append(data[0])
                elif query[0].startswith("L_FULL"):
                    ff.append(data[1])
                    tf.append(data[0])

    print("Arrays created. Displaying Plot...")

    plt.title("Lichteinfall")
    plt.xlabel("Zeit in Minuten")
    plt.ylabel("Lichteinfall (0 bis 4048, Spannungsabfall am Widerstand)")

    plt.plot(tb, fb, label="Blaues Licht")
    plt.plot(tr, fr, label="Rotes Licht")
    plt.plot(tg, fg, label="Grünes Licht")
    plt.plot(tg, fg, label="Licht Gesamt")

    plt.legend(loc="upper center")
    plt.show()



if __name__ == "__main__":
    main()
