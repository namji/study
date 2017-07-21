'''
총 3개의 기둥이 있고 첫번째 기둥에 작은 원판이 위에 있도록 순서대로 쌓여져 있다.
첫번째 기둥이 있는 원판들을 마지막 기둥으로 옮겨야하며 최종적으로 동일한 순서를 유지해야 한다. 이때 다음 두 가지 조건을 만족시켜야 한다.

한 번에 하나의 원판만 옮길 수 있다.
큰 원판이 작은 원판 위에 있어서는 안 된다.
하노이 타워 문제에도 재귀적 사고를 적용해보자.

일단 n번째 즉 제일 마지막 원판이 마지막 기둥 제일 아래에 위치시켜야 한다. 이것을 위해서는 n-1개의 원판은 중간 기둥에 모두 옮겨져 있어야 한다.
중간 기둥에 있는 n-1개의 원판중 n-1번째 원판을 마지막 기둥으로 옮겨야한다. 이것을 위해서는 n-2개의 원판을 비어있는 첫번째 원판으로 옮겨야한다.
…이런 반복이 무한하게 반복된다. 여기서 각 단계 마다의 탈출 조건(Base case)은 옮겨야할 원판이 아무것도 없다면 종료될 것이다.
'''


def hanoi(n, start=1, way=2, end=3):
    print('hanoi({}, {}, {}, {})'.format(n, start, way, end))
    if n == 0:
        return
    else:
        # 마지막 원판을 end에 놓기 위해 마지막 원판보다 작은애들을 모두 way에 옮겨놓는다
        hanoi(n-1, start, end, way)
        # 마지막 원판을 end에다가 옮긴다.
        print('{n}번째 원판: {start} => {end}'.format(n=n, start=start, end=end))
        # 마지막 원판 위에다가 나머지 작은 원판을 놓는다.
        hanoi(n-1, way, start, end)