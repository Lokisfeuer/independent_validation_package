from sklearn.metrics import accuracy_score, balanced_accuracy_score

def b_accuracy(predictions, true_values):
    preds = []
    trues = []
    accs = []
    baccs = []
    for pre, tru in zip(predictions, true_values):
        preds.append(pre)
        trues.append(tru)
        accs.append(accuracy_score(trues, preds))
        baccs.append(balanced_accuracy_score(trues, preds))
    return accs, baccs

if __name__ == '__main__':
    print(b_accuracy([1, 1, 1, 0, 1], [1, 0, 1, 0, 1]))