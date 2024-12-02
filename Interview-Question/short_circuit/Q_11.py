# 10. Short-Circuit with Lambdas
# Question: Will the lambda function execute?

func = lambda: print("This won't run")
result = 0 or func()


# Solution:

# 0 or func(): 0 is False, so func() is executed.
# Output: "This won't run"
