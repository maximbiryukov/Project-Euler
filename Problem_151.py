def table(sheet):
    
    table = []
    
    if sheet != 1:
        while 1 not in table:
            sheet /= 2
            table.append(sheet)
            
    return table


def batch(envelope, options = {():0}):
              
    output = 0
    
    envelope = tuple(envelope)
    
    if envelope and envelope not in options:
        options[envelope] = 0
        
        for item in envelope:
            
            new_env = list(envelope)
            new_env.remove(item)
            new_env += cut(item)
            new_env = sorted(new_env)
            
            output += batch(tuple(new_env), options)
            
        output /= len(envelope)
        
        if len(envelope) == 1:
            output += 1
            
        options[envelope] = output
        
        
        
    return options[envelope]

round(batch((16,))-2, 6)
