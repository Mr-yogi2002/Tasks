
# that sum to a given value

def find3Numbers(A, arr_size, sum):
    for i in range(0, arr_size - 2):

        for j in range(i + 1, arr_size - 1):

            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    print("Triplet is", A[i],
                          ", ", A[j], ", ", A[k])
                    return True

    return False


# Driver program  function
A = [10,20,30,9]
sum = 59
arr_size = len(A)
find3Numbers(A, arr_size, sum)

# Python  program to find all the triplets with the given sum