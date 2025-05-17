#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            value1 = my_list_1[i]
            value2 = my_list_2[i]
            if not (isinstance(value1, (int, float)) and isinstance(value2, (int, float))):
                print("{}".format("wrong type"))
                result.append(0)
            else:
                try:
                    division = value1 / value2
                    result.append(division)
                except ZeroDivisionError:
                    print("{}".format("division by 0"))
                    result.append(0)
        except IndexError:
            print("{}".format("out of range"))
            result.append(0)
        finally:
            pass
    
    return result
