import csv


def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename) as passwd, open(csv_filename, "w") as output:
        infile = csv.reader(passwd, delimiter=":")
        outfile = csv.writer(output, delimiter="\t")

        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))


print(passwd_to_csv("docs/passwd.txt", "docs/file_01.csv"))
