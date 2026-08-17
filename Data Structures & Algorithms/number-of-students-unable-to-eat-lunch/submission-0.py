class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)
        for sandwich in sandwiches:
            cnt = 0 
            while cnt < n and q[0] != sandwich: 
                first = q.popleft()
                q.append(first)
                cnt += 1 

            if q[0] == sandwich: 
                q.popleft()
                n -= 1 
            else: 
                break
        return len(q)
            

        
