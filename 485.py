# Max Consecutive Ones

def test(nums: list):
    count = final_count = 0 
    
    for index, value in enumerate(nums):
        if value == 1:
            count += 1
            
        else:
            count = 0
            
        final_count = max(count, final_count)
            
    return final_count

print(test([1,1,0,1,1,1,0,1,1,1,1,1,1]))

# runtime 376 ms, 14.5 MB memory