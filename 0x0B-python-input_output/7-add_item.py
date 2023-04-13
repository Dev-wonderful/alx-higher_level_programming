#!/usr/bin/python3

"""A module to add items to a list and serialize it"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
sys = __import__('sys')


filename = "add_item.json"
try:
    j_file = load_from_json_file(filename)
except Exception:
    my_list = sys.argv[1:]
    save_to_json_file(my_list, filename)
else:
    my_list = j_file[:] + sys.argv[1:]
    save_to_json_file(my_list, filename)
