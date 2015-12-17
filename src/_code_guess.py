__author__ = 'xxp'

# default_candidates1 = ['a', 'b', 'c', 'd', 'e', 'f']
# default_candidates2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
default_candidates1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
default_candidates2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
KEY = '*'
CODE_LEN = 16


def guess_full_codes(origin_codes):
    codeLength = len(origin_codes)
    result_list = []
    # print(codeLength)
    if codeLength < CODE_LEN:
        for i in range(0, codeLength - 1, 1):
            fill_to_full_len = origin_codes[0:i] + KEY + origin_codes[i:codeLength]
            # print(fill_to_full_len)
            sub_result_list = replace(fill_to_full_len)
            for s in sub_result_list:
                result_list.append(s)
    else:
        sub_result_list = replace(origin_codes)
        for s in sub_result_list:
            result_list.append(s)
    return result_list


def replace_key_to_candidate(codes, candidate):
    key_index = codes.index(KEY)
    before = codes[:key_index]
    end = codes[(key_index + 1):]
    replaced = before + candidate + end
    return replaced


def replace(tile_codes):
    codes = str(tile_codes)
    result_list = []

    if len(codes.split(KEY)) < 2:
        result_list.append(codes)
        return result_list

    for c in default_candidates1:
        result1 = str(replace_key_to_candidate(codes, c))
        # print("replace : " + result1)
        if len(result1.split(KEY)) > 1:
            for c2 in default_candidates2:
                result2 = str(replace_key_to_candidate(result1, c2))
                result_list.append(result2)
        else:
            result_list.append(result1)
    return result_list