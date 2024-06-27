# raise Exception("BAD")

# raise FileExistsError("NO FILE")

try:
    x=7/0
except Exception as e:
    print(e)
finally:
    print("CLEAN UP TASK")