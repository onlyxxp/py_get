from src import m_code_guess
from src import m_code_verify
from src import m_url
from src import m_ip

__author__ = 'xxp'

# code = "146c7f0bae8ac4c6"
code = "a6*b8f4c981*577a"

def main():
    result_list = m_code_guess.guess_full_codes(code)

    print(len(result_list))

    # result_list = ["a6*b8f4c981*577a"]
    m_code_verify.get_responses(result_list, m_url.get_url())

main()