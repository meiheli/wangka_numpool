"""
Definations of regex tags.

Created by Tony Liu (388848@163.com)
Date: 02/11/2018
"""
regexTags = [
    (r"(\d)\1(?!\1)(\d)\2", "AABB"),
    (r"(\d)\1{2}", "AAA"),
    (r"(\d)\1{3}", "AAAA"),
    (r"(\d)\1{4}", "AAAAA"),
    (r"(0123|1234|2345|3456|4567|5678|6789|7890)", "ABCD"),
    (r"(0987|9876|8765|7654|6543|5432|4321|3210)", "DCBA"),
    (r"(01234|12345|23456|34567|45678|56789|67890)", "ABCDE"),
    (r"(09876|98765|87654|76543|65432|54321|43210)", "EDCBA"),
]