'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

    1. The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    2. You may assume that there are no duplicate edges in the input prerequisites.
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[]]) -> bool:
        graph = {n: [] for n in range(numCourses)}
        for x, y in prerequisites:
            graph[x].append(y)

        for target in range(numCourses):
            stack = graph[target]
            visited = set()
            while stack:
                course = stack.pop()
                visited.add(course)
                if course == target:
                    return False
                for i in graph[course]:
                    if i not in visited:
                        stack.append(i)
        return True


if __name__ == "__main__":
    assert True == Solution().canFinish(2, [[1, 0]])
    assert False == Solution().canFinish(2, [[1, 0], [0, 1]])
