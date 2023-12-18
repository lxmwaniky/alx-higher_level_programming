#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(list_length):
        div = None
        try:
            if isinstance(my_list_1[i], (int, float)):
                div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        except TypeError:
            print('wrong type')
        finally:
            if div is not None:
                div_list.append(div)
            else:
                div_list.append(0)
    return div_list
