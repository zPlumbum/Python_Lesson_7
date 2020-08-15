# Задание №1
cook_book = {}
recipe = []

with open('recipes.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        if line != '\n':
            line = line.replace('\n', '')

        if ('|' not in line) and (line != '\n') and (not line.isdigit()):
            recipe_name = line
        elif '|' in line:
            ingredient = list(line.split(' | '))
            ingredient_dict = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
            recipe.append(ingredient_dict)
        elif line == '\n':
            cook_book.setdefault(recipe_name, recipe)
            recipe = []
    cook_book.setdefault(recipe_name, recipe)

print(cook_book)

# Задание №2
dishes = list(input('Введите через запятую названия блюд, которые хотите приготовить: ').split(', '))
person_count = int(input('Укажите количество людей: '))

def get_shop_list_by_dishes(dishes, person_count):
    buy_list = []
    buy_dict = {}

    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for ingredient in ingredients:
                buy_list.append(ingredient)
    for item in buy_list:
        item['quantity'] = int(item['quantity']) * person_count
        ingred_dict = {'quantity': item['quantity'], 'measure': item['measure']}
        if item['ingredient_name'] not in buy_dict.keys():
            buy_dict.setdefault(item['ingredient_name'], ingred_dict)
        else:
            buy_dict[item['ingredient_name']]['quantity'] += item['quantity']

    print(buy_dict)

get_shop_list_by_dishes(dishes, person_count)