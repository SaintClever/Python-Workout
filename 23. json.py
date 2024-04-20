import json


def print_scores(input_json):
    with open(input_json) as f:
        grades = json.load(f)
        science = [i["science"] for i in grades]
        literature = [i["literature"] for i in grades]
        maths = [i["math"] for i in grades]

        s = {
            "min": min(science),
            "max": max(science),
            "avg": sum(science) / len(science),
        }

        l = {
            "min": min(literature),
            "max": max(literature),
            "avg": sum(literature) / len(literature),
        }

        m = {"min": min(maths), "max": max(maths), "avg": sum(maths) / len(maths)}

        return f"""\nscience - min: {s["min"]}, max: {s["max"]}, avg: {s["avg"]}\
        \nliterature - min: {l["min"]}, max: {l["max"]}, avg: {l["avg"]}\
        \nmath - min: {m["min"]}, max: {m["max"]}, avg: {m["avg"]}\n"""


print(print_scores("docs/9a.json"))
