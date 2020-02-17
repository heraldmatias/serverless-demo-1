import json
from itertools import filterfalse
import fcc

def hello(event, context):
    numbers = range(1, 11)
    even_numbers = filterfalse(lambda num: num % 2, numbers)
    even_numbers_sqrt = map(even_sqrt, numbers)
    s = sum(numbers)

    plus_5 = fcc.make_adder(5) 
    
    plus_10 = fcc.make_adder(10)
    speak_test = fcc.speak('HELLO')

    adder_obj = fcc.Adder(4)
    

    groups = naive_grouper(numbers, 2)

    response = {
        'even_numbers': list(even_numbers),
        'even_numbers_sqrt': list(even_numbers_sqrt),
        'groups': groups,
        'plus_5_val': plus_5(5),
        'plus_10_val': plus_10(20),
        'speak_test': speak_test,
        'adder_test': adder_obj(6),
        'adder_test_plus': adder_obj.plus(10)
    }

    try:
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as e:
      return {
          'message': str(e)
      }

def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]

def even_sqrt(num):
    if num % 2 == 0:
        num = num ** num

    return num

