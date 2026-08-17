class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Website(homepage, None, None)

    def visit(self, url: str) -> None:
        self.cur.next = Website(url, self.cur, None)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next: 
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
        
class Website: 
    def __init__(self, val, prev, next): 
        self.val = val
        self.prev = prev
        self.next = next

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)