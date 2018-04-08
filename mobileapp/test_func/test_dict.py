def tests_yield():
    meta_data={
        'test':'tests1'
    }
    for one_article in ['num is {}'.format(str(i)) for i in range(1,20)]:
        nim_str=one_article
        data_in_board = {
            'url':nim_str
        }
        meta_data.update(data_in_board)
        yield {
            'data':meta_data,
            'url':nim_str
        }


data_list=[]

for onedata in tests_yield():
    if len(data_list)<8:
        data_list.append(onedata)
    else:
        print(data_list)
        data_list=[]


