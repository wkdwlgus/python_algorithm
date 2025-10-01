import time

# 배열 방식
def test_array():
    arr = [False] * int(1e7)
    start = time.time()
    for i in range(int(1e7)):
        arr[i % 100] = True
        if arr[i % 100]:
            arr[i % 100] = False
    return time.time() - start

# set 방식
def test_set():
    s = set()
    start = time.time()
    for i in range(int(1e7)):
        s.add(i % 100)
        if (i % 100) in s:
            s.remove(i % 100)
    return time.time() - start

print(f"Array: {test_array():.4f}s")
print(f"Set: {test_set():.4f}s")

def test_array_access():
    arr = [True] * 1000
    start = time.time()
    
    for _ in range(1000000):
        # 배열 접근
        if arr[5]: pass
        if arr[10]: pass  
        if arr[15]: pass
        
    return time.time() - start

def test_set_access():
    s = {5, 10, 15}
    start = time.time()
    
    for _ in range(1000000):
        # set 접근 
        if 5 in s: pass
        if 10 in s: pass
        if 15 in s: pass
        
    return time.time() - start

array_time = test_array_access()
set_time = test_set_access()

print(f"Array: {array_time:.4f}s")
print(f"Set: {set_time:.4f}s") 
print(f"Set is {set_time/array_time:.1f}x slower")