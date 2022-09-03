#!/bin/python3

LED_LABELS = tuple('abcdefg')

#      binary         seven segment
#   (2³ 2² 2¹ 1): (A  B  C  D  E  F  G)
TRUTH_TABLE = {
    (0, 0, 0, 0): (1, 1, 1, 0, 1, 1, 1),  # 0
    (0, 0, 0, 1): (0, 0, 1, 0, 0, 1, 0),  # 1
    (0, 0, 1, 0): (1, 0, 1, 1, 1, 0, 1),  # 2
    (0, 0, 1, 1): (1, 0, 1, 1, 0, 1, 1),  # 3
    (0, 1, 0, 0): (0, 1, 1, 1, 0, 1, 0),  # 4
    (0, 1, 0, 1): (1, 1, 0, 0, 1, 0, 1),  # 5
    (0, 1, 1, 0): (1, 1, 0, 1, 1, 1, 1),  # 6
    (0, 1, 1, 1): (1, 0, 1, 1, 0, 1, 0),  # 7
    (1, 0, 0, 0): (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 0, 0, 1): (1, 1, 1, 1, 0, 1, 1),  # 9
}

TRUTH_TABLE_OUT = {
    (0, 1, 1, 1, 0, 1, 1, 1): (0, 0, 0, 0, 0),  # 0
    (0, 0, 0, 1, 0, 0, 1, 0): (0, 0, 0, 0, 1),  # 1
    (0, 1, 0, 1, 1, 1, 0, 1): (0, 0, 0, 1, 0),  # 2
    (0, 1, 0, 1, 1, 0, 1, 1): (0, 0, 0, 1, 1),  # 3
    (0, 0, 1, 1, 1, 0, 1, 0): (0, 0, 1, 0, 0),  # 4
    (0, 1, 1, 0, 0, 1, 0, 1): (0, 0, 1, 0, 1),  # 5
    (0, 1, 1, 0, 1, 1, 1, 1): (0, 0, 1, 1, 0),  # 6
    (0, 1, 0, 1, 1, 0, 1, 0): (0, 0, 1, 1, 1),  # 7
    (0, 1, 1, 1, 1, 1, 1, 1): (0, 1, 0, 0, 0),  # 8
    (0, 1, 1, 1, 1, 0, 1, 1): (0, 1, 0, 0, 1),  # 9
    (1, 1, 1, 1, 0, 1, 1, 1): (0, 1, 0, 1, 0),  # 10
    (1, 0, 0, 1, 0, 0, 1, 0): (0, 1, 0, 1, 1),  # 11
    (1, 1, 0, 1, 1, 1, 0, 1): (0, 1, 1, 0, 0),  # 12
    (1, 1, 0, 1, 1, 0, 1, 1): (0, 1, 1, 0, 1),  # 13
    (1, 0, 1, 1, 1, 0, 1, 0): (0, 1, 1, 1, 0),  # 14
    (1, 1, 1, 0, 0, 1, 0, 1): (0, 1, 1, 1, 1),  # 15
    (1, 1, 1, 0, 1, 1, 1, 1): (1, 0, 0, 0, 0),  # 16
    (1, 1, 0, 1, 1, 0, 1, 0): (1, 0, 0, 0, 1),  # 17
    (1, 1, 1, 1, 1, 1, 1, 1): (1, 0, 0, 1, 0),  # 18
}



def sum_of_products(table: dict[tuple: tuple]) -> tuple[str]:

    num_of_bits = len(list(table.keys())[0])
    for bit_indice in range(num_of_bits):

        sum = ''
        print(1 + bit_indice)
        for bits, leds in table.items():
            if bits[bit_indice]:
                sum += ' + ' if sum else ''
                sum += ' * '.join(LED_LABELS[i] if led else
                                  f'(not {LED_LABELS[i]})'
                                  for i, led in enumerate(leds))
        print(sum)


# debug
# print('\nLEDS TO BITS\n')
# sum_of_products(TRUTH_TABLE)
# print('\nBITS TO LEDS\n')
# sum_of_products(dict(zip(TRUTH_TABLE.values(),
#                          TRUTH_TABLE.keys())))
sum_of_products(TRUTH_TABLE_OUT)
# print()

