#!/usr/bin/env python3
# #Author ID: pgerrard1

file_name = 'data.txt'

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    result = f.read()
    f.close()
    return result


def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    result = f.readlines()
    f.close()
    return [line.strip() for line in result]


if __name__ == '__main__':
    file_name = 'data.txt'
    file_string = read_file_string(file_name)

    print(read_file_string(file_name))
    print(read_file_list(file_name))