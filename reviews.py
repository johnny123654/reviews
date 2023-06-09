# 留言分析程式 練習
data = []
x = 0 
with open ('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		x += 1 # 快寫法 x = x + 1
		if x % 1000 == 0: # x與1000的餘數等於0
		    print (len(data))
print ('檔案讀取完了','總共有',len (data),'筆資料')

print(data[0])
#如何算出平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print ('平均是', sum_len / len(data) )

# 假設我們要篩選出長度小於100的留言
new = [] #建立一個新清單
for d in data: # 將data一筆一筆列出來
	if len(d) < 100:
		new.append(d)
print ('一共有 ', len(new) , '筆留言')
print (new[0]) #印出第0筆留言

# 篩選出含有good的留言
good = []
for d in data:
	if 'good' in (d):#if後慢一定會變是非題 true false
		good.append(d)
print('一共有' ,len(good) , '個留言含有good')
# 1.首先 先建立一個能開啟reviews.txt檔案的程式碼
# 2.將檔案存成f(隨便取)
# 3.利用for迴圈，將f 每次都讀取一行(line)
# 4.讀取之後，將之裝進一個清單，建立空清單data
# 5.每一行把他append(加進)data裡面
# 6.len 能夠求字串的長度或者清單的長度
# 7.如果只想印出第一筆資料，用[]中括號 ，清單都是從0開始
# 0是第一筆，1是第二筆
# 8. % 是餘數 
# 9.sun 是加總 