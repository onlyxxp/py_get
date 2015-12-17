from src import _code_guess
from src import _code_verify
from src import _url_
from src import _ip_

__author__ = 'xxp'

# code = "146c7f0bae8ac4c6"
code = "a6*b8f4c981*577a"

def main():
    result_list = _code_guess.guess_full_codes(code)

    print(len(result_list))

    # result_list = ["a6*b8f4c981*577a"]
    _code_verify.get_responses(result_list, _url_.get_url())

main()