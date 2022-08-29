def create_sample_data():
    new_rows = [('CA',22, 45000),("WA",35,65000) ,("WA",50,85000)]
    demo_df = spark.createDataFrame(new_rows, ['state', 'age', 'salary'])
    demo_df.show()
#create_sample_data()

