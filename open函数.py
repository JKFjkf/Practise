#file=open('C://Users/hp/Desktop/txet.txt','w')
#file.write('hello python')

def text_creat(name,msg):
    desktop_path = 'C://Users/hp/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    print('Finish')
    return msg
#text_creat('hello','hello world')

def text_fliter(word,censored_word = 'lame',changed_wold = 'awesome'):
    word = word.replace(censored_word,changed_wold)
    return word
#text_fliter('python is lame!')

if __name__ == '__main__':
    name = input("请输入名字：\n")
    word = input("请输入信息：\n")
    msg = text_fliter(word)
    text_creat(name,msg)
