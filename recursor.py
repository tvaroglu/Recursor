class Recursor:
    def test_func(actual, expected):
        if actual == expected:
            return f"PASSED: expected '{expected}', and got '{actual}'"
        return f"FAILED: expected '{expected}', but got '{actual}'"

    def countdown(number):
        #base case
        if number < 0:
            #if no more numbers to count down, return number
            return number
        #recursive case
        print(number)
        #print the current number, and call the function recursively decremented by one
        return Recursor.countdown(number - 1)

    #tail call optimized
    def get_sum(numbers, sum=0):
        #base case
        if len(numbers) == 0:
            return sum
        #recursive case
        current_num = numbers.pop(0)
        return Recursor.get_sum(numbers, sum + current_num)

    #tail call optimized
    def factorial(number, product=1):
        #base case
        if number == 1:
            return product
        #recursive case
        return Recursor.factorial(number - 1, product * number)

    #tail call optimized
    def reverse_string(string, reversed=''):
        #base case
        if len(string) == 0:
            return reversed
        #recursive case
        return Recursor.reverse_string(string[0:-1], reversed + string[-1])

    #tail call optimized
    def power(base, exponent, product=1):
        #base case
        if exponent == 0:
            return product
        #recursive case
        return Recursor.power(base, exponent - 1, base * product)

    #tail call optimized
    def is_palindrome(string, reversed=''):
        #base case
        if len(string) <= 1 or string == reversed:
            return True
        #recursive case
        if string[0] == string[len(string) - 1]:
            return Recursor.is_palindrome(string[1:-1], reversed + string[-1])
        return False

    #tail call optimized
    def find_next_palindrome(number, result=0):
        #base case
        if number == int(Recursor.reverse_string(str(number))):
            result = number
            return result
        #recursive case
        return Recursor.find_next_palindrome(number + 1, result)

    #tail call optimized
    def palindromic_sum(number, collector=[]):
        if number <= 200:
            while number < 201:
                number += 1
            return Recursor.palindromic_sum(number, collector)
        elif len(collector) == 25:
            return collector
        else:
            sum = number + int(''.join(reversed(str(number))))
            if sum == int(''.join(reversed(str(sum)))) and sum > 1000:
                collector.append(number)
            return Recursor.palindromic_sum(number + 1, collector)

    def flattener(list_of_lists):
        output_list = []
        for l in list_of_lists:
            if type(l) != list:
                output_list.append(l)
            else:
                output_list += Recursor.flattener(l)
        return output_list

    # tail call optimized
    def nth_fibonnaci(number, memo={}):
        if number in memo:
            return memo[number]
        elif number <= 2:
            return 1
        memo[number] = Recursor.nth_fibonnaci(number - 1, memo) + Recursor.nth_fibonnaci(number - 2, memo)
        return memo[number]

    # tail call optimized
    def valid_grid_traveler_combos(num_rows, num_cols, memo={}):
        # can only travel down or right across the grid
        if num_cols < num_rows:
            formatted = f'{num_cols}x{num_rows}'
        formatted = f'{num_rows}x{num_cols}'
        if formatted in memo:
            return memo[formatted]
        elif num_rows == 0 or num_cols == 0:
            return 0
        elif num_rows == 1 or num_cols == 1:
            return 1
        memo[formatted] = Recursor.valid_grid_traveler_combos(num_rows - 1, num_cols, memo) \
         + Recursor.valid_grid_traveler_combos(num_rows, num_cols - 1, memo)
        return memo[formatted]

    # tail call optimized
    def can_sum(target_sum, nums_list, memo={}):
        if target_sum in memo:
            return memo[target_sum]
        elif target_sum == 0:
            return True
        elif target_sum < 0:
            return False
        for num in nums_list:
            delta = target_sum - num
            if Recursor.can_sum(delta, nums_list, memo):
                return True
            memo[target_sum] = False
        return memo[target_sum]

    # tail call optimized
    def how_sum(target_sum, nums_list, memo={}):
        if target_sum in memo:
            return memo[target_sum]
        elif target_sum == 0:
            return []
        elif target_sum < 0:
            return None
        for num in nums_list:
            delta = target_sum - num
            result = Recursor.how_sum(delta, nums_list, memo)
            if result is not None:
                result = [*result, num]
                result.sort()
                return result
            memo[target_sum] = None
        return memo[target_sum]

    # tail call optimized
    def best_sum(target_sum, nums_list, memo={}):
        if target_sum in memo:
            return memo[target_sum]
        elif target_sum == 0:
            return []
        elif target_sum < 0:
            return None
        shortest_combo = None
        for num in nums_list:
            delta = target_sum - num
            result = Recursor.best_sum(delta, nums_list, memo)
            if result is not None:
                current_combo = [*result, num]
                if shortest_combo is None or len(current_combo) < len(shortest_combo):
                    shortest_combo = current_combo
                    shortest_combo.sort()
                memo[target_sum] = shortest_combo
        return shortest_combo


# test cases
print('countdown:')
Recursor.countdown(3)
print('\n')

