#1️⃣ match_a_followed_by_b(string)
print(match_a_followed_by_b("abbb"))  # True
print(match_a_followed_by_b("aaa"))   # True
print(match_a_followed_by_b("b"))     # False

#2️⃣ match_a_followed_by_2_to_3_b(string)
print(match_a_followed_by_2_to_3_b("abb"))   # True
print(match_a_followed_by_2_to_3_b("abbbb")) # False

#3️⃣ find_lowercase_with_underscore(string)
print(find_lowercase_with_underscore("this_is_a_test example_text"))  
# ['this_is', 'example_text']

#4️⃣ find_upper_followed_by_lower(string)
print(find_upper_followed_by_lower("Hello World Test String"))  
# ['Hello', 'World', 'Test', 'String']

#5️⃣ match_a_followed_by_anything_ending_b(string)
print(match_a_followed_by_anything_ending_b("axxxb"))  # True
print(match_a_followed_by_anything_ending_b("ab"))     # True
print(match_a_followed_by_anything_ending_b("acb"))    # False

#6️⃣ replace_spaces_commas_dots(string)
print(replace_spaces_commas_dots("Hello, world. How are you?"))  
# "Hello:world:How:are:you:"

#7️⃣ snake_to_camel(snake_str)
print(snake_to_camel("this_is_a_test"))  
# "thisIsATest"

#8️⃣ split_at_uppercase(string)
print(split_at_uppercase("SplitAtUppercase"))  
# ['Split', 'At', 'Uppercase']

#9️⃣ insert_spaces_between_capitals(string)
print(insert_spaces_between_capitals("InsertSpacesBetweenCapitals"))  
# "Insert Spaces Between Capitals"

#🔟 camel_to_snake(camel_str)
print(camel_to_snake("CamelCaseString"))  
# "camel_case_string"

