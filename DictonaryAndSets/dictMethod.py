marks = {
    "harry": 12,
    "ron": 11,
    "hermione": 9
    
}

#1.  .markitems, will return key-value pair in tuple
# print(marks.items()) 

# 2. .keys and .values

# print(marks.keys())
# print(marks.values())

# 3. .update
# marks.update({"harry": 78})
# print(marks)

# 4. get method

# print(marks.get("harry"))

# 5. pop method
# marks.pop("harry")
# print(marks)  # Output: {'ron': 11, 'hermione':
# 6. popitem method
# marks.popitem()
# print(marks)  # Output: {'ron': 11, 'hermione':