import csv


def passwd_to_csv(input_file, output_file):
    with open(input_file) as txt_file, open(output_file, "w") as csv_file:
        csv_reader = csv.reader(txt_file, delimiter=":")
        csv_writer = csv.writer(csv_file)
        [csv_writer.writerow((i[0], i[2])) for i in csv_reader if len(i) > 1]

    return f"Path: {output_file}"


print(passwd_to_csv("docs/passwd.txt", "docs/file_02.csv"))
