def read():
    data = []
    count = 0
    with open('reviews.txt', 'r') as f:
        for line in f:
            data.append(line)
            count += 1
            if count % 1000 == 0:
                print(len(data))
    print('檔案讀取完了，總共有', len(data), '筆資料')
    print(data[0])
    return data

def count(filename):
    wc = {} # word_count
    for d in filename:
        words = d.strip().split()
        for word in words:
            if word not in wc:
                wc[word] = 1
            else:
                wc[word] += 1 # 新增一個key進入字典
    
    for word in wc:
        if wc[word] > 1000000:
            print('單字', word, '出現', wc[word], ' 次')
    return wc


def show(filename):
    while True:
        word = input('請輸入查詢的字: ')
        if word == 'q':
            print('See you.')
            break
        elif word in filename:
            print(word, '出現了過的次數為', filename[word], '次')
        else:
            print('這個字沒有出現過!')



def main():
    data = read()
    wc = count(data)
    show(wc)
main()

