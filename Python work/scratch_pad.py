def snail_old(snail_map):
    if snail_map == [[]]:
        return snail_map
    else:
        array = snail_map.pop(0)
        last_array = snail_map.pop(len(snail_map)-1)
        last_array.reverse()
        for x in snail_map:
            print(x)
            array.append(x.pop(len(x)-1))
        print(type(last_array))
        array = array+last_array
        for x in range((len(snail_map))-1,-1,-1):
            array.append(snail_map[x].pop(0))   
        array = array+snail_map.pop(0)
        array += snail_map[len(snail_map)-1][::-1]

    return array

def snail(snail_map):
    array = []
    while snail_map!= []:
        array += snail_map.pop(0)
        if snail_map!= []:
            last_array = snail_map.pop(len(snail_map)-1)
            last_array.reverse()
            for x in snail_map:
                array.append(x.pop(len(x)-1)) 
            array += last_array
            for x in range((len(snail_map))-1,-1,-1):
                array.append(snail_map[x].pop(0))
        
    return array


array = [[1,2,3,4],
         [5,6,7,8],
         [8,9,10,11],
         [12,13,14,15]]

array_2=[[1,2,3],
         [4,5,6],
         [7,8,9]]


print(snail(array))

print(snail(array_2))