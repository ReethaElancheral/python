from textutils import sanitize, word_count, char_count, most_common

txt = "Hello, world! Hello!!"
print(sanitize(txt))


print(word_count(txt))


print(char_count(txt))


print(most_common("apple banana apple orange banana apple", 2))

