def outlierCleaner(predictions, x, y):
    """
        Clean away k points that have the largest
        residual errors (different between the prediction
        and the actual)

        Return:
            - cleaned_data: list of tuple of the form (x, y, error)
            - cleaned_list: list of value x needed to be removed
    """
    
    cleaned_data = list(zip(x, y, [(float(pred) - actual)**2 for pred, actual in zip(predictions, y)]))
    cleaned_data.sort(key = lambda tup: tup[2])

    #for i in range(0, int(len(cleaned_data) * 0.1)):
    cleaned_list = []
    #k = int(0.01*len(cleaned_data)) # Number of points removed
    k = 40
    for i in range(0, k): 
        cleaned_list.append(cleaned_data[-1][0])
        cleaned_data.pop()
    return cleaned_data, cleaned_list
