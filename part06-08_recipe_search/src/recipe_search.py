def search_by_name(filename: str, word: str):
    try:
        with open(filename) as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

    found_recipes = []
    i = 0
    
    while i < len(lines):
        recipe_name = lines[i]
        
        if word.lower() in recipe_name.lower():
            found_recipes.append(recipe_name)
            
        i += 1
        
        if i < len(lines):
            i += 1
        else:
            break
            
        while i < len(lines) and lines[i] != "":
            i += 1
            
        i += 1
        
    return found_recipes

def search_by_time(filename: str, prep_time: int):
    try:
        with open(filename) as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

    found_recipes = []
    i = 0
    
    while i < len(lines):
        recipe_name = lines[i]
        
        if i + 1 >= len(lines):
            break 
            
        try:
            recipe_time_str = lines[i+1]
            recipe_time_int = int(recipe_time_str)
        except ValueError:
            i += 2
            while i < len(lines) and lines[i] != "":
                i += 1
            i += 1
            continue 

        if recipe_time_int <= prep_time:
            found_recipes.append(f"{recipe_name}, preparation time {recipe_time_int} min")
            
        i += 1
        
        if i < len(lines):
            i += 1
        else:
            break
            
        while i < len(lines) and lines[i] != "":
            i += 1
            
        i += 1
        
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    try:
        with open(filename) as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

    found_recipes = []
    i = 0
    
    while i < len(lines):
        recipe_name = lines[i]
        
        if i + 1 >= len(lines):
            break
            
        try:
            recipe_time_str = lines[i+1]
            recipe_time_int = int(recipe_time_str)
        except ValueError:
            i += 2
            while i < len(lines) and lines[i] != "":
                i += 1
            i += 1
            continue

        ingredient_start_index = i + 2
        ingredient_end_index = ingredient_start_index

        while ingredient_end_index < len(lines) and lines[ingredient_end_index] != "":
            ingredient_end_index += 1

        ingredient_list = lines[ingredient_start_index:ingredient_end_index]
        
        ingredient_found = False
        for item in ingredient_list:
            if item.lower() == ingredient.lower():
                ingredient_found = True
                break 
                
        if ingredient_found:
            found_recipes.append(f"{recipe_name}, preparation time {recipe_time_int} min")
            
        i = ingredient_end_index
        if i < len(lines):
            i += 1
            
    return found_recipes

if __name__ == "__main__":
    
    with open("recipes1.txt", "w") as f:
        f.write("Pancakes\n")
        f.write("15\n")
        f.write("milk\n")
        f.write("eggs\n")
        f.write("flour\n")
        f.write("sugar\n")
        f.write("salt\n")
        f.write("butter\n")
        f.write("\n")
        f.write("Meatballs\n")
        f.write("45\n")
        f.write("mince\n")
        f.write("eggs\n")
        f.write("breadcrumbs\n")
        f.write("\n")
        f.write("Tofu rolls\n")
        f.write("30\n")
        f.write("tofu\n")
        f.write("rice\n")
        f.write("water\n")
        f.write("\n")
        f.write("Cake pops\n")
        f.write("60\n")
        f.write("milk\n")
        f.write("bicarbonate\n")
        f.write("eggs\n")

    print("Searching for 'cake'...")
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)
        
    print("\nSearching for 'rolls'...")
    found_recipes_2 = search_by_name("recipes1.txt", "rolls")
    for recipe in found_recipes_2:
        print(recipe)

    print("\nSearching for recipes 20 min or less...")
    found_recipes_3 = search_by_time("recipes1.txt", 20)
    for recipe in found_recipes_3:
        print(recipe)

    print("\nSearching for recipes with 'eggs'...")
    found_recipes_4 = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes_4:
        print(recipe)