def find_max(values):
    """Find the largest value in the list"""
    biggest = values[0]
    for num in values: 
        if num > biggest:
            biggest = num
    return biggest

def count_occurances(items, target):
    """Count the amount of times an item occurs in a list"""
    count = 0
    for v in items:
        if v == target:
            count += 1
    return count

def filter_by_value(dic,min):
    """Return a new dictionary with only values above the provided minimum"""
    new = {}
    for k, v in dic.items():
        if v >= min:
            new[k] = v
    return new   
    
nums = [3,2,8,9]
print(find_max(nums))

val = ["a","b","a","a","c","a"]
print(count_occurances(val,"a"))

rest = {"ana":10, "ben": 15, "cate":20}
print(filter_by_value(rest,10))