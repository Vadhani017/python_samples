# hypothesis testing z-test

import math
import random
import statistics

import numpy as np

print("Calculating the hypothesis, whether the mean of sample represents the mean of population with level of "
      "significance 0.05")
# getting population count
population = int(input("Enter total population count = "))
# getting sample count
sample_count = int(input("Enter the sample count = "))
pop1 = np.array([population], dtype=int)

# if sample size is greater than population, then the sample is not from population
# So, checking
if population > sample_count:
    print("Enter the population values")
    for val in range(population):
        value1 = int(input("Enter the value= "))
        pop1 = np.append(pop1, value1)

    # calculating the parameters for doing z - test
    sample1 = np.random.choice(pop1, size=sample_count)
    mu = pop1.mean()
    x_bar = sample1.mean()
    standard_deviation = statistics.stdev(data=pop1, xbar=None)

    # calculating the z-test
    test_statistic = (x_bar - mu) * math.sqrt(population) / standard_deviation

    # choice of doing testing
    print("Enter T if you want two sided test\n"
          "Enter L if you want left tailed test\n"
          "Enter R if you want right tailed test\n")
    test_choice = input()

    # estimating test result
    if test_choice == 'T':
        if test_statistic < 1.96:
            if test_statistic > -1.96:
                print("The test statistic value is ", test_statistic)
                print("The sample mean represents the population mean")
            else:
                print("The test statistic value is ", test_statistic)
                print("The generated sample's mean does not represents the population mean")
    elif test_choice == 'L':
        if test_statistic > 1.645:
            print("The test statistic value is ", test_statistic)
            print("The sample mean represents the population mean")
        else:
            print("The test statistic value is ", test_statistic)
            print("The generated sample's mean does not represents the population mean")
    elif test_choice == 'R':
        if test_statistic < 1.645:
            print("The test statistic value is ", test_statistic)
            print("The sample mean represents the population mean")
        else:
            print("The test statistic value is ", test_statistic)
            print("The generated sample's mean does not represents the population mean")

else:
    print("Population count should be greater than sample count")

