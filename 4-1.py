print('蘋果店進出貨系統')
sell = 0
cus = []
while True:
    print('功能')
    print('1設定')
    print('2進貨')
    print('3出貨')
    print('4營業額統計')
    print('5庫存顯示')
    print('6結束系統')
    op = int(input('請輸入功能選項'))
    if op == 6:
        break
    elif op == 1:
        number = int(input('輸入蘋果數量'))
        price = int(input('蘋果單價'))
        print('蘋果目前有',number,'顆')
        print('蘋果一顆',price,'元')
    elif op == 2:
        applein = int(input('蘋果進貨數量'))
        number = applein + number
        print('蘋果目前有',number,'顆')
    elif op == 3:
        appleout = int(input('蘋果賣出數量'))
        print('應付',appleout*price,'元')
        number = number - appleout
        sell = sell + appleout
        print('蘋果目前有',number,'顆')
        cus.append(appleout)
    elif op == 4:
        for i in range(len(cus)):
            print(cus[i],'顆',cus[i]*price,'元')
        total = sell*price
        print('共賣了',sell,'顆')
        print('營業額',total,'元')
    elif op == 5:
        print('蘋果目前有',number,'顆')
    else:
        print('error')
        
        
        
        
        
        