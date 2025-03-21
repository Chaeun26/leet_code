from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        num_of_pre={recipe:0 for recipe in recipes}
        graph={}

        recipe_ingredients_map = {recipe:set(ing) for recipe,ing in zip(recipes, ingredients)}
        recipes=set(recipes)
        supplies=set(supplies)

        for recipe,ing in recipe_ingredients_map.items():
            for i in ing:
                if i in recipes:
                    if i in graph:
                        graph[i].append(recipe)
                    else:
                        graph[i]=[recipe]

                    num_of_pre[recipe]+=1

        starters = deque([recipe for recipe, value in num_of_pre.items() if value==0])
        ans=[]

        while starters:
            recipe=starters.popleft()
            if recipe_ingredients_map[recipe] <= supplies:
                ans.append(recipe)
                supplies.add(recipe)
                if recipe in graph:
                    for mem in graph[recipe]:
                        num_of_pre[mem]-=1
                        if num_of_pre[mem]==0:
                            starters.append(mem)


        return ans