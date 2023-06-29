class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #기울기 절편 계산해서 직선의 방정식구하고 점들이 그 위에 있는지 확인
        #x값은 0, y값은 1을 인덱스로

        if coordinates[1][0] - coordinates[0][0] == 0:
            for i in range(len(coordinates)-1):
                if coordinates[i][0] != coordinates[i+1][0]:
                    return False
        
        else:
            a = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            b = coordinates[0][1] - a*coordinates[0][0]

            #y=ax+b
            for i in range(len(coordinates)):
                if coordinates[i][1] != a*coordinates[i][0]+b:
                    return False
    
        return True