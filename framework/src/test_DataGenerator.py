import os
import shutil
import DataGenUtil
import ContosoDataGenerator
import M365DataGenerator
import MSInsightsDataGenerator
#import OneRosterDataGenerator

destination = 'tmp_generated_data'
if os.path.exists(destination): shutil.rmtree(destination)
os.makedirs(destination)

def test_ContosoDataGenerator():
    dg = ContosoDataGenerator.ContosoDataGenerator()
    writer = DataGenUtil.FileWriter(destination)
    dg.generate_data(2, writer)
    
def test_M365DataGenerator():
    dg = M365DataGenerator.M365DataGenerator()
    writer = DataGenUtil.FileWriter(destination)
    dg.generate_data(1, writer)
    
def test_MSInsightsDataGenerator():
    dg = MSInsightsDataGenerator.MSInsightsDataGenerator()
    writer = DataGenUtil.FileWriter(destination)
    dg.generate_data(2, writer)

#test_ContosoDataGenerator()
test_M365DataGenerator()
#test_MSInsightsDataGenerator()