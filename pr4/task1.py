# def join_words(*words, separator: str = "-") -> str:
#     return separator.join(words)

# def join_words(words, separator: str = "-") -> str:
#     join_res = ""
#     for w in words:
#         if not join_res:
#             join_res = f"{w}"
#         else:
#             join_res = f"{join_res}{separator}{w}"
#     return join_res

def join_words(words, separator: str = "-") -> str:
    join_res = ""
    for i, w in enumerate(words):
        if i == 0:
            join_res = f"{w}"
        else:
            join_res = f"{join_res}{separator}{w}"
    return join_res

print(join_words(["hi", "hello"], separator="+"))
