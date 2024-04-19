import csv


def passwd_to_csv(input_txt, output_csv):
    output = [["key", "value"]]

    # Input: TXT
    with open(input_txt) as f:
        txt_file = f.readlines()

        for i in txt_file:
            if ":" in i:
                key = i[: i.find(":")]
                value = i[i.find("*:") + 2 :]
                output.append([key, value[: value.find(":")]])

    # Output: CSV
    with open(output_csv, "w") as f:
        writer = csv.writer(f)
        writer.writerows(output)

    return f"\nFile: {output_csv}\n"


print(passwd_to_csv("docs/passwd.txt", "docs/file.csv"))
