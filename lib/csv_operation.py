#!/usr/bin/env python
# coding=utf-8


import csv


def write_to_csv(data_list, file_path):
    """
    将数据写入CSV文件。

    :param data_list: 要写入的数据，格式为列表的列表，其中每个子列表代表一行数据。
    :param file_path: CSV文件的名称。
    """
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in data_list:
            writer.writerow(row)


def read_csv(file_path):
    """
    读取CSV文件并返回数据。

    :param file_path: CSV文件的名称。
    :return: 包含CSV数据的列表。
    """
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def load_csv_to_dict(file_path):
    lists = read_csv(file_path)
    if len(lists) == 0:
        print("load data failed, the file is empty")
        return False
    head = lists[0]
    attr_length = len(head)
    output_dict = {}
    for item in lists[1:]:
        output_dict[item[0]] = {}
        for i in range(attr_length):
            output_dict[item[0]][head[i]] = item[i]
    return output_dict

    # 示例数据


data_to_write = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"]
]

# 写入CSV文件
write_to_csv(data_to_write, r'D:\codeRoot\boss-spider\local_version\output\example.csv')

# 读取CSV文件
data = read_csv(r'D:\codeRoot\boss-spider\local_version\output\example.csv')
print(data)
data2 = load_csv_to_dict(r'D:\codeRoot\boss-spider\local_version\output\example.csv')

print(data2)
