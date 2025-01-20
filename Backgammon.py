
import random

#player1 = [0,2,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,3,0,5,0,0,0,0,0,0,0,0,0,0,0]  # تعداد مهره ها در هر جایگاه تخته در شروع بازی (بازیکن اول)
player1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0]
player2 = [0,2,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,3,0,5,0,0,0,0,0,0,0,0,0,0,0]  #  تعداد مهره ها در هر جایگاه تخته در شروع بازی (بازیکن دوم)
DiceSwitch = False  # برای کنترل انداختن تاس
player1name = input("بازیکن اول لطفا نام خود را وارد کنید: ")
player2name = input("بازیکن دوم لطفا نام خود را وارد کنید: ")
def show(DiceSwitch):  # برای نمایش دادن صفحه تخته و شماره های تاس
    space = 40
    print("B    A   ", "-"*50, "  A    B")  # برای نمایش خط ابتدتیی تخته و عنوان اعداد جایگاه های هر بازیکن در کنار سطر های آن
    for i in range(1,13):   # برای نمایش سطر به سطر جایگاه های تخته
        if i<4:             # برای تنظیم فواصل وقتی شماره هر دو جایگاه دو رقمی است
            print(13-i, " ", 12+i, "  |_", chr(111)*player1[12+i],chr(174)*player2[13-i], " "*(space-(player1[12+i]+player2[13-i]+player1[13-i]+player2[12+i])),\
                  chr(111)*player1[13-i], chr(174)*B[12+i], "_|  ", 13-i, " ", 12+i)
        else:
            print(13-i, "  ", 12+i, "  |_", chr(111)*player1[12+i],chr(174)*player2[13-i], " "*(space-(player1[12+i]+player2[13-i]+player1[13-i]+player2[12+i])),\
                  chr(111)*player1[13-i], chr(174)*player2[12+i], "_|  ", 13-i, "  ", 12+i)
        if i == 6 :  # برای نمایش خط وسط در صفحه تخته
            if DiceSwitch :  # آیا تاس را بیاندازد یا خیر
                if player1[0] > 0 or player2[0] > 0:  # نمایش مهره های زده شده
                    print(" "*9,"-"*10," ", player1[0]*chr(111), " ","-"*(26-player1[0]-player2[0])," ", player2[0]*chr(174), " ", "-"*10, end=" ")
                else:
                    print(" "*9, "-" * 50, end=" ")
                print(" "*25, "->", random.randint(1, 6), "<-", " "*10, "->", random.randint(1, 6), "<-")  # انداختن تاس
                DiceSwitch = False
            else:
                if player1[0] > 0 or player2[0] > 0:
                    print(" "*9,"-"*10," ", player1[0]*chr(111), " ","-"*(26-player1[0]-player2[0])," ", player2[0]*chr(174), " ", "-"*10)
                else:
                    print(" "*9, "-" * 50)
                DiceSwitch = True
    print(" "*9, "-"*50)  # نمایش خط پایانی انتهای تخته
    #print(" ")
    SumPlayer1 = 0
    SumPlayer2 = 0
    for i in range(25,31):
        SumPlayer1 = SumPlayer1 + player1[i]
        SumPlayer2 = SumPlayer2 + player2[i]
    print(" "*9 ,SumPlayer1, ": ", chr(111), " "*36, chr(174), ": ", SumPlayer2 )
    return (DiceSwitch)

