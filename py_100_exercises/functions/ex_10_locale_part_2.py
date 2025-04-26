def region_code(locale):
    return locale.split('.')[0].split('_')[1]

print(region_code('en_US.UTF-8'))
print(region_code('en_GB.UTF-8'))
print(region_code('ko_KR.UTF-16'))