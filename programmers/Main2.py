def solution(a, b):
    days=[31,29,31,30,31,30,31,31,30,31,30,31] #윤년이라 가정
    weeks=['FRI','SAT','SUN','MON','TUE','WED','THU']
    day = sum(days[0:a-1])+b
    n = day%7-1
    return weeks[n]
