s = {
    "emp1": {"name": "John", "salary":  7500},
    "emp2": {"name": "Emma", "salary":  8000},
    "emp3": {"name": "Brad", "salary":  6500},
}
print(s["emp3"])
print(s["emp3"]["salary"])
s["emp3"]["salary"] = 8500
for i in s:
    print(i)
    for j in s[i]:
        print("\t", j, ":", s[i][j])
