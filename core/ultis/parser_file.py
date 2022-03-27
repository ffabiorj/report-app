from typing import TextIO, List


def parser_values(file: TextIO) -> List:
    """A function that parser value from a txt file"""
    with open("values.txt") as file:
        lines = file.readlines()
    lines = [
                {
                    "type_": line[0],
                    "date": line[1:9],
                    "value": line[9:19],
                    "cpf": line[19:30],
                    "card": line[30:42],
                    "hour": line[42:48],
                    "store_onwer": line[48:62],
                    "store_name": line[62:]
                }
                for line in lines
            ]
    return lines
    

