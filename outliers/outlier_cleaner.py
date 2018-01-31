#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here

    errors = [((abs(x1 - x2) *  100)/x2) for (x1, x2) in zip(predictions, net_worths)]

    data_with_errors = zip(ages, net_worths, errors)
    sorted_by_errors = sorted(data_with_errors, key=lambda tup: tup[2])

    cleaned_data = sorted_by_errors[0:int(0.9 * len(sorted_by_errors))]

    return cleaned_data
