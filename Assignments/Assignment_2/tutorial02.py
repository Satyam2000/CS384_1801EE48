import math
# All decimal 3 places


# Function to compute mean
def mean(first_list):
    # mean Logic
    mean_value = summation(first_list) / len(first_list)     

    return round(mean_value,3)


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    median_value = 0
    for x in range(len(first_list)) :
        if (not isinstance(first_list[x],int)) and (not isinstance(first_list[x],float)) :
            return 0
        else:
            list1=sorting(first_list.copy())
            n=len(list1)
            if(n%2 == 0) :
                median_value=(list1[int((n/2)-1)]+list[int(n/2)])/2
            else:
                median_value=list1[(int((n+1)/2)-1)]

            return round(median_value,3)


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    for x in range(len(first_list)) :
        if (not isinstance(first_list[x],int)) and (not isinstance(first_list[x],float)) :
            return 0

    else:
        standard_deviation_value=math.sqrt(variance(first_list))
        return round(standard_deviation_value,3)
    


# Function to compute variance. You cant use Python functions
def variance(first_list):
    for x in range(len(first_list)) :
        if (not isinstance(first_list[x],int)) and (not isinstance(first_list[x],float)) :
            return 0
    else:
    # variance Logic
        avg=mean(first_list)
        list2=[]
        for i in range(len(first_list)):
            list2.append((first_list[i-1]-avg)*(first_list[i-1]-avg))

        variance_value=mean(list2)
        return round(variance_value,3)
    


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    for i in first_list:
        if (not isinstance(i,int)) and (not isinstance(i,float)):
            return 0
    for i in second_list:
        if (not isinstance(i,int)) and (not isinstance(i,float)) :
            return 0
             
    rmse_value=math.sqrt(mse(first_list,second_list))
    
    return round(rmse_value,3)


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    for i in first_list:
        if (not isinstance(i,int)) and (not isinstance(i,float)):
            return 0
    for i in second_list:
        if (not isinstance(i,int)) and (not isinstance(i,float)) :
            return 0

    list3=[]
    for (i,j) in zip(first_list,second_list):
        list3.append(((i-j)*(i-j)))

    mse_value=mean(list3)

    return mse_value

# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    for i in first_list:
        if (not isinstance(i,int)) and (not isinstance(i,float)):
            return 0
    for i in second_list:
        if (not isinstance(i,int)) and (not isinstance(i,float)) :
            return 0

    # mae Logic
    if(len(first_list)!=len(second_list)):
        return 0
    list6=[]

    for x,y in zip(first_list,second_list):
        list6.append(abs(x-y))

    mae_value=mean(list6)

    return round(mae_value,3)

    


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    for i in first_list:
        if (not isinstance(i,int)) and (not isinstance(i,float)):
            return 0
    for i in second_list:
        if (not isinstance(i,int)) and (not isinstance(i,float)) :
            return 0

    # nse Logic
    nse_value = 1 - (mse(first_list,second_list)/variance(first_list))

    return round(nse_value,3)



# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    for i in first_list:
        if (not isinstance(i,int)) and (not isinstance(i,float)):
            return 0
    for i in second_list:
        if (not isinstance(i,int)) and (not isinstance(i,float)) :
            return 0

    # nse Logic
    mylist=[]

    avg1=mean(first_list)

    avg2=mean(second_list)

    for x,y in zip(first_list,second_list):
        mylist.append((x-avg1)*(y-avg2))

    avg=mean(mylist)
    pcc_value=(avg/(standard_deviation(first_list)*standard_deviation(second_list)))
    return round(pcc_value,3)    


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    for x in range(len(first_list)) :
        if (not isinstance(first_list[x],int)) and (not isinstance(first_list[x],float)) :
            return 0
    else:        
        # Skewness Logic
        var=standard_deviation(first_list)
        avg=mean(first_list)

        list4=[]

        for i in first_list:
            list4.append(((i-avg)/var)*((i-avg)/var)*((i-avg)/var))
        skewness_value = mean(list4)
        return round(skewness_value,3)
    
def sorting(first_list):
    # Sorting Logic
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    for x in range(len(first_list)) :
        if (not isinstance(first_list[x],int)) and (not isinstance(first_list[x],float)) :
            return 0
    else:        
    # Kurtosis Logic
        var=standard_deviation(first_list)
        avg=mean(first_list)
        list5=[]

        for x in first_list:
            list5.append(((x-avg)/var)*((x-avg)/var)*((x-avg)/var)*((x-avg)/var))

        kurtosis_value=mean(list5)

        return round(kurtosis_value,3)



# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value = 0
    for x in range(len(first_list)) :
        if (not isinstance(first_list[x],int)) and (not isinstance(first_list[x],float)) :
            return 0
            
        else:
            summation_value = summation_value + first_list[x]

    return summation_value



# Python program for implementation of Quicksort  sorting algorithm
 
def partition(arr,low,high): 
	i = ( low-1 )		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		# If current element is smaller than the pivot 
		if arr[j] < pivot: 
		
			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 


# Function to do Quick sort 
def quickSort(arr,low,high): 
	if low < high: 
 
	    pi = partition(arr,low,high) 
 
	    quickSort(arr, low, pi-1) 
	    quickSort(arr, pi+1, high) 

#Function to do the sorting of list using Quick sort
def sorting(first_list):
    # Sorting Logic
    quickSort(first_list,0,len(first_list)-1)

    return first_list
