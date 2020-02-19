def dedupe(items):
    seen=set()
    for item in items:
        if item not in seen:
            yield item
        seen.add(item)

a=(1,5,1,2,3,3,4,5,6,9)
b=dedupe(a)
for i in b:
    print(i)