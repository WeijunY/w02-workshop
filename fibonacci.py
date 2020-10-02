# Task 1: Generalised Fibonacci

# Define your function here:
def fib(p,q,n):
    dp=[1]*n
    for i in range(2,n):
        dp[i]=p*dp[i-1]+q*dp[i-2]
    print(dp)
fib(1,1,15)
fib(1,3,15)



# Tests

print(p_q_fibo(1, 1, 15))
# Expected result: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

print(p_q_fibo(1, 3, 15))
# Expected result: [1, 1, 4, 7, 19, 40, 97, 217, 508, 1159, 2683, 6160, 14209, 32689, 75316]

print(p_q_fibo(2, 2, 15))
# Expected result: [1, 1, 4, 10, 28, 76, 208, 568, 1552, 4240, 11584, 31648, 86464, 236224, 645376]

print(p_q_fibo(6, 4, 10))
# Expected result: [1, 1, 10, 64, 424, 2800, 18496, 122176, 807040, 5330944]
