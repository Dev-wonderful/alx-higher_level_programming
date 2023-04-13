#!/usr/bin/python3

"""A module to add items to a list and serialize it"""
save_to_json_file = __import__('5-save_to_json_file')
sys = __import__('sys')


filename = "add_item.json"
my_list = sys.argv[1:]
save_to_json_file(my_list, filename)