A = player1
B = player2
CurrentPlayer = "A"
DiceSwitch = show(DiceSwitch)
UserOrder = input("برای نمایش عدد تاس لطفا کلید t  فشار دهید و برای خارج شدن از برنامه کلید e را فشار دهید: ")
while UserOrder == "t":  # اجرای بازی تا زمانی که تاس انداخته شود
    DiceSwitch = show(DiceSwitch)
    if CurrentPlayer == "A":
        A = player1
        B = player2
        TPlayer1Name = player1name
        CurrentPlayer = "B"
    else:
        A = player2
        B = player1
        TPlayer1Name = player2name
        CurrentPlayer = "A"
    WrongMove = True   # سوییچ برای حرکت اشتباه
    WrongMoveaPairing1 = True   # سوییچ اول در حالت جفت برای دو حرکت اول
    WrongMoveaPairing2 = True   # سوییچ دوم در حالت جفت برای دو حرکت دوم
    while WrongMove:
        if WrongMoveaPairing1:
            num1 = int(input("{} جان لطفا حرکت اول را وارد کنید:".format(TPlayer1Name)))
            num2 = int(input("{} جان لطفا حرکت دوم را وارد کنید:".format(TPlayer1Name)))
            jaygah_1 = int((num1 / 10))
            tas_1 = (num1 % 10)
            jaygah_2 = int((num2 / 10))
            tas_2 = (num2 % 10)

        if tas_1 == tas_2 and WrongMoveaPairing2:
            num3 = int(input("{} جان لطفا حرکت سوم را وارد کنید:".format(TPlayer1Name)))
            num4 = int(input("{} جان لطفا حرکت چهارم را وارد کنید:".format(TPlayer1Name)))
            jaygah_3 = int((num3 / 10))
            tas_3 = (num3 % 10)
            jaygah_4 = int((num4 / 10))
            tas_4 = (num4 % 10)
        if (A[0] > 1 and jaygah_1 > 0) or (A[0] > 1 and jaygah_2 > 0):  # اگر بیش از یک مهره بیرون باشد باید اجرا میشود
            print("* {} جان ابتدا مهره های بیرونی خود را باید وارد بازی کنید *".format(TPlayer1Name))
            WrongMoveaPairing2 = True
        else:
            if A[0] == 1 and (jaygah_1 != 0 and jaygah_2 != 0):  # اگر تنها یک مهره بیرون باشد اجرا میشود.
                print("* {} جان ابتدا مهره بیرونی خود را باید وارد بازی کنید *".format(TPlayer1Name))
                WrongMoveaPairing2 = True
            else:
                if A[jaygah_1] == 0:
                    print("* {} جان در جایگاه اول مهره ای برای حرکت دادن ندارید. *".format(TPlayer1Name))
                    WrongMoveaPairing2 = True
                else:
                    if A[jaygah_2] == 0 and (jaygah_1 + tas_1) != jaygah_2:
                        print("* {} جان در جایگاه دوم مهره ای برای حرکت دادن ندارید. *".format(TPlayer1Name))
                        WrongMoveaPairing2 = True
                    else:
                        SumList = 0
                        for i in range(19):   # برای ارزیابی خالی بودن 19 جایگاه اول جهت برداشتن مهره ها
                            SumList = SumList + A[i]
                        if (jaygah_1 + tas_1 > 24 or jaygah_2 + tas_2 > 24) and SumList > 0:
                            print("* {} جان فعلا نمیتوانید مهره های خود را خارج کنید *".format(TPlayer1Name))
                            WrongMoveaPairing2 = True
                        else:
                            if B[(25 - jaygah_1) - tas_1] > 1 or B[(25 - jaygah_2) - tas_2] > 1:
                                print("* {} جان مهره های حریف در این جایگاه قرار دارد. *".format(TPlayer1Name))
                                WrongMoveaPairing2 = True
                            else:
                                if B[(25 - jaygah_1) - tas_1] == 1:  # عملیات تغییر لیست هنگام زدن مهره حریف در جایگاه 1
                                    B[(25 - jaygah_1) - tas_1] = B[(25 - jaygah_1) - tas_1] - 1
                                    B[0] = B[0] + 1
                                if B[(25 - jaygah_2) - tas_2] == 1:  # عملیات تغییر لیست هنگام زدن مهره حریف در جایگاه 2
                                    B[(25 - jaygah_2) - tas_2] = B[(25 - jaygah_2) - tas_2] - 1
                                    B[0] = B[0] + 1
                                A[jaygah_1] = A[jaygah_1] - 1  # عملیات تغییر لیست هنگام حرکت دادن مهره ها
                                A[jaygah_1 + tas_1] = A[jaygah_1 + tas_1] + 1
                                A[jaygah_2] = A[jaygah_2] - 1
                                A[jaygah_2 + tas_2] = A[jaygah_2 + tas_2] + 1
                                if not WrongMoveaPairing1:
                                    WrongMoveaPairing2 = False
                                if tas_1 == tas_2 and WrongMoveaPairing1:
                                    jaygah_1 = jaygah_3
                                    tas_1 = tas_3
                                    jaygah_2 = jaygah_4
                                    tas_2 = tas_4
                                    WrongMoveaPairing1 = False
                                    WrongMoveaPairing2 = False
                                else:
                                    DiceSwitch = show(DiceSwitch)
                                    WrongMove = False
                                SumList = 0
                                for i in range(25):  # برای ارزیابی خالی بودن 19 جایگاه اول جهت برداشتن مهره ها
                                    SumList = SumList + A[i]
                                if SumList == 0:
                                    print("* {} جان شما برنده شده اید. *".format(TPlayer1Name))
                                    break

    UserOrder = input("برای نمایش عدد تاس لطفا کلید t  فشار دهید و برای خارج شدن از برنامه کلید e را فشار دهید: ")