__author__ = 'xxp'

from src import code_guess
from src import code_verify

# code = "146c7f0bae8ac4c6"
code = "a6*b8f4c981*577a"

def main():
    result_list = code_guess.guess_full_codes(code)

    print(len(result_list))
    # result_list = ["a6*b8f4c981*577a"]
    code_verify.get_responses(result_list)

main()