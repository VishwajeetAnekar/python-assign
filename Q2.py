def process(input_list):
    result = {}

    for item in input_list:
        key, value = item.split(":")
        value = int(value)
        
        if key in result:
            result[key] += value
        else:
            result[key] = value
            
    
    output = ""
    comma = True
    for key in sorted(result):
        if result[key] != 0:
            if not comma:
                output += ","
            output += f"{key}:{result[key]}"
            comma = False

    print(output) 

process(["B:-1","A:1","B:3","A:5"])  
process(["Z:0","A:-1"])      
     
