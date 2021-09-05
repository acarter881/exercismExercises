from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS,
                                  EXAMPLE_INTERSECTION,
                                  VEGAN_INTERSECTIONS,
                                  VEGETARIAN_INTERSECTIONS,
                                  PALEO_INTERSECTIONS,
                                  KETO_INTERSECTIONS,
                                  OMNIVORE_INTERSECTIONS,
                                  example_dishes)

def clean_ingredients(dish_name, dish_ingredients):
    '''

    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    '''
    return (dish_name, set(dish_ingredients))
    
def check_drinks(drink_name, drink_ingredients):
    '''

    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")

    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    '''
    return drink_name + ' Cocktail' if True in [ingredient in ALCOHOLS for ingredient in drink_ingredients] else drink_name + ' Mocktail'
    
def categorize_dish(dish_name, dish_ingredients):
    '''

    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `categories.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    '''
    if False in [ingredient in VEGAN for ingredient in dish_ingredients]:
        pass
    else:
        return f'{dish_name}: VEGAN'

    if False in [ingredient in VEGETARIAN for ingredient in dish_ingredients]:
        pass
    else:
        return f'{dish_name}: VEGETARIAN'
        
    if False in [ingredient in PALEO for ingredient in dish_ingredients]:
        pass
    else:
        return f'{dish_name}: PALEO'

    if False in [ingredient in KETO for ingredient in dish_ingredients]:
        pass
    else:
        return f'{dish_name}: KETO'

    if False in [ingredient in OMNIVORE for ingredient in dish_ingredients]:
        pass
    else:
        return f'{dish_name}: OMNIVORE'

def tag_special_ingredients(dish):
    '''

    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `categories.py`.
    '''
    return (dish[0], {ingredient for ingredient in set(dish[1]) if ingredient in SPECIAL_INGREDIENTS})    

def compile_ingredients(dishes):
    '''

    :param dishes: list of dish ingredient sets
    :return: set

    This function should return a `set` of all ingredients from all listed dishes.
    '''
    return set([ingredient for dish in dishes for ingredient in dish])
    
def separate_appetizers(dishes, appetizers):
    '''

    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    '''
    return set([name for name in dishes if name not in appetizers])
   
def singleton_ingredients(dishes, intersection):
    '''

    :param intersection: constant - one of (VEGAN_INTERSECTION,VEGETARIAN_INTERSECTION,PALEO_INTERSECTION,
                                            KETO_INTERSECTION,OMNIVORE_INTERSECTION)
    :param dishes:  list of ingredient sets
    :return: set of singleton ingredients

    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    '''
    return set([ingredient for ingredient in compile_ingredients(dishes=dishes) if ingredient not in intersection])