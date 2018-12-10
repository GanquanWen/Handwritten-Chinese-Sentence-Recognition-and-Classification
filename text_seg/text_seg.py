import jieba


text1 = "年轻的卡拉小姐在结婚前夕被告知自己的身世"
print(text1)

seg_list = jieba.cut(text1, cut_all=False)

array1 = []
array1.append(",".join(seg_list))
#print(array1)

array2 = [x.split(",") for x in array1]
# print(array2)

while '' in array2[0]:
    array2[0].remove('')
print(array2)
	
#print("Default Mode: " + ",".join(seg_list))

