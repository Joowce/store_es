import requests
import json
fp = open('input/store_201712_01.csv', 'r')
index = 'store'
url = 'http://localhost:9200/{}/_doc'.format(index)
query = {'pipeline': 'parse_store'}

# fields = ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd','indsLclsNm',
#           'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd',
#           'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd',
#           'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm',
#           'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno',
#           'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo',
#           'hoNo', 'lon', 'lat']
# templates = map(lambda x: '%{{DATA:{}}}'.format(x), fields)
# print(",".join(templates))
file_iter = iter(fp)
print(next(file_iter))
for line in file_iter:
    r = requests.post(url,params=query, json={'store': line.replace('\"', '\'')})

print('-' * 8 + 'done' + '-' * 8)