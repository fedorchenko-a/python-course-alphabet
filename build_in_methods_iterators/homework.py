from typing import List, Dict, Union, Generator

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> List[str]:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]

    """
    for dic in data:
        if 'name' in dic:
            a = dic.get('name').capitalize()
            dic.update({'name': a})


    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for value in data:

        for item in redundant_keys:
            value.pop(item)
    return data





def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    out_list = []
    '''for dic in data:
        if item.get() in item == value:
            out_list.append(item)
    return out_list
        x = dic.values()
        if value in x:
            out_list.append(dic)'''
    for dic in data:
        for val in dic.values():
            if val == value:
                out_list.append(dic)
    return out_list



def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    if data:
        data.sort()
        return data[0]
    else:
        return None



def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
    new_data = []
    if data:
        for item in data:

            if not isinstance(item, str):
                item = str(item)
                new_data.append(item)
            else:
                new_data.append(item)

        minim = min(new_data, key = len)
        return minim
    else:
        return None







def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """

    newdic = []
    for item in data:
        if key in item:
            newdic.append(item)
        else:
            continue
    a = min(newdic, key=lambda x: x[key])
    return a



def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    #a = max(data, key=lambda x: max(data[x]))
    #in_key = min(data, key=lambda key: min(data[key]))
    datanew = []
    for item in data:
        if len(item) != 0:
            c = max(item)
            datanew.append(c)
    a = max(datanew)
    return a


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    summ = 0
    if len(data) != 0:
        summ = sum(data)
    return summ



def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    a = 0
    calc = []
    for item in text:
        calc.append(ord(item))
    a = sum(calc)
    return a


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    primes = [2, 200]
    yield 2
    n = 3
    while True:
        for p in primes:
            if n % p == 0:
                n += 1
                break
        else:
            primes.append(n)
            yield n


def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet

    """
    import random
    import string
    a = []
    #letters = string.ascii_lowercase
    #a.append(random.choice(letters) for i in range(20))
    while len(a) < 20:
        a.append(random.choice(string.ascii_lowercase))

    return a