def cal_kcal(eat):
    hanrabong_kcal = 0.5 * eat
    return hanrabong_kcal

eat = int(input("한라봉 몇g을 섭취하셨나요."))

print("한라봉 {}g은 {}kcal입니다.".format(eat, cal_kcal(eat)))

def cal_kcal(eat):
    strawberry_kcal = 0.34 * eat
    return strawberry_kcal

eat = int(input("딸기(설향) 몇g을 섭취하셨나요."))

print("딸기(설향) {}g은 {}kcal입니다.".format(eat, cal_kcal(eat)))

def cal_kcal(eat):
    banana_kcal = 0.77 * eat
    return banana_kcal

eat = int(input("바나나 몇g을 섭취하셨나요."))

print("바나나 {}g은 {}kcal입니다.".format(eat, cal_kcal(eat)))

def cal_kcal(eat):
    applemango_kcal = 0.57 * eat
    return applemango_kcal

eat = int(input("애플망고 몇g을 섭취하셨나요."))

print("애플망고 {}g은 {:.1f}kcal입니다.".format(eat, cal_kcal(eat)))
