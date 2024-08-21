class UnionFind:
    def __init__(self, n: int):
        self.parents = {}
        self.rank = {}
        self.count = n
        for i in range(n):
            self.parents[i] =i
            self.rank[i]=0
        

    def find(self, x: int) -> int:
        p = self.parents[x]
        # path compression -> this will not nessisarily reset 
        if p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x)==self.find(y)


    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)

        if self.isSameComponent(x,y):
            return False

        if self.rank[p1]>self.rank[p2]:
            self.parents[p2] = p1
        elif self.rank[p2]>self.rank[p1]:
            self.parents[p1]=p2
        else:
            self.parents[p1]=p2
            self.rank[p2]+=1
        
        self.count-=1
        return True
        

    def getNumComponents(self) -> int:
        return self.count
    
uf = UnionFind(5)
uf.union(0,1)
uf.union(2,3)
uf.union(0,3)
uf.find(0)
uf.union(0,4)

print(uf.parents)
