import scipy.stats
import pandas as pd


def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data
    (left-handed and right-handed hitters).

    The source file a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg').

    The function will read the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.

    One cohort is data frame of right-handed batters. And the other
    cohort is a data frame of left-handed batters.

    With a significance level of 95%, if there is no difference
    between the two cohorts, the function returns a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.

    If there is a difference, the functiopn returns a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.

    For example, the tuple that is returned may look like:
    (True, (9.93570222, 0.000023))
    """
    # Read the csv file in to a data frame
    df = pd.read_csv(filename, sep=",")
    # Drop Null in the Handedness
    # and the Batting Averages Column
    df = df.dropna(subset=["handedness", "avg"])
    # Create two seperate dataframes containing
    # batting averages for left and right handed players
    df_right = df[df["handedness"] == "R"]
    df_left = df[df["handedness"] == "L"]
    # Perform the t-test on the batting averages from the two dataframes
    t_test_results = scipy.stats.ttest_ind(df_left["avg"],
                                           df_right["avg"],
                                           equal_var=False)
    # If there is a significant difference between
    # averages return False along with the t-test values
    if t_test_results[1] <= 0.05:
        print((False, (t_test_results[0], t_test_results[1])))
    else:
        print((True, (t_test_results[0], t_test_results[1])))


compare_averages("src_data/baseball_stats.csv")
