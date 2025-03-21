from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree={recipe:0 for recipe in recipes}
        graph=defaultdict(list)
        supplies=set(supplies)

        for recipe,ing in zip(recipes,ingredients):
            for i in ing:
                if i in set(recipes):
                    graph[i].append(recipe)
                    indegree[recipe]+=1
                elif i not in supplies:
                    pass

        queue=deque([recipe for recipe,value in indegree.items() if value==0 and set(ingredients[recipes.index(recipe)])<=supplies])
        ans=[]

        while queue:
            r=queue.popleft()
            ans.append(r)
            supplies.add(r)
            for recipe in graph[r]:
                indegree[recipe]-=1
                if indegree[recipe]==0 and set(ingredients[recipes.index(recipe)]) <= supplies:
                    queue.append(recipe)

        return ans