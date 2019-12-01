while True:
    try:
        d = 0.875
        flag = 0
        pages = input().split(" ")
        
        linksFeitas = {}
        linksRecebidas = {}
        pr = {}
        num_pass = 0
        aux = input().split(" ")

        while("->" in aux):
            flag = 1
            if aux[0] != aux[2]:
                if(aux[0] in linksFeitas.keys()):
                    if aux[2] not in linksFeitas[aux[0]]:
                        linksFeitas[aux[0]]+=aux[2]
                else:
                    linksFeitas[aux[0]]=[aux[2]]
            aux.clear()
            aux = input().split(" ")
            if("->" not in aux):
                num_pass = aux[0]
                flag = 0

        if(flag == 0):
            num_pass = aux[0]

        for k in linksFeitas:
            for l in linksFeitas[k]:
                if l in linksRecebidas.keys():
                    linksRecebidas[l] += k
                else:
                    linksRecebidas[l] = [k]
                    

        for i in range(int(num_pass)+1):
            if i == 0:
                for j in pages:
                    if j not in pr.keys():
                        pr[j] = [round(1/len(pages),3)]
                    else: 
                        pr[j] += [1/len(pages)]
            else:
                a = 0
                for j in pages:
                    for k in j:
                        if k in linksRecebidas.keys():
                            for l in linksRecebidas[k]:
                                a+=pr[l][i-1]/len(linksFeitas[l])
                    pr[j] += [round((1 - d)/len(pages) + d * a,3)]
                    a = 0
            
        
        for i in pages:
            if i in linksFeitas.keys():
                print(f"{i} -> {linksFeitas[i]}")
            else:
                print(f"{i} -> []")
            if i in linksRecebidas.keys():
                print(f"{linksRecebidas[i]} -> {i}")
            else:
                print(f"[] -> {i}")
            
        for i in range(int(num_pass)+1):
            print(f"PageRank (passo {i})")
            for j in pr:
                print(f"{j}: {pr[j][i]}")

    except EOFError:
        break
