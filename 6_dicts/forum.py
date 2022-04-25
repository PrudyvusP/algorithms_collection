import sys
from collections import defaultdict


if __name__ == '__main__':
    n = int(input())
    main_counter = 1
    topics = defaultdict(list)
    topics_new = dict()
    while main_counter <= n:
        row = sys.stdin.readline().rstrip()
        if row == '0':
            topic_name = sys.stdin.readline().rstrip()
            message = sys.stdin.readline().rstrip()
            message_id = main_counter
            topics[topic_name].append(message_id)
            main_counter += 1
        elif row.isdigit():
            message_id = int(row)
            _ = sys.stdin.readline()
            for k, v in topics.items():
                if message_id in v:
                    topics[k].append(main_counter)
            main_counter += 1

    print(sorted(list(topics.items()), key=lambda x: -len(x[1]))[0][0])
