from loader import logger


def place_sign(token, data, table_dict):
    data = int(data)
    pos = table_dict[data]
    if pos not in (chr(10060), chr(11093)):
        table_dict[data] = chr(10060) if token == "X" else chr(11093)
        return table_dict
    return "The position is already occupied!"


def check_win(table_dict):
    win_coord = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    logger.debug(f'Занятые позиции {table_dict}')

    n = [table_dict[x[0]] for x in win_coord if table_dict[x[0]] == table_dict[x[1]] == table_dict[x[2]]]
    return n[0] if n else n
