class Solution:
    def isNumber(self, s):
        state = [
              {},
              {'blank': 1, 'sign': 2, 'digit':3, '.':4},
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]
        current_state = 1 
        for n in s:
            if n <= '9' and n >= '0':
                next = 'digit'
            elif n in ['-', '+']:
                next = 'sign'
            elif n == ' ':
                next = 'blank'
            if next not in state[current_state]:
                return False
            current_state = state[current_state][next]
        if current_state not in [3, 5, 8, 9]:
            return False
        return True
