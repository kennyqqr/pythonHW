double_digit_evens = [e*2 for e in range(1,14)]
double_digit_odds = {e*2+1 for e in range(5, 50)}
dic_digit = {e: e*10 for e in range(1, 11)}

"""test doc strings"""
print('evens:' + str(double_digit_evens))
print('odds:' + str(double_digit_odds))
print('dictionary:' + str(dic_digit))
