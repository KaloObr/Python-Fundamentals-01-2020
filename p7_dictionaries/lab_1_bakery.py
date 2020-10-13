def solution(raw_data):
    data = raw_data.split(' ')
    return {data[i]: int(data[i+1]) for i in range(0, len(data), 2)}

    # result = {}
    # for i in range(0, len(data), 2):
    #     key = data[i]
    #     value = data[i+1]
    #     result[key] = int(value)
    # return result



print(solution(input()))

