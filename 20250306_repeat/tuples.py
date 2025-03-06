# Кортеж - список, защищенный от замены элементов первого уровня

nums = [3, 5, 7]
nums[2] = 0
print(nums)
print("В списке можно заменять элемент: ", nums)
del nums[1]
print(nums)
print("В списке можно удалять элемент: ", nums)
nums.append(4)
print("В список можно дописать элемент: ", nums)
nums = (3, 5, 7)
# nums[2] = 0
# TypeError: 'tuple' object does not support item assignment
# del nums[1]
#TypeError: 'tuple' object doesn't support item deletion
# nums.append - нельзя присоединить
print(id(nums), nums)
nums += (4, )  # не ИЗМЕНЕНИЕ кортежа, а вычисление нового!
print(nums)
print(id(nums), nums)

# А на втором уровне уже все...
lists = ((1, 2, 3), [4, 5, 6])
#lists[0][0] = 111  # В кортеже нельзя, в списке - можно
lists[1][0] = 'kuku'
print(lists)

# Комод тот же, ящики те же, носки в них разные
