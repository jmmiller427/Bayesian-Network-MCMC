"""
Name: John Miller
Date: 15 November 2017
Class: CS 463 - 001
Project: Bayesian Network Markov Chain Monte Carlo (MCMC)

Structure: - Given a Bayesian Network, find all the conditional probabilities of each node given
             its Markov Blanket (Except Node C)
           - Generate random boolean values for each node value (C will always be true)
           - Run a loop 10,000 times to check each node
           - For each node, check if the CPT values match the randomly generated node values,
             if they match then check if the current node you are checking is true or false,
             flip the state of the node if a random number generated from 0 to 1 is greater
             than the conditional probability calculated.

Note: - Nodes A, B, D and E are all calculated the same way with just different values from the
        randomly generated node array.
"""

from random import randint
import matplotlib.pyplot as plt


def main():
    #  ---------------------------
    # | B   C   D   a       ~a    |
    # | 1   1   1   .8873   .1127 |
    # | 1   1   0   .9921   .0079 |
    # | 0   1   1   .2727   .7273 |
    # | 0   1   0   .8517   .1429 |
    #  ---------------------------
    table_a = [[1, 1, 1, .8873, .1127],
               [1, 1, 0, .9921, .0079],
               [0, 1, 1, .2727, .7273],
               [0, 1, 0, .8517, .1429]]

    #  ------------------
    # | A   b       ~b   |
    # | 1   .9130   .0870|
    # | 0   .0184   .9816|
    #  ------------------
    table_b = [[1, .9130, .0870],
               [0, .0184, .9816]]

    #  -------------------------
    # | A   C   E   d      ~d   |
    # | 1   1   1   .027   .973 |
    # | 1   1   0   .692   .308 |
    # | 0   1   1   .308   .692 |
    # | 0   1   0   .973   .027 |
    #  -------------------------
    table_d = [[1, 1, 1, .027, .973],
               [1, 1, 0, .692, .308],
               [0, 1, 1, .308, .692],
               [0, 1, 0, .973, .027]]

    #  --------------------
    # | C   D   b      ~b  |
    # | 1   1   .100   .900|
    # | 1   0   .900   .100|
    #  --------------------
    table_e = [[1, 1, .100, .900],
               [1, 0, .900, .100]]

    bIsTrue = 0
    ratioBInstances = []

    # Create a nodes array
    # A = 0, B = 1, C = 2, D = 3, E = 4
    nodes = []
    for j in range(0, 5):

        # Generate random 0 or 1 for each state, but make sure to set C to 1
        nodes.append(randint(0, 1))
    nodes[2] = 1

    # Loop through 10,000 iterations, Checking each node every time
    for k in range(1, 10001):

        """ NODE A """
        # Get random number for checking node A
        randnum = randint(0, 100) / 100

        # Check Node A
        for l in range(len(table_a)):

            # If the B and D state are equal to the B and D state of the randomly generated nodes state
            if table_a[l][0] == nodes[1] and table_a[l][2] == nodes[3]:

                # If the randomly generated node value for A was a 0, check if the random number
                # generated is greater than the value of ~a, if it is change the node value to 1
                if nodes[0] == 0:
                    if randnum > table_a[l][4]:
                        nodes[0] = 1

                # If the randomly generated node value for A was a 1, then check if the random number
                # to see if it is greater than the value of a, if it is change the node value to 0
                elif nodes[0] == 1:
                    if randnum > table_a[l][3]:
                        nodes[0] = 0

        """ NODE B """
        # Get random number for checking node B
        randnum = randint(0, 100) / 100

        # Check Node B
        for l in range(len(table_b)):

            if table_b[l][0] == nodes[0]:

                if nodes[1] == 0:
                    if randnum > table_b[l][2]:
                        nodes[1] = 1

                elif nodes[1] == 1:
                    if randnum > table_b[l][1]:
                        nodes[1] = 0

        """ NODE D """
        # Get random number for checking node D
        randnum = randint(0, 100) / 100

        # Check Node D
        for l in range(len(table_d)):

            if table_d[l][0] == nodes[0] and table_d[l][4] == nodes[4]:

                if nodes[3] == 0:
                    if randnum > table_d[l][4]:
                        nodes[3] = 1

                elif nodes[3] == 1:
                    if randnum > table_d[l][3]:
                        nodes[3] = 0

        """ NODE E """
        # Get random number for checking node E
        randnum = randint(0, 100) / 100

        # Check Node E
        for l in range(len(table_e)):

            if table_e[l][1] == nodes[3]:

                if nodes[4] == 0:
                    if randnum > table_e[l][3]:
                        nodes[4] = 1

                elif nodes[4] == 1:
                    if randnum > table_e[l][2]:
                        nodes[4] = 0

        # If B is true, add to the true count for a ratio
        if nodes[1] == 1:
            bIsTrue += 1

        # If it is a 1000th run, add a ratio of B being true to the number of instances to an array to graph
        if k % 100 == 0:
            ratioBInstances.append(bIsTrue / k)

    # Plot the ratio points. The points are plotted every 100
    xValue = range(0, 100)
    plt.scatter(xValue, ratioBInstances)
    plt.xlabel("Iterations")
    plt.ylabel("B Ratio")
    plt.title("Pr(B|C=T)")
    plt.show()


main()
