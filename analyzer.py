import argparse
from collections import Counter


def parse_logs(file_path):
    errors = []
    warnings = []
    all_messages = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                all_messages.append(line)

                lower_line = line.lower()
                if "error" in lower_line:
                    errors.append(line)
                elif "warning" in lower_line:
                    warnings.append(line)

    except FileNotFoundError:
        print("Error: Log file not found.")
        return [], [], []

    return errors, warnings, all_messages


def show_summary(errors, warnings, all_messages):
    print("\n===== LOG SUMMARY =====")
    print(f"Total lines   : {len(all_messages)}")
    print(f"Error count   : {len(errors)}")
    print(f"Warning count : {len(warnings)}")


def show_top_messages(all_messages, top_n):
    print(f"\n===== TOP {top_n} FREQUENT MESSAGES =====")
    counter = Counter(all_messages)

    for message, count in counter.most_common(top_n):
        print(f"{count}x  ->  {message}")


def show_sample(errors, warnings):
    if errors:
        print("\n===== SAMPLE ERRORS =====")
        for e in errors[:5]:
            print(e)

    if warnings:
        print("\n===== SAMPLE WARNINGS =====")
        for w in warnings[:5]:
            print(w)


def main():
    parser = argparse.ArgumentParser(description="Log Analyzer CLI Tool")

    parser.add_argument("file", help="Path to log file")
    parser.add_argument("--top", type=int, default=5, help="Top frequent messages")

    args = parser.parse_args()

    errors, warnings, all_messages = parse_logs(args.file)

    if not all_messages:
        print("No logs to analyze.")
        return

    show_summary(errors, warnings, all_messages)
    show_top_messages(all_messages, args.top)
    show_sample(errors, warnings)


if __name__ == "__main__":
    main()