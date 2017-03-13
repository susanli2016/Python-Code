# Given your birthday and current date, caculate your age in days

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 \
       or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

def dateIsBefore(y1, m1, d1, y2, m2, d2):
    """
    Return True if y1-m1-d1 is before
    y2-m2-d2, otherwise return False
    """
    if y1 < y2:
        return True
    if y1 == y2:
        if m1 < m2:
            return True
        if m1 == m2:
            return d1 < d2
    return False

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = 0
    assert not dateIsBefore(y2, m2, d2, y1, m1, d1)
    while dateIsBefore(y1, m1, d1, y2, m2, d2):
        y1, m1, d1 = nextDay(y1, m1, d1)
        days+=1
    return days

def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

print(test())




            










        

















