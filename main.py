users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"},
         {"name": "Yeti", "country": "USA"}]


def only_poland(list):
    return [i for i in list if i.get("country") == "Poland"]


print(only_poland(users))

numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]


def sum_of_first_ten_elements(list):
    idx = list.index(5)
    new_list = list[idx: idx + 10]
    return sum(new_list)


print(sum_of_first_ten_elements(numbers))


def power_of_2(n):
    return [2 ** n for n in range(1, n)]


print(power_of_2(20))
