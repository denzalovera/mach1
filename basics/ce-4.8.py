furniture = ['table', 'chair', 'cabinet', 'desk', 'couch']
x = 'cabinet'
for i in furniture:
    if i == x:
        continue
    print(i)

i = 1

###
#
# while i <= 15:
#     if i >= 15:
#         print("i is no longer less than 15")
#         break
#     print(i)
#     i += 1
#
#
###


while i < 15:
    print(i)
    i += 1
else:
    print("i is no longer less than 15")

