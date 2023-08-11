def transform_string(input_str):
    uppercase_str = input_str.upper()
    lowercase_str = input_str.lower()
    titlecase_str = input_str.title()
    
    return uppercase_str, lowercase_str, titlecase_str

# Test the function with different strings
my_str_1 = "Life's too short to be serious. Smile and laugh more!"
my_str_2 = "python is FUN"
my_str_3 = "HELLO World!"

uppercase_result, lowercase_result, titlecase_result = transform_string(my_str_1)

print("Original String:", my_str_1)
print("Uppercase:", uppercase_result)
print("Lowercase:", lowercase_result)
print("Titlecase:", titlecase_result)
