def iterateOverList (yourList: list):
    for iterateList in range(len(yourList)):
        print(yourList[iterateList], end=", ")
    print()

listOfNumber = [20,80,75,60,50,85,45,90]
listOfNumber.sort()
print(listOfNumber)


kelas1 = []
kelas2 = []
kelas3 = []
kelas4 = []
kelas5 = []
kelas6 = []
kelas7 = []
kelas8 = []
tempt = 2.875
# for index in range(8):
#     print(f"kelas {index + 1}: {tempt}")
#     tempt += 2.875
# for listRange in range(len(listOfNumber)):
#     if listOfNumber[listRange] < 45:
#         kelas1.append(listOfNumber[listRange])
#     elif listOfNumber[listRange] < 50:
#         kelas2.append(listOfNumber[listRange])
#     elif listOfNumber[listRange] < 55:
#         kelas3.append(listOfNumber[listRange])
#     elif listOfNumber[listRange] < 60:
#         kelas4.append(listOfNumber[listRange])
#     elif listOfNumber[listRange] < 65:
#         kelas5.append(listOfNumber[listRange])
#     elif listOfNumber[listRange] < 70:
#         kelas6.append(listOfNumber[listRange])
#     elif listOfNumber[listRange] < 75:
#         kelas7.append(listOfNumber[listRange])
#     else:
#         kelas8.append(listOfNumber[listRange])
#
#
# print(f"this is kelas 1 {len(kelas1)}")
# print(f"this is kelas 2 {len(kelas2)}")
# print(f"this is kelas 3 {len(kelas3)}")
# print(f"this is kelas 4 {len(kelas4)}")
# print(f"this is kelas 5 {len(kelas5)}")
# print(f"this is kelas 6 {len(kelas6)}")
# print(f"this is kelas 7 {len(kelas7)}")
# print(f"this is kelas 8 {len(kelas8)}")
#
# print(len(kelas1) + len(kelas2) + len(kelas3) + len(kelas4) + len(kelas5) + len(kelas6) + len(kelas7) + len(kelas8))
# variablePlaceHolder = 39.5

# for loopRange in range(4):
#     for loopClass in range(10):
#         variablePlaceHolder += 1
#         if loopClass == 5 - 1:
#             print(f"Nilai tengah = {variablePlaceHolder}")
# # print(max(listOfNumber))
