# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 08:27:19 2023

@author: Rodrigo
"""


def read_numbers_from_file(filepath):
    numbers = []
    with open(filepath, 'r') as f:
        for line in f:
            try:
                number = float(line)
                numbers.append(number)
            except ValueError:
                pass
    return numbers

def put_numbers_in_intervals(numbers, intervals):
    interval_counts = {i: 0 for i in intervals}
    for number in numbers:
        for interval in intervals:
            if interval[0] <= number < interval[1]:
                interval_counts[interval] += 1
                break
    return interval_counts

if __name__ == '__main__':
    filepath = input('Ingresa el nombre del archivo\n')
    intervals = [(0, 5), (5, 10), (10, 15), (15, 20)]
    numbers = read_numbers_from_file(filepath)
    interval_counts = put_numbers_in_intervals(numbers, intervals)
    for interval, count in interval_counts.items():
        print(f'Number of numbers in interval {interval}: {count}')