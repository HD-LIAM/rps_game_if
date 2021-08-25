print("=====================================================")
print("가위, 바위, 보 게임을 시작합니다!!")

#컴퓨터가 가위, 바위, 보를 하게 만드는 방법
import random   # random 모듈을 사용할 수 있도록 하는 방법

rps_game = ['바위', '가위', '보']      #[]는 list / rps =  rock, paper, scissors
computer = random.randint(0,2)    #주어진 list에서 무작위로 하나 뽑고 싶을때 choice라는 함수사용

mychoice = int(input("0: 바위, 1: 가위, 2: 보, 중 하나의 숫자를 입력하세요: "))   # 나의 선택 입력

print("나의 선택:", rps_game[mychoice])
print("컴퓨터의 선택:", rps_game[computer])

if computer == mychoice :
    print("비겼습니다!!")
elif mychoice - computer == -1 or (mychoice == 2 and computer == 0 ):
    print("내가 이겼다!!")
else:
    print("컴퓨터가 이겼다!!")
# 내가 이긴 경우는 2가지 경우의 수는 차이가 -1이고 나머지 경우는 and로 적어줬다
# 주의할 점은 0,1,2를 결정할때 낮은숫자가 한자리 높은숫자를 이기도록 설정해야 한다는 것이다 ex)0:바위, 1:가위
# 그리고 보가 바위를 이길 수있게 and로 추가해줬다.
# 그 외 비긴 경우를 제외한 모든 조건은 컴퓨터가 이긴다.

print("=====================================================")