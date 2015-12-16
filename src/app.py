from src import guess
from src import multi_thread_verify

__author__ = 'xxp'

code = "a6*b8f4c981*577a"

def main():
    result_list = guess.guess_full_codes(code)

    print(len(result_list))
    # result_list = ["a6*b8f4c981*577a"]
    multi_thread_verify.get_responses(result_list)

main()