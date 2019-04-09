#
# (C) blacktriangles 2019
# http://www.blacktriangles.com
#

def get_stats(data, units, w=30):

    new = round(data[-1], 2)
    last = round(data[-2], 2)
    percs = round(((new/last)-1) * 100, 2)
    minv = round(min(data), 2)
    maxv = round(max(data), 2)
    avg = round(sum(data) / len(data), 2)

    if percs > 0:
        percs = '+{0:.2f}'.format(percs)

    return F'''
  {new} {units} ({percs}%)
  Last: {last}
  Min: {minv}
  Max: {maxv}
  Avg: {avg}
'''
