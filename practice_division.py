## list 자료형
ori_list = ['abc', 789, 2.34, "def", 5]
add_list = [123, 'yong', 2]

print(ori_list)

# 1이상 3미만
print(ori_list[1:3])

# 3이상 모두
print(ori_list[3:])

# 정수 + 정수
print(ori_list[1] + add_list[0])

# 실수 + 정수
print(ori_list[2] + add_list[0])

# list + list
print(ori_list+add_list)

# 제곱 # 5 ** 2 = 25
print(ori_list[4] ** add_list[2])

# 몫 # 5 // 2 = 2
print(ori_list[4] // add_list[2])

# 나머지 # 5 % 2 = 1
print(ori_list[4] % add_list[2])

## dictionary 자료형
dictionary = {}
dictionary['one'] = "This is number of word"
dictionary[2] = 256

print(dictionary[2]);
print(dictionary['one']);
# print(dictionary['two']); # KeyError: 'two'
print(dictionary.keys());
print(dictionary.values());

# 산술연산자
# 비교연산자
# 할당연산자
# 논리연산자
# Bitwise 연산자
# 멤버쉽 연산자 # 좌측 Operand가 우측 컬렉션에 속해 있는지 체크
# Identity 연산자 # 두 객체의 메모리 위치 체크
