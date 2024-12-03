# ДЗ: Сложение элементов списков
import itertools


def list_sum(list1, list2):
    summary = [i + y for (i, y) in itertools.zip_longest(list1, list2, fillvalue=0)]
    return summary


def list_sum_manual(list1, list2):
    summary = []
    diff = len(list1) - len(list2)
    if diff > 1:
        for i, v in enumerate(list2):
            summary.append(list1[i] + v)
        summary += list1[-diff:]
    elif diff < 0:
        for i, v in enumerate(list1):
            summary.append(list2[i] + v)
        summary += list2[diff:]
    else:
        for i, v in enumerate(list1):
            summary.append(list2[i] + v)
    return summary


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [3, 2, 1]
    print(f"""
Первый список чисел: {list1} 
Второй список чисел: {list2}
Результат сложения списков: {list_sum_manual(list1, list2)}
Результат сложения списков: {list_sum(list1, list2)}
""")


main()
