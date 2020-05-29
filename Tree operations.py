from __future__ import print_function
import datetime
import pandas as pd



class The_Question:

    def __init__(self, column_no, value):    #to make object  from class  constructor initialize attributes of the class

        self.classColumn = column_no
        self.value = value

    def Similar_to(self, example):           #fn find how much the question will fit to
                                             #
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.classColumn]

        return val == self.value


def The_Counts(rows):
    counts = {}
    for row in rows:
        rate = row[-1]
        if rate not in counts:
            counts[rate] = 0
        counts[rate] += 1

    return counts

class Leaf:     
    def __init__(self, rows):
        self.predictions = The_Counts(rows)


def true_or_false(rows, question):          
    true_rows, false_rows = [], []
    for row in rows:
        if question.Similar_to(row):         #similar fn: see if the answer yes or no
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


def get_impurity(rows):                #quantify the uncertainity of the node 
                                       
    counts = The_Counts(rows)
    #print(counts)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl ** 2
    return impurity



def calculate_info(left, right, current_uncertainty):   #quantify how much the question reduces the uncertanity using concept called info gain
                                                        

    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * get_impurity(left) - (1 - p) * get_impurity(right)


def accurate_Split(rows):   
    maxGain = 0
    bestQuestion = None
    current_uncertainty = get_impurity(rows)
    n_features = len(rows[0]) - 1
    for col in range(n_features):

        values = set([row[col] for row in rows])


        for val in values:

            question = The_Question(col, val)

            trueRowsHere, falseRowsHere = true_or_false(rows, question)

            if len(trueRowsHere) == 0 or len(falseRowsHere) == 0:
                continue

            informationGained = calculate_info(trueRowsHere, falseRowsHere, current_uncertainty)

            if informationGained >= maxGain:
                maxGain, bestQuestion = informationGained, question

    return maxGain, bestQuestion




class Tree_Node:           

    def __init__(self,
                 branchingQuestion,
                 trueDecisionBranch,
                 falseDecisionBranch):
        self.question = branchingQuestion
        self.true_branch = trueDecisionBranch
        self.false_branch = falseDecisionBranch


def BuildTree(rows):       
    gain, question = accurate_Split(rows)      

    if gain == 0:
        return Leaf(rows)

    true_rows, false_rows = true_or_false(rows, question)  

    true_branch = BuildTree(true_rows)

    false_branch = BuildTree(false_rows)

    return Tree_Node(question, true_branch, false_branch)

)
def arrange(row, node):  #classify returns postive or negative
    if isinstance(node, Leaf):  
        return node.predictions

    if node.question.Similar_to(row):
        return arrange(row, node.true_branch)
    else:
        return arrange(row, node.false_branch)

def GetList(Data, tree):
    rows = []
    i = 0
    for row in Data:
        rows.append(arrange(row, tree))
        # print("Review Number: %s, Predicted: %s" %
        # (i, arrange(row, ourTree)))
        i += 1
    item = 0
    for item in range(len(rows)):  # to check accuracy
        if 'Positive' in rows[item] and 'Negative' not in rows[item]:
            rows[item] = 'Positive'
        elif 'Negative' in rows[item] and 'Positive' not in rows[item]:
            rows[item] = 'Negative'
        else:
            if int(rows[item]['Positive']) > int(rows[item]['Negative']):
                rows[item] = 'Positive'
            else:
                rows[item] = 'Negative'
        item += 1

    return rows


def calculate_accuracy(predicted_rating,actual_rating):
    accuracy = 100 * (1 - ((abs(int(actual_rating['Positive']) - int(predicted_rating['Positive'])) + abs(
        int(actual_rating['Negative']) - int(predicted_rating['Negative']))) / (
                                   int(actual_rating['Positive']) + int(actual_rating['Negative']))))

    return accuracy
