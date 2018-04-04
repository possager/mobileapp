from mobileapp.items import MobileappItem



def standard(data):
    standard_item=MobileappItem()
    for i in data.keys():
        if i in standard_item.fields:
            standard_item[i]=data[i]

    return standard_item