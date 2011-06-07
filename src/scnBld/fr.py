
        
        names = []
        for i in range(len(row)):
            try:
                t=int(row[i])
                row[i]=t 
            except ValueError:
                t=float(row[i])
                row[i]=t
                row=tuple(row)
                names.append(row)
                print names