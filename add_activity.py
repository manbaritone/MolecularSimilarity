""""
add real activity to similarity

Usage:
    python add_activity.py
        -s (input json lines file from score_molecule program)
        -a (input json file with test activity)
        -o (output json lines file)

"""

import argparse
import json

import my_library


def _read_configuration() -> dict:
    parser = argparse.ArgumentParser(description="add activity "
                                                 "See file header for more details.")
    parser.add_argument("-s", type=str, dest="score", required=True)
    parser.add_argument("-a", type=str, dest="activity", required=True)
    parser.add_argument("-o", type=str, dest="output", required=True)
    return vars(parser.parse_args())


def read_activity(input_activity: str) -> list:
    with open(input_activity, "r") as stream:
        for line in stream:
            activity = json.loads(line)
            return activity["activity"]


def write_to_json(input_score: str, activity: list, output_file: str):
    my_library.create_parent_directory(output_file)
    with open(output_file, "w") as output_stream:
        with open(input_score, "r") as stream:
            for num, line in enumerate(stream):
                score = json.loads(line)
                output = {
                    "name": score["name"],
                    "score": score["score"],
                    "activity": activity[num]
                }
                if num != 0:
                    output_stream.write("\n")
                json.dump(output, output_stream)


def _main():
    configuration = _read_configuration()
    activity = read_activity(configuration["activity"])
    write_to_json(configuration["score"], activity, configuration["output"])


if __name__ == "__main__":
    _main()
