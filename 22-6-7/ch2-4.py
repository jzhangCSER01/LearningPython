'''
列表实现堆栈数据结构
'''

# example
songn = []
# add the song name
while(1):
    newsong = input('Enter the name of song(if end, enter -1):')
    if(newsong == '-1'):
        break
    else:
        newsong.replace(u'\xa0', '')    # 将不间断空白符 '\xa0' 替换为 ''
        songn.append(newsong)
# only keep 5 songs
while(len(songn) > 5):
    songn.pop()
print(songn)