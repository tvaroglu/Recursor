class Recursor:
    def __init__(self, can_sum_memo={}, how_sum_memo={}, best_sum_memo={}):
        self.can_sum_memo = can_sum_memo
        self.how_sum_memo = how_sum_memo
        self.best_sum_memo = best_sum_memo

    def clear_all_memos(self, can_sum_memo={}, how_sum_memo={}, best_sum_memo={}):
        self.can_sum_memo = can_sum_memo
        self.how_sum_memo = how_sum_memo
        self.best_sum_memo = best_sum_memo

    def countdown(self, number):
        # base case
        if number < 0:
            # if no more numbers to count down, return number
            return number
        # recursive case
        print(number)
        # print the current number, and call the function recursively decremented by one
        return self.countdown(number - 1)

    # tail call optimized
    def get_sum(self, numbers, sum=0):
        # base case
        if len(numbers) == 0:
            return sum
        # recursive case
        current_num = numbers.pop(0)
        return self.get_sum(numbers, sum + current_num)

    # tail call optimized
    def factorial(self, number, product=1):
        # base case
        if number == 1:
            return product
        # recursive case
        return self.factorial(number - 1, product * number)

    # tail call optimized
    def reverse_string(self, string, reversed=''):
        # base case
        if len(string) == 0:
            return reversed
        # recursive case
        return self.reverse_string(string[0:-1], reversed + string[-1])

    # tail call optimized
    def power(self, base, exponent, product=1):
        # base case
        if exponent == 0:
            return product
        # recursive case
        return self.power(base, exponent - 1, base * product)

    # tail call optimized
    def is_palindrome(self, string, reversed=''):
        # base case
        if len(string) <= 1 or string == reversed:
            return True
        # recursive case
        if string[0] == string[len(string) - 1]:
            return self.is_palindrome(string[1:-1], reversed + string[-1])
        return False

    # tail call optimized
    def find_next_palindrome(self, number, result=0):
        # base case
        if number == int(self.reverse_string(str(number))):
            return result + 1
        # recursive case
        return self.find_next_palindrome(number + 1, number)

    # tail call optimized
    def palindromic_sum(self, number, collector=[]):
        if number <= 200:
            while number < 201:
                number += 1
            return self.palindromic_sum(number, collector)
        elif len(collector) == 25:
            return collector
        else:
            sum = number + int(''.join(reversed(str(number))))
            if sum == int(''.join(reversed(str(sum)))) and sum > 1000:
                collector.append(number)
            return self.palindromic_sum(number + 1, collector)

    # tail call optimized
    def flattener(self, list_of_lists, output_list=[]):
        if list_of_lists == []:
            return output_list
        current_elem = list_of_lists[0]
        if type(current_elem) == list:
            output_list = self.flattener(current_elem, output_list) + self.flattener(list_of_lists[1:], output_list)
            return output_list
        output_list = [current_elem] + self.flattener(list_of_lists[1:], output_list)
        return output_list

    # tail call optimized
    def nth_fibonnaci(self, number, memo={}):
        if number in memo:
            return memo[number]
        elif number <= 2:
            return 1
        memo[number] = self.nth_fibonnaci(number - 1, memo) + self.nth_fibonnaci(number - 2, memo)
        return memo[number]

    # tail call optimized
    def valid_grid_traveler_combos(self, num_rows, num_cols, memo={}):
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
        memo[formatted] = self.valid_grid_traveler_combos(num_rows - 1, num_cols, memo) \
         + self.valid_grid_traveler_combos(num_rows, num_cols - 1, memo)
        return memo[formatted]

    # tail call optimized
    def can_sum(self, target_sum, nums_list):
        if target_sum in self.can_sum_memo:
            return self.can_sum_memo[target_sum]
        elif target_sum == 0:
            return True
        elif target_sum < 0:
            return False
        for num in nums_list:
            delta = target_sum - num
            if self.can_sum(delta, nums_list):
                return True
            self.can_sum_memo[target_sum] = False
        return False

    # tail call optimized
    def how_sum(self, target_sum, nums_list):
        if target_sum in self.how_sum_memo:
            return self.how_sum_memo[target_sum]
        elif target_sum == 0:
            return []
        elif target_sum < 0:
            return None
        for num in nums_list:
            delta = target_sum - num
            result = self.how_sum(delta, nums_list)
            if result is not None:
                result = [*result, num]
                result.sort()
                return result
            self.how_sum_memo[target_sum] = None
        return None

    # tail call optimized
    def best_sum(self, target_sum, nums_list):
        if target_sum in self.best_sum_memo:
            return self.best_sum_memo[target_sum]
        elif target_sum == 0:
            return []
        elif target_sum < 0:
            return None
        shortest_combo = None
        for num in nums_list:
            delta = target_sum - num
            result = self.best_sum(delta, nums_list)
            if result is not None:
                current_combo = [*result, num]
                if shortest_combo is None or len(current_combo) < len(shortest_combo):
                    shortest_combo = current_combo
                    shortest_combo.sort()
                    self.best_sum_memo[target_sum] = shortest_combo
        return shortest_combo

    def merge_sort(self, list):
        return list
