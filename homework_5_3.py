import sys
from typing import List


def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 4)
    date = parts[0]
    time = parts[1]
    level = parts[2]
    message = parts[4].strip()
    return {
        'date': date,
        'time': time,
        'level': level,
        'message': message
    }


def load_logs(file_path: str) -> list[dict] | str:
    try:
        with open(file_path, encoding="utf-8", mode='r') as file:
            log_list = []
            for line in file:
                log_list.append(parse_log_line(line))
        return log_list
    except Exception as e:
        return f"{e} has occured"


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level]


def count_logs_by_level(logs: list) -> dict:
    log_counts = {'INFO': 0, 'ERROR': 0, 'DEBUG': 0, 'WARNING': 0}
    for log in logs:
        log_counts[log['level']] += 1
    return log_counts


def display_log_counts(counts):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count:>8}")


# Rest of your code remains unchanged


if __name__ == "__main__":
    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)

    if len(sys.argv) == 3:
        log_level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, log_level)
        counts = count_logs_by_level(filtered_logs)
        display_log_counts(counts)
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

# print(load_logs("/Users/alinakylymnyk/Documents/python_projects/homework_5/log_file"))
