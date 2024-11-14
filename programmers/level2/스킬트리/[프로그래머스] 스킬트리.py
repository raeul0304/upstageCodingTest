def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        filtered_skills = [s for s in tree if s in skill]
        
        if filtered_skills == list(skill[:len(filtered_skills)]):
            answer += 1

    return answer