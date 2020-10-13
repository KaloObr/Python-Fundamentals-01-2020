# nums = list(map(int, input().split('.')))
#
# nums[2] += 1
#
# if nums[2] >= 10:
#     nums[2] = 0
#     nums[1] += 1
#
# if nums[1] >= 10:
#     nums[1] = 0
#     nums[0] += 1
#
#
# print('.'.join(map(str, nums)))
#

version = int(input().replace('.', ''))
new_version = version + 1

print('.'.join(str(new_version)))

