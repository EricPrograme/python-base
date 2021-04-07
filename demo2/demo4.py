# Author: hmchen
# DATE  : 2021/3/20 18:58


list2 = [{'module': 'bms-server', 'versiontag': 'bms-ui'},
         {'module': 'bms-server', 'versiontag': 'bms-ui-server'},
         {'module': 'bms-server', 'versiontag': 'bms-456'},
         {'module': 'bds-server', 'versiontag': 'bds-server'},
         {'module': 'pca-server', 'versiontag': 'pca-server'},
         {'module': 'bds-server', 'versiontag': 'bds-456r'}]

dict = {'module': 'bms-server', 'versiontag': 'bms-ui'}
str = dict.values()
print(str)

version_dict = {}
for k in list2:
    module = k.get('module')
    versionTag = k.get('versiontag')
    if module in version_dict.keys():
        list3 = list(version_dict.get(module))
        list3.append(versionTag)
        # version_dict[module].values()
        # list.append(versionTag)
        version_dict[module] = list3

    else:
        list3 = []
        list3.append(versionTag)
        version_dict[module] = list3

print(version_dict)
