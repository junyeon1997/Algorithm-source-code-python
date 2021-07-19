#enumerate로 각 배열 인덱스자리의 값을 비교
def solution(skill, skill_trees):
    answer = len(skill_trees)
    for i in skill_trees:
        arr=[]
        for j in list(i):
            if j in skill:
                arr.append(j)
        for idx,a in enumerate(arr):
            if a!=skill[idx]:
                answer-=1
                break      
    return answer

#pop으로 각 원소를 직접 비교
def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    for skills in skill_trees:
        skill_list = list(skill)
        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    answer -= 1
                    break
    return answer