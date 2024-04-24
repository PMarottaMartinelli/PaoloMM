from pathlib import Path
import json


# def read_write_highscore_file(file_path, num_correct):
#     file_path = Path(file_path)
#     old_highscore = ""
#     if file_path.exists():
#         with open(file_path, "r", encoding="utf-8") as f:
#             old_highscore = f.readline()

#     if old_highscore:
#         print(f"Alter highscore: {old_highscore}")
#         if num_correct > int(old_highscore):
#             print(f"Neuer highscore: {num_correct}")
#             with open(file_path, "w", encoding="utf-8") as f:
#                 f.write(str(num_correct))
#     else:
#         with open(file_path, "w", encoding="utf-8") as f:
#             f.write(str(num_correct))


def read_highscore_file(file_path):
    """Reads highscore file if existent and returns content."""
    file_path = Path(file_path)
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            highscore_info = json.load(f)
        return highscore_info
    else:
        return {}


def write_highscore_file(file_path, highscore_info):
    old_highscore_info = read_highscore_file(file_path)

    old_highscore = old_highscore_info["highscore"]

    num_correct = highscore_info["highscore"]

    if old_highscore:
        print(f"Alter highscore: {old_highscore}")
        if num_correct > old_highscore:
            print(f"Neuer highscore: {num_correct}")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(highscore_info, f)
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(highscore_info, f)
