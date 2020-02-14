import json
from itertools import filterfalse


def hello(event, context):
    numbers = range(1, 11)
    even_numbers = filterfalse(lambda num: num % 2, numbers)
    even_numbers_sqrt = map(even_sqrt, numbers)
    
    groups = naive_grouper(numbers, 2)

    response = {
        'even_numbers': list(even_numbers),
        'even_numbers_sqrt': list(even_numbers_sqrt),
        'groups': groups
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]

def even_sqrt(num):
    if num % 2 == 0:
        num = num ** num

    return num

