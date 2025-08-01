import random
sonlar = [1,2,3,4,5,6,7,8,9,10]
tasodif_son = random.choice(sonlar)
print(" 1 dan 10 gacha son o'yladim topa olasanmi?")
javob2 = str(input())
javoblar_soni = 0
if javob2 == "xa":
    for i in sonlar:
        javob1=int(input("o'ylagan sonimni kiriting"))
        javoblar_soni += 1
        if javob1 > tasodif_son:
            print("kechirasiz siz kattaroq son aytyapsiz")

        elif javob1 < tasodif_son:
            print("kechirasiz siz kichikroq son o'yladingiz")

        elif javob1 == tasodif_son:

            print(f"tabriklayman siz {javoblar_soni} ta urinishda toptingiz")
            javoblar_soni1 = 0
            print("Kel endi sen o'ylaysan men topaman 1 dan 10 gacha oraliqda son o'ylang")
            javob5 = str(input("O'yladingizmi? "))
            for i in sonlar:
                javoblar_soni1 = javoblar_soni1 + 1

                javob3 = ["xa","+","-"]
                if javob5 == "xa":
                    tasodif_son1 = random.choice(sonlar)
                    print(f"o'ylagan soning {tasodif_son1} shumi?")
                    print("agar o'ylagan soningizdan katta bo'lsa + kiriting",
                          "agar o'ylagan soningizdan kichik bo'lsa - kiriting")
                    javob4 = str(input())
                    if javob4 == javob3[0]:
                        if javoblar_soni>javoblar_soni1:
                            print(f"Tabriklaymiz siz {javoblar_soni1} urinishda toptim va O'yinda yutdim")
                            break

                        elif javoblar_soni<javoblar_soni1:
                            print(f"Tabriklaymiz siz {javoblar_soni1} urinishda toptim va O'yinda siz yutdingiz")
                            break


                    elif javob4 == javob3[1]:
                        tasodif_son1 = random.choice(sonlar)
                    elif javob4 == javob3[1]:
                        tasodif_son1 = random.choice(sonlar)
