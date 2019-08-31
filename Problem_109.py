all_scores = []
for _ in range(0,21):
    all_scores.append([_,"S"])
for _ in range(1,21):
    all_scores.append([_*2,"D"])
for _ in range(1,21):
    all_scores.append([_*3,"T"])
    
all_scores.append([25,"S"])
all_scores.append([50,"D"])

targets = [i for i in range(2,100)]

result = []

for i in all_scores:
    for j in all_scores:
        for k in all_scores:
            
            if k[0] > 0:
                
                if k[1] == "D" and i[0]+j[0] == 0 and k[0] in targets and [k,j,i, k[0]+j[0]+i[0]] not in result:
                    result.append([k,j,i, k[0]+j[0]+i[0]])
                if j[1] == "D" and k[0] + j[0] in targets and i[0] == 0 and [k,j,i, k[0]+j[0]+i[0]] not in result:
                    result.append([k,j,i, k[0]+j[0]+i[0]])
                if i[1] == "D" and k[0] + j[0] + i[0] in targets and j[0] != 0 and [k,j,i, k[0]+j[0]+i[0]] not in result and [j,k,i, k[0]+j[0]+i[0]] not in result:
                    result.append([k,j,i, k[0]+j[0]+i[0]])
print(len(result)
