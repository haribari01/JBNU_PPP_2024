import os
import pickle

DB_FILE = "money_control_db.pkl"

def read_db():
    if not os.path.exists(DB_FILE):
        return {"잔고": 400000, "식비": 0, "교통비": 0, "여가비": 0}   #기본세팅
    with open(DB_FILE, "rb") as f:
        return pickle.load(f)

def write_db(money_db):
    with open(DB_FILE, "wb") as f:
        pickle.dump(money_db, f)

def main():
    pr_money = read_db()
    print(f"현재 잔고는 {pr_money['잔고']:,}원")
    print(f"식비: {pr_money['식비']:,}원, 교통비: {pr_money['교통비']:,}원, 여가비: {pr_money['여가비']:,}원")

    while True:
        spending = input("얼마 사용했어? (용돈 추가하려면 '다음달', 종료하려면 '종료' 입력): ")  #아래서 숫자 입력 다시 처리
        if spending == '종료':
            break
        elif spending == '다음달':
            additional_money = int(input("받은 용돈 입력: "))
            pr_money["잔고"] += additional_money
        else:
            try:
                real_spending = int(spending)
            except ValueError:
                print("금액을 숫자로 입력하세요")
                continue

            category = input("카테고리 입력 (식비, 교통비, 여가비): ")
            if category not in ["식비", "교통비", "여가비"]:
                print("세 개중에 입력해")
                continue

            pr_money["잔고"] -= real_spending
            pr_money[category] += real_spending   #키값 체크

        print(f"현재 잔고는 {pr_money['잔고']:,}원")
        print(f"식비: {pr_money['식비']:,}원, 교통비: {pr_money['교통비']:,}원, 여가비: {pr_money['여가비']:,}원")

        write_db(pr_money)

if __name__ == '__main__':
    main()
