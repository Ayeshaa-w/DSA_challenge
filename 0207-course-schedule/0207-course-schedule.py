class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit=set()
        prev={i:[]for i in range(numCourses)}
        for crs,pre in prerequisites:
            prev[crs].append(pre)
        def dfs(crs):
            if crs in visit:
                return False
            if prev[crs]==[]:
                return True
            visit.add(crs)
            for j in prev[crs]:
                if not dfs(j):
                    return False
            visit.remove(crs)
            prev[crs]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        