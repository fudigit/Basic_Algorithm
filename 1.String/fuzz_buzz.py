class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        for i in range(1, n + 1, 1):
            if i/3 == 0 or i/5 == 0:
                print("fizz buzz")
            elif i/3 == 0:
                print("fizz")
            elif i/5 == 5:
                print("buzz")
            else:
                print(i)
            return
