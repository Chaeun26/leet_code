class Solution:

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def is_valid_mutation(gene1, gene2):
            return sum(c1 != c2 for c1, c2 in zip(gene1, gene2)) == 1

        queue=[(startGene, 0)]
        visited=set()

        while queue:
            curr,count=queue.pop(0)
            if curr==endGene:
                return count
            for gene in bank:
                if gene not in visited:
                    if is_valid_mutation(curr,gene):
                        visited.add(gene)
                        queue.append((gene, count+1))

        return -1
