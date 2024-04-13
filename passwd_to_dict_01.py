from pprint import pprint

"""
“password file,” commonly stored as /etc/passwd, and returns a dict based on it. If  you don't have access to such a file, you can download one that I've uploaded at  http://mng.bz/2XXg. Here's a sample of what the file looks like:

nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false  root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false

Each line is one user record, divided into colon-separated fields. The first field (index  0) is the username, and the third field (index 2) is the user's unique ID number. (In  the system from which I took the /etc/passwd file, nobody has ID -2, root has ID 0,  and daemon has ID 1.) For our purposes, you can ignore all but these two fields.

Sometimes, the file will contain lines that fail to adhere to this format. For example, we generally ignore lines containing nothing but whitespace. Some vendors (e.g.,  Apple) include comments in their /etc/passwd files, in which the line starts with a #  character.

The function passwd_to_dict should return a dict based on /etc/passwd in  which the dict's keys are usernames and the values are the users' IDs.
"""


def passwd_to_dict():
    output = {}

    with open("passwd/passwd.txt") as f:
        file = f.readlines()

    for lines in file:
        if not lines.startswith(("#", "\n")):
            user_info = lines.split(":")
            output[user_info[0]] = int(user_info[2])

    return output


pprint(passwd_to_dict())