print('get_sum:')
print(Recursor.test_func(Recursor.get_sum([1, 2, 3, 4]), 10))
print('\n')

print('factorial:')
print(Recursor.test_func(Recursor.factorial(5), 120))
print('\n')

print('reverse_string:')
print(Recursor.test_func(Recursor.reverse_string('Ariel'), 'leirA'))
print('\n')

print('power:')
print(Recursor.test_func(Recursor.power(2, 4), 16))
print(Recursor.test_func(Recursor.power(8, 5), 32768))
print('\n')

print('is_palindrome:')
print(Recursor.test_func(Recursor.is_palindrome('racecar'), True))
print(Recursor.test_func(Recursor.is_palindrome('kayak'), True))
print(Recursor.test_func(Recursor.is_palindrome('a'), True))
print(Recursor.test_func(Recursor.is_palindrome('library'), False))
print(Recursor.test_func(Recursor.is_palindrome('dngojkafnghkoasng'), False))
print('\n')

print('find_next_palindrome:')
print(Recursor.test_func(Recursor.find_next_palindrome(100), 101))
print(Recursor.test_func(Recursor.find_next_palindrome(283), 292))
print('\n')

print('palindromic_sum:')
print(Recursor.palindromic_sum(0))
print(Recursor.test_func(len(Recursor.palindromic_sum(0)), 25))
print('\n')

print('flattener:')
print(Recursor.test_func(Recursor.flattener([1, 2, 3, [[4], 5], [[[6]]]]), [1, 2, 3, 4, 5, 6]))
print(Recursor.test_func(Recursor.flattener(["hi", "this is", [[["string"], "that is very"], [[[["nested"]]]]]]), ["hi", "this is", "string", "that is very", "nested"]))
print('\n')

print('nth_fibonnaci:')
print(Recursor.test_func(Recursor.nth_fibonnaci(2), 1))
print(Recursor.test_func(Recursor.nth_fibonnaci(6), 8))
print(Recursor.test_func(Recursor.nth_fibonnaci(7), 13))
print(Recursor.test_func(Recursor.nth_fibonnaci(8), 21))
print(Recursor.test_func(Recursor.nth_fibonnaci(50), 12586269025))
print('\n')

print('valid_grid_traveler_combos:')
print(Recursor.test_func(Recursor.valid_grid_traveler_combos(0, 1), 0))
print(Recursor.test_func(Recursor.valid_grid_traveler_combos(1, 0), 0))
print(Recursor.test_func(Recursor.valid_grid_traveler_combos(0, 2), 0))
print(Recursor.test_func(Recursor.valid_grid_traveler_combos(2, 0), 0))
print(Recursor.test_func(Recursor.valid_grid_traveler_combos(0, 0), 0))
print(Recursor.test_func(Recursor.valid_grid_traveler_combos(1, 1), 1))
print(Recursor.test_func(Recursor.valid_grid_traveler_combos(1, 3), 1))
print(Recursor.test_func(Recursor.valid_grid_traveler_combos(3, 1), 1))
print(Recursor.test_func(Recursor.valid_grid_traveler_combos(2, 3), 3))
print(Recursor.test_func(Recursor.valid_grid_traveler_combos(3, 2), 3))
print(Recursor.test_func(Recursor.valid_grid_traveler_combos(3, 3), 6))
print(Recursor.test_func(Recursor.valid_grid_traveler_combos(18, 18), 2333606220))
print('\n')

print('can_sum:')
print(Recursor.test_func(Recursor.can_sum(7, [2, 3]), True))
print(Recursor.test_func(Recursor.can_sum(7, [5, 3, 4, 7]), True))
print(Recursor.test_func(Recursor.can_sum(7, [2, 4]), False))
print(Recursor.test_func(Recursor.can_sum(8, [2, 3, 5]), True))
print(Recursor.test_func(Recursor.can_sum(300, [7, 14]), False))
print('\n')

print('how_sum:')
print(Recursor.test_func(Recursor.how_sum(7, [2, 3]), [2, 2, 3]))
print(Recursor.test_func(Recursor.how_sum(7, [5, 3, 4, 7]), [3, 4]))
print(Recursor.test_func(Recursor.how_sum(7, [2, 4]), None))
print(Recursor.test_func(Recursor.how_sum(8, [2, 3, 5]), [3, 5]))
print(Recursor.test_func(Recursor.how_sum(0, [1, 2, 3]), []))
print(Recursor.test_func(Recursor.how_sum(300, [7, 14]), None))
print('\n')

print('best_sum:')
print(Recursor.test_func(Recursor.best_sum(7, [2, 4]), None))
print(Recursor.test_func(Recursor.best_sum(7, [5, 3, 4, 7]), [7]))
print(Recursor.test_func(Recursor.best_sum(8, [2, 3, 5]), [3, 5]))
print(Recursor.test_func(Recursor.best_sum(0, [1, 2, 3]), []))
print(Recursor.test_func(Recursor.best_sum(100, [1, 2, 5, 25]), [25, 25, 25, 25]))
print('\n')
