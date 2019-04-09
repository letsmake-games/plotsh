#
# (C) BLACKTRIANGLES 2019
# http://www.blacktriangles.com
#

import math

#
# utility functions ###########################################################
#

def _u_str(num):
    return '{0:.2f}'.format(num)

#
# plot raw ####################################################################
#

def plot_raw(title='', data=[], bar='▄', w=0, h=0):
    maxTitleLen = w-2
    if len(title) > maxTitleLen:
        title = title[:maxTitleLen]
    if len(title) < maxTitleLen:
        diff = maxTitleLen - len(title)
        diff = diff / 2
        partial = (diff % 1) > 0
        diff = int(diff)
        if partial:
            title = ' ' * diff + title + ' ' * (diff+1)
        else:
            title = ' ' * diff + title + ' ' * diff

    binSize = h-3
    if binSize <= 1:
        binSize = 5

    histo_data = [0] * binSize
    histo_min = [0] * binSize
    histo_max = [0] * binSize

    minv = min(data)
    maxv = max(data)
    binw = (maxv - minv) / float(binSize)

    for i in range(0, binSize-1):
        histo_min[i] = minv + (i * binw)
        histo_max[i] = minv + ((i + 1) * binw)

    histo_min[-1] = histo_max[-2]
    histo_max[-1] = max(maxv,histo_max[-2])

    for datum in data:
        added = False
        for i in range(0, binSize):
            if datum < histo_max[i]:
                histo_data[i] = histo_data[i] + 1
                added = True
                break

        if not added:
            histo_data[-1] = histo_data[-1] + 1

    result = []
    result.append('┌' + '─'*(w-2) + '┐' + '\n')
    result.append('│' +   title   + '│' + '\n')
    result.append('└' + '─'*(w-2) + '┘' + '\n')
    
    min_label_len = len(_u_str(maxv))
    max_label_len = len('{maxv}-{maxv}:'.format(maxv = _u_str(maxv)))
    max_histo_len = w - max_label_len

    minv = min(histo_data)
    maxv = max(histo_data)
    delta = maxv - minv
    csize = delta / max_histo_len

    for i in range(0, len(histo_data)):
        minl = _u_str(histo_min[i]).zfill(min_label_len)
        maxl = _u_str(histo_max[i]).zfill(min_label_len)
        result.append('%s-%s:' % (minl,maxl))
        v = int(math.floor(csize * histo_data[i]))
        result.append(bar * v)
        result.append('\n')

    return ''.join(result)
