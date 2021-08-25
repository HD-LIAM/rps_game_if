print("===========================================")
print("가위, 바위, 보 게임을 시작합니다!!")

#컴퓨터가 가위, 바위, 보를 하게 만드는 방법
import random   # random 모듈을 사용할 수 있도록 하는 방법

rps_game = ['가위', '바위', '보']      #[]는 list / rps =  rock, paper, scissors
computer = random.choice(rps_game)    #주어진 list에서 무작위로 하나 뽑고 싶을때 choice라는 함수사용

mychoice = input("가위, 바위, 보 중 선택하세요: ")   # 나의 선택 입력

print("컴퓨터의 선택: " + computer)    # str끼리 계산이라서 + 사용 가능
print("나의 선택: " + mychoice)

# 단순히 if문 사용하여 경우의 수 별로 코딩한 경우
if computer == '가위' :                         
    if mychoice == '가위' :
        print("비겼다!!")
    elif mychoice == '바위' :
        print("내가 이겼다!!")
    elif mychoice == '보' :
        print("컴퓨터가 이겼다!!")

elif computer == '바위' :
    if mychoice == '바위' :
        print("비겼다!!")
    elif mychoice == '보' :
        print("내가 이겼다!!")
    elif mychoice == '가위' :
        print("컴퓨터가 이겼다!!")

elif computer == '보' :
    if mychoice == '보' :
        print("비겼다!!")
    elif mychoice == '가위' :
        print("내가 이겼다!!")
    elif mychoice == '바위' :
        print("컴퓨터가 이겼다!!")

print("===========================================")