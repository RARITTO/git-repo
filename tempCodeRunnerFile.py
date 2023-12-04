def printboard (xstate ,ystate):
    data0 = 'X' if xstate[0] else ('O'if ystate[0] else 0)
    data1 = 'X' if xstate[1] else ('O'if ystate[1] else 1)
    data2 = 'X' if xstate[2] else ('O'if ystate[2] else 2)
    data3 = 'X' if xstate[3] else ('O'if ystate[3] else 3)
    data4 = 'X' if xstate[4] else ('O'if ystate[4] else 4)
    data5 = 'X' if xstate[5] else ('O'if ystate[5] else 5)
    data6 = 'X' if xstate[6] else ('O'if ystate[6] else 6)
    data7 = 'X' if xstate[7] else ('O'if ystate[7] else 7)
    data8 = 'X' if xstate[8] else ('O'if ystate[8] else 8)
    print(f' {data0}| {data1} | {data2}')
    print( '--|---|--') 
    print(f' {data3}| {data4} | {data5}')
    print( '--|---|--')
    print(f' {data6}| {data7} | {data8}')

xstate = [0,0,0,0,0,0,0,0,0]
ystate = [0,0,0,0,0,0,0,0,0]

print(printboard(xstate , ystate))