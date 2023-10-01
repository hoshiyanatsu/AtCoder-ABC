#!/usr/bin/env python3
s = input()
moji = "aiueo"
char_list = [char for char in s if char not in moji]
print("".join(char_list))