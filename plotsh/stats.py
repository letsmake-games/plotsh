#
# (C) blacktriangles 2019
# http://www.blacktriangles.com
#

def get_stats(data, units):
    rep = {
        new: data[-1],
        last: data[-2],
        percs: round(((new/last)-1) * 100, 2),
        min: min(data),
        max: max(data),
        avg: sum(data) / len(data),
        units: units,
    }

    if rep.percs > 0:
        rep.percs = '+{0:.2f}'.format(rep.percs)

    return '''                                                                                                     
    Latest: %(new)s %(units)s (%(percs)s%%)\n
    Last: %(last)s\n
    Min: %(min)s\n
    Max: %(max)s\n
    Avg: %(avg)s\n
    ''' % data)
