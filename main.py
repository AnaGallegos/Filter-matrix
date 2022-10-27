def process_matrix(arr):
    # Here we'll catch our final result
    result = []

    # We go through the matrix and we'll work with each line

    for i in range(len(arr)):
        lines = []
        # Then we go through the lines and work with each element
        try:
            for j, value in enumerate(arr[i]):

                if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1: # corners
                    
                    get_neighbors = [arr[i][j]]
                    if i != 0:
                        get_neighbors.append(arr[i - 1][j])  # top neighbor
                    if j != len(arr[i]) - 1:
                        get_neighbors.append(arr[i][j + 1])  # right neighbor
                    if i != len(arr) - 1:
                        get_neighbors.append(arr[i + 1][j])  # bottom neighbor
                    if j != 0:
                        get_neighbors.append(arr[i][j - 1])  # left neighbor                   
                else:
                    # add neighbors
                    get_neighbors = [
                        arr[i][j],      # actual value
                        arr[i - 1][j],  # top neighbor
                        arr[i][j + 1],  # right neighbor
                        arr[i + 1][j],  # bottom neighbor
                        arr[i][j - 1]   # left neighbor
                    ]   
                avg = get_average(get_neighbors)  # When we have all the values in a list, we get the average
                lines.append(avg)                 # And we add it to the line we are currently working
            result.append(lines)                  # Then we add the line to the result
        except TypeError:
            try:
                result = process_line(arr)
            except TypeError:
                print('Thats not a matrix!!😢')
                break
    return result

def get_average(values):
    """Gets a list of numbers and returns the average, rounding up to 2 decimals"""
    return round(sum(values)/len(values),2)

def process_line(arr):
    result = []
    for index, values in enumerate(arr):
        numbers = []
        if index == 0:
            numbers.append([arr[index]])
            numbers.append(arr[index + 1])
            
        if index == len(arr) - 1:
            numbers.append(arr[index])
            numbers.append(arr[index -1])
        else:
            numbers.append(arr[index])
            numbers.append(arr[index -1])
            numbers.append(arr[index +1])
        result.append(get_average(numbers))
    return result
            