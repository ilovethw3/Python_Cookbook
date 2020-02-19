import random
import time
import linecache


def genertor_id():
    i = range(1, 1000000000)
    for a in i:
        yield str(a)


def genertor_name():
    i = random.randint(1,249298)
    name_list=linecache.getline('name.txt',i).strip().split(',')
    first_name=name_list[0]
    sex=name_list[1]
    full_name=name_list[2]
    return first_name,sex,full_name


def genertor_sex():
    i = random.choice(['男', '女'])
    return i


def genertor_address():
    i = random.randint(1,901305)
    address_list=linecache.getline('address.txt',i).strip().split(',')
    xingzhengma=address_list[0]
    address=address_list[3]
    return xingzhengma,address


def genertor_phone():
    list = ['139', '138', '137', '136', '135', '134', '159', '158', '157', '150', '151', '152', '188', '187', '182',
            '183', '184', '178', '130', '131', '132', '156', '155', '186', '185', '176', '133', '153', '189', '180',
            '181', '177']
    str = '0123456789'
    ##改写电话号码使用正则方式
    return (random.choice(list) + "".join(random.choice(str) for i in range(8)))

def genertor_birth():
    r=time.localtime(time.time() - random.uniform(0,1.5) * random.randint(100000000, 1000000000))
    birth=time.strftime("%Y%m%d", r)
    return birth

def genertor_cardid(xingzhengma,birth,sex):
    seq1 = random.randint(0, 9)
    seq2 = random.randint(0, 9)
    if sex == '男':
        n=random.choice([1,3,5,7,9])
    else:
        n=random.choice([0,2,4,6,8])
    cardid=xingzhengma+birth+str(seq1)+str(seq2)+str(n)
    digs=[int(i) for i in cardid]
    chk=['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2'][sum([int(digs[i]) * [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2][i] for i in range(17)]) % 11]
    return cardid+chk


def genertor_data(count,length):
    # 生成id
    _genertor_id = genertor_id()
    # 读取文件到内存
    with open('address.txt',mode='r',encoding='utf-8') as f:
        file=f.read()
        for c in range(count):
            # 生成id
            _table_values_id = next(_genertor_id)
            # 生成名字 生成性别
            first_name,sex,full_name=genertor_name()
            # 生成生日
            birth=genertor_birth()
            # 生成地址
            xingzhengma,address=genertor_address()
            # 生成手机
            phone=genertor_phone()
            # 生成cardid
            cardid=genertor_cardid(xingzhengma, birth, sex)

            table_values=[_table_values_id,full_name,sex,birth,address,phone,cardid]
            if len(table_values)<length:
                table_values.append(_table_values_id)
            yield table_values

