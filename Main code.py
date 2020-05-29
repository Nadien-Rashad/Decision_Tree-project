if __name__ == '__main__':

    csv_file = input("Train File: ")  # input trained data file
    df = pd.read_csv(csv_file)
    trainedData = df.values.tolist()

    csv_file_dev = input("Dev File: ")  # input file to calculate accuracy
    dev_df = pd.read_csv(csv_file_dev)
    Data_from_dev = dev_df.values.tolist()

    csv_file_test = input("Test File: ")  # input tested data
    test_df = pd.read_csv(csv_file_test)
    Data_from_test = test_df.values.tolist()

    start_time = {datetime.datetime.now().strftime('%H:%M:%S')}
    print(f"Training Process start at: {start_time}")
    tree = BuildTree(trainedData)

    print(f"Training Process End at: {datetime.datetime.now().strftime('%H:%M:%S')}")
    print("  ")


    rows=GetList(Data_from_dev,tree)
    df = pd.DataFrame(rows, columns=["rating"])
    #print(df)
    df.to_csv('devList.csv', index=False)

    rating = pd.read_csv('devList.csv').values.tolist()


    predicted_rating = The_Counts(rating)
    actual_rating = The_Counts(Data_from_dev)

    print("******* Evaluation of dev_file data *******")
    print(f' actual rating => {actual_rating}')
    print(f' predicted rating => {predicted_rating}')

    accuracy = calculate_accuracy(predicted_rating,actual_rating)


    print(f' Accuracy is {round(accuracy)}%')




    rows=GetList(Data_from_test,tree)
    df = pd.DataFrame(rows, columns=["rating"])

    df.to_csv('testList.csv', index=False)
    test_rating = pd.read_csv('testList.csv').values.tolist()
    testedResult = The_Counts(test_rating)

    print(" ")
    print("******* Predicted data of test_file *******")
    print(testedResult)
