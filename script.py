import csv


# get all data from csv file and save it to a list of dictionaries
insurance_data = []
with open('insurance.csv') as insurance_data_file:
    insurance_data_reader = csv.DictReader(insurance_data_file)
    for row in insurance_data_reader:
        insurance_data.append(row)


# function to get average age of all patients
def average_age():
    # variable to track total age and the number of ages
    total_age = 0
    num_ages = 0
    # loop through data to get ages and add to total and count
    for each in insurance_data:
        total_age += int(each['age'])
        num_ages += 1
    # calculate average age and return appropriate sentence
    average_age = total_age / num_ages
    return("The average age of the {num} patients is {average} years old.".format(num=num_ages, average=int(average_age)))


# function to get female to make ratio of patients
def female_male_ratio():
    # variables to track number of women and men
    female = 0
    male = 0
    # loop through data set and add to women/men variable
    for each in insurance_data:
        if each['sex'] == 'female':
            female += 1
        else:
            male += 1
    # calculate ratio rounded off to two decimal places and return appropriate sentence
    ratio = round(female / male, 2)
    return("There are {women} women and {men} men in this group of patients. Which means that there are {ratio} women for every man.".format(women=female, men=male, ratio=ratio))


# function to get number of smokers and non-smokers and their average insurance costs
def smoking():
    # variable to track how many smokers/non-smokers and the total costs for each group
    num_smokers = 0
    num_non_smokers = 0
    smoker_cost = 0
    non_smoker_cost = 0

    # loop through data set to get data and save to above variables
    for each in insurance_data:
        if each['smoker'] == 'yes':
            num_smokers += 1
            smoker_cost += float(each['charges'])
        else:
            num_non_smokers += 1
            non_smoker_cost += float(each['charges'])

    # calculate the averages and return appropriate sentence
    smoker_average = round(smoker_cost / num_smokers, 2)
    non_smoker_average = round(non_smoker_cost / num_non_smokers, 2)
    return("There are {num_smokers} smokers and {num_non_smokers} non-smokers in this group of patients. \n The average insurance cost for a smoker is {smoker} dollars and the average insurance cost a non-smoker is {non} dollars.".format(num_smokers=num_smokers, num_non_smokers=num_non_smokers, smoker=smoker_average, non=non_smoker_average))


#function to group people by number of children they have and then calculate their average insurance costs
def children():
    #lists to hold costs per group and number per group
    costs = [0, 0, 0, 0, 0, 0]
    counts = [0, 0, 0, 0, 0, 0]

    #loop through data set and save data to relevent lists
    for each in insurance_data:
        if each['children'] == '0':
            costs[0] = costs[0] + float(each['charges'])
            counts[0] += 1
        elif each['children'] == '1':
            costs[1] += float(each['charges'])
            counts[1] += 1
        elif each['children'] == '2':
            costs[2] += float(each['charges'])
            counts[2] += 1
        elif each['children'] == '3':
            costs[3] += float(each['charges'])
            counts[3] += 1
        elif each['children'] == '4':
            costs[4] += float(each['charges'])
            counts[4] += 1
        elif int(each['children']) >= 5:
            costs[5] += float(each['charges'])
            counts[5] += 1
            
    #loop through lists and display data in appropriate message 
    for i in range(6):
        print(str(i) + " children: " + str(counts[i]) + " patients with average insurance costs of " + str(round(costs[i] / counts[i], 2)) + " dollars.")        