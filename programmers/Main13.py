def solution(board):
    for x in range(1, len(board)):
        for y in range(1, len(board[0])):
            if board[x][y]==1:                                                   #board[x][y]가 정사각형의 맨 오른쪽 아래 꼭지점일경우 
                board[x][y]=min(board[x-1][y-1], board[x-1][y], board[x][y-1])+1 #만들수있는 정사각형의 한변의 길이의 최대값으로 값을 바꿔준다
    answer=max([num for row in board for num in row])**2

    return answer