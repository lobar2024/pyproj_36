class Deque:
    def __init__(self):
        self._data = []

    def push_front(self, val): self._data.insert(0, val)
    def push_back(self, val):  self._data.append(val)
    def pop_front(self):
        if not self._data: raise IndexError("Bo'sh!")
        return self._data.pop(0)
    def pop_back(self):
        if not self._data: raise IndexError("Bo'sh!")
        return self._data.pop()
    def peek_front(self): return self._data[0]  if self._data else None
    def peek_back(self):  return self._data[-1] if self._data else None
    def __len__(self):    return len(self._data)
    def __str__(self):    return f"Deque{self._data}"

def is_palindrome(s):
    """Deque yordamida palindrom tekshirish."""
    dq = Deque()
    for ch in s.lower():
        if ch.isalpha(): dq.push_back(ch)
    while len(dq) > 1:
        if dq.pop_front() != dq.pop_back():
            return False
    return True

if __name__ == "__main__":
    dq = Deque()
    dq.push_back(1)
    dq.push_back(2)
    dq.push_front(0)
    print(dq)              # Deque[0, 1, 2]
    print(dq.pop_back())   # 2
    print(dq.pop_front())  # 0

    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))    # False
