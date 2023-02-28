import csv
import time


def write_csv(save_file_path):
    with open(save_file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow("Hi")


if __name__ == '__main__':
    timestr = time.strftime("%Y%m%d-%H%M%S")
    write_csv(timestr)
