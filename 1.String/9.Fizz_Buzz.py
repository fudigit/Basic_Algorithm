class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        results = []
        for i in range(1, n + 1, 1):
            if i%3 == 0 and i%5 == 0:
                results.append("fizz buzz")
            elif i%3 == 0:
                results.append("fizz")
            elif i%5 == 0:
                results.append("buzz")
            else:
                results.append(str(i))
        return results
