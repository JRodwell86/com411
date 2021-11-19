# importing the visualisation stuff.
import matplotlib.pyplot as plt

import csv

def read_data():
    with open('titanic.csv') as file:
        csv_reader = csv.reader(file)
        # removes headers from the text
        header = next(csv_reader)
        # makes a dictionary with the key pairs and second bit is list
        data = {'survived': [], 'sex': [], 'age': [],'fare': []}

        for values in csv_reader:

            survived = values[1].strip()
            sex = values[14].strip()
            age = values[4].strip()
            fare = values[8].strip()
            #only add the data for the above to the dictionary if it's not blank
            if (survived != "" and sex != "" and age != "" and fare != ""):
                # add the data to the dictionary. bool changes 0 to false and 1 to true.
                data['survived'].append(bool(int(survived)))
                #code to change 1&0 to male and female and add to dictionary.
                if (int(sex) == 0):
                    data['sex'].append('male')
                else:
                    data['sex'].append('female')
                #code to add age to dict as a float.
                data['age'].append(float(age))
                #code to add fare as a float, rounded to 2 places.
                data['fare'].append(round(float(fare), 2))
    # return the dictionary to the function
    return data

# two parameters - axes position and then data from read_data()
def plot_age_vs_survival(ax, data):
    # create dictionaries for each age group
    children = {'survived': [], 'deceased': []}
    adults = {'survived': [], 'deceased': []}
    elderly = {'survived': [], 'deceased': []}

    # populate each dictionary
    # for variable in the range of ages in the dictionary.
    for index in range(len(data['age'])):
        # variable to make the age
        age = data['age'][index]
        #if statement - if under 18 and survive add to survived list in children dictionary...etc...
        if (age < 18 and data['survived'][index]):
            children['survived'].append(age)
        elif (age < 18 and not data['survived'][index]):
            children['deceased'].append(age)
        elif (age < 65 and data['survived'][index]):
            adults['survived'].append(age)
        elif (age < 65 and not data['survived'][index]):
            adults['deceased'].append(age)
        elif (data['survived'][index]):
            elderly['survived'].append(age)
        else:
            elderly['deceased'].append(age)

    # prepare labels and totals
    labels = ['children', 'adults', 'elderly']
    # works out the totals for survived and deceased.
    survivors = [len(children['survived']), len(adults['survived']), len(elderly['survived'])]
    deceased = [len(children['deceased']), len(adults['deceased']), len(elderly['deceased'])]

    # display suitable bar plots
    # x axis is the different categories made in the labels above and survivors is the total number of suvvors for each
    ax.bar(labels, survivors, label='Survived')
    ax.bar(labels, deceased, bottom=survivors, label='Deceased')
    ax.set_ylabel('age')
    ax.legend()
    ax.set_title('Age vs Survival')


def plot_fare_vs_survival(ax, data):
    # two empty lists
    survived = []
    deceased = []
    # for variable in the range of fare prices
    for index in range(len(data['fare'])):
        #not needed but gives the individual fares
        fare = data['fare'][index]
        # if they are down as 'survived' in the index then adds the fare (the float number) to the list survived.
        if (data['survived'][index]):
            survived.append(data['fare'][index])
        # else add to deceased
        else:
            deceased.append(data['fare'][index])

    #plot a scatter graph with number of survived. Then using the float list of fares.
    ax.scatter(range(len(survived)), survived, label='Survived')
    ax.scatter(range(len(deceased)), deceased, label='Deceased')
    ax.set_ylabel('fare')
    ax.legend()
    ax.set_title('Fare vs Survival')


def plot_sex_vs_survival(ax, data):
    # empty dictionarys
    males = {'survived': [], 'deceased': []}
    females = {'survived': [], 'deceased': []}
    # for variable in the total records of sex
    for index in range(len(data['sex'])):
        sex = data['sex'][index]
        # if male and survived add to the list survived in males etc
        if (sex == 'male' and data['survived'][index]):
            males['survived'].append(sex)
        elif (sex == 'male' and not data['survived'][index]):
            males['deceased'].append(sex)
        elif (sex == 'female' and data['survived'][index]):
            females['survived'].append(sex)
        else:
            females['deceased'].append(sex)

    labels = ['male', 'female']
    # list of totals
    survivors = [len(males['survived']), len(females['survived'])]
    deceased = [len(males['deceased']), len(females['deceased'])]

    ax.bar(labels, survivors, label='Survived')
    # bottom is the y coordinate of the bars bases which is 0 by default
    ax.bar(labels, deceased, bottom=survivors, label='Deceased')
    ax.set_ylabel('passengers')
    ax.legend()
    ax.set_title('Sex vs Survival')


def plot_all_vs_survival(ax, data):
    children = {
        'male': {'survived': [], 'deceased': []},
        'female': {'survived': [], 'deceased': []}
    }

    adults = {
        'male': {'survived': [], 'deceased': []},
        'female': {'survived': [], 'deceased': []}
    }

    elderly = {
        'male': {'survived': [], 'deceased': []},
        'female': {'survived': [], 'deceased': []}
    }

    for index in range(len(data['age'])):
        age = data['age'][index]

        # children
        if (age < 18):
            if (data['sex'][index] == 'male' and data['survived'][index]):
                children['male']['survived'].append(age)
            elif (data['sex'][index] == 'male' and not data['survived'][index]):
                children['male']['deceased'].append(age)
            elif (data['sex'][index] == 'female' and data['survived'][index]):
                children['female']['survived'].append(age)
            elif (data['sex'][index] == 'female' and not data['survived'][index]):
                children['female']['deceased'].append(age)

        # adults
        elif (age < 65):
            if (data['sex'][index] == 'male' and data['survived'][index]):
                adults['male']['survived'].append(age)
            elif (data['sex'][index] == 'male' and not data['survived'][index]):
                adults['male']['deceased'].append(age)
            elif (data['sex'][index] == 'female' and data['survived'][index]):
                adults['female']['survived'].append(age)
            elif (data['sex'][index] == 'female' and not data['survived'][index]):
                adults['female']['deceased'].append(age)

        # elderly
        else:
            if (data['sex'][index] == 'male' and data['survived'][index]):
                elderly['male']['survived'].append(age)
            elif (data['sex'][index] == 'male' and not data['survived'][index]):
                elderly['male']['deceased'].append(age)
            elif (data['sex'][index] == 'female' and data['survived'][index]):
                elderly['female']['survived'].append(age)
            elif (data['sex'][index] == 'female' and not data['survived'][index]):
                elderly['female']['deceased'].append(age)

    x_labels = ['children', 'adults', 'elderly']
    male_survivors = [len(children['male']['survived']), len(adults['male']['survived']),
                      len(elderly['male']['survived'])]
    female_survivors = [len(children['female']['survived']), len(adults['female']['survived']),
                        len(elderly['female']['survived'])]

    ax.plot(x_labels, male_survivors, label='Male Survivors')
    ax.plot(x_labels, female_survivors, label='Female Survivors')
    ax.set_title('Age, Sex vs Survival')
    ax.legend()
    ax.set_title('All vs Survival')


def run():
    data = read_data()

    # plots arranged in a 2 by 2 grid
    fig, axs = plt.subplots(2, 2)

    # display plots
    plot_age_vs_survival(axs[0, 0], data)
    plot_fare_vs_survival(axs[0, 1], data)
    plot_sex_vs_survival(axs[1, 0], data)
    plot_all_vs_survival(axs[1, 1], data)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run()
