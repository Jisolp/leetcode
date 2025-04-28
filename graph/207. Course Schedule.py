class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        preMap = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True 
            
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        
    