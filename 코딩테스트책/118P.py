N = 4
M = 4

position = [1,1,0]  # (x, y, head)

world =  [[1,1,1,1],
          [1,0,0,1],
          [1,1,0,1],
          [1,1,1,1]]

trial = 0
visit = 1

# 플레이어 시작점을 방문 표시
x = position[0]
y = position[1]
world[x][y] = 2


def rotate():
    global position
    if position[2] == 0:
        position[2] = 3
    else:
        position[2] -= 1

def get_forward_step():
    global position
    x = position[0]
    y = position[1]
    head = position[2]

    if head == 0:
        forward = [x-1, y]
    elif head == 1:
        forward = [x, y+1]
    elif head == 2:
        forward = [x+1, y]
    elif head == 3:
        forward = [x, y-1]

    return forward

def get_backward_step():
    global position
    x = position[0]
    y = position[1]
    head = position[2]

    if head == 0:
        backward = [x+1, y]
    elif head == 1:
        backward = [x, y-1]
    elif head == 2:
        backward = [x-1, y]
    elif head == 3:
        backward = [x, y+1]

    return backward

def can_go_forward():
    global my_position
    global world

    forward = get_forward_step()
    
    if(forward[0]<0 or forward[0]>=N or forward[1]<0 or forward[1]>=M): 
        return False
    
    next_x = forward[0]
    next_y = forward[1]

    if world[next_x][next_y] == 1: return False
    elif world[next_x][next_y] == 0: return True


def can_go_backward():
    global my_position
    global world

    backward = get_backward_step()
    
    if(backward[0]<0 or backward[0]>=N or backward[1]<0 or backward[1]>=M): 
        return False
    
    next_x = backward[0]
    next_y = backward[1]

    if world[next_x][next_y] == 1: return False
    elif world[next_x][next_y] == 2: return True


def go_forward():
    global position
    global world

    forward = get_forward_step()
    x = forward[0]
    y = forward[1]

    # 플레이어 위치 이동
    position[0] = x
    position[1] = y

    # 방문표시
    world[x][y] = 2



def go_backward():
    global position
    global world

    backward = get_backward_step()
    x = backward[0]
    y = backward[1]

    # 플레이어 위치 이동
    position[0] = x
    position[1] = y

while True:
    if(trial == 4):
        if can_go_backward():
            go_backward()
            trial = 0
        else:
            break
    rotate()
    if can_go_forward(): 
        go_forward()
        visit += 1
        trial = 0
    else:
        trial += 1
        continue

print(visit)