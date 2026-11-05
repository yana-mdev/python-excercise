def cookbook(*args):
    cookbook_dict = {}
    for recipe_name, cuisine, list_of_ingredients in args:
        if cuisine not in cookbook_dict:
            cookbook_dict[cuisine] = {}
        cookbook_dict[cuisine][recipe_name] = list_of_ingredients

    sorted_cookbook = sorted(cookbook_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for cuisine, recipes in sorted_cookbook:
        result.append(
            f"{cuisine} cuisine contains {len(recipes)} recipes:"
        )
        for recipe, ingredients in sorted(recipes.items()):
            result.append(
                f"  * {recipe} -> Ingredients: {', '.join(ingredients)}"
            )

    return "\n".join(result)


