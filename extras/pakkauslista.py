ITEM_PROMPT: str = "Anna esine (tyhjä lopettaa): "
RESULT_HEADING: str = "\nAnnetut esineet:"

item_set = set()

while user_input := input(ITEM_PROMPT):
    if user_input not in item_set:
        item_set.add(user_input)
    else:
        print(f"{user_input} löytyy jo!")

print(RESULT_HEADING)
for idx, item in enumerate(item_set):
    print(f"{idx + 1}. {item.capitalize()}")
