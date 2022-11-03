
with open('Cook_book.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for l in file:
        dish_name = l.strip()
        num_of_servings = int(file.readline())
        ingredients = []
        for ingredient in range(num_of_servings):
            ingr = file.readline().strip().split('|')
            name, quantity, measure = ingr
            ingredients.append({'ingredient_name': name,
                                'quantity': quantity,
                                'measure': measure})
        file.readline()
        cook_book[dish_name] = ingredients
    # print(cook_book)

    def get_shop_list_by_dishes(dishes, person_count):
        get_shop_list = {}
        for dish in dishes:
            if dish in cook_book:
                for el in cook_book[dish]:
                    ingredient = el['ingredient_name']
                    measure = el['measure'].strip()
                    quantity = int(el['quantity']) * person_count
                    if ingredient not in get_shop_list:
                        get_shop_list[ingredient] = {
                            'measure': measure, 'quantity': quantity}
                    else:
                        get_shop_list[ingredient]['quantity'] += quantity
        print(get_shop_list)

    # get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'],2)
