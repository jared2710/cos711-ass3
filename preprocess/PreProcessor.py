import pandas as pd
import numpy as np

class PreProcessor():
    def __init__(self):
        self.sensor_column_names = [    'ID','location','loc_altitude','km2','aspect','dist_motorway','dist_trunk','dist_primary',
                                        'dist_secondary','dist_tertiary','dist_unclassified','dist_residential','popn','hh',
                                        'hh_cook_charcoal','hh_cook_firewood','hh_burn_waste'] 
        
        self.dataset_column_names = [   'ID','location','temp','precip','rel_humidity',
                                        'wind_dir','wind_spd','atmos_press','target']
    
    def print(self):
        print("PreProcessor")
        
    def fetchFromFiles(self):
        raw_dataset = pd.read_csv("data/airqo_metadata.csv", names=self.sensor_column_names,
                          na_values = "?", comment='\t',
                          sep=",", skiprows=1)
        sensors = raw_dataset.copy()
        sensors.pop("dist_motorway")
        self.sensor_column_names.remove("dist_motorway")
        print(sensors)
        sensors = sensors.fillna(sensors.mean())
        print(sensors)
        
                    
                                        
        self.sensor_column_names_input = self.sensor_column_names[2:]
        self.len_sensor_column_names_input = len(self.sensor_column_names_input)


        self.sensor_arr = {}
        for i in range(len(sensors)):
            #print(sensors.iloc[i])
            #print(sensors.iloc[i]['location'])
            self.sensor_arr[sensors.iloc[i]['location']] = sensors.iloc[i]
        #print(self.sensor_arr)
        
        
        
        raw_dataset = pd.read_csv("data/Train.csv", names=self.dataset_column_names,
                              na_values = "?", comment='\t',
                              sep=",", skiprows=1)
        self.dataset = raw_dataset.copy()
        print(len(self.dataset))
        #self.dataset = self.dataset[:100]
        print(self.dataset.head())
        
        
                                        
        self.dataset_column_names_input = self.dataset_column_names[2:8]
        self.len_dataset_column_names_input = len(self.dataset_column_names_input)
        
        self.dataset_array = np.empty([len(self.dataset),121,(self.len_dataset_column_names_input+self.len_sensor_column_names_input+1)])
        
        
    def convertCSVReadToNumpy(self):
        self.target_array_old = np.array(self.dataset['target'])
        self.target_array = np.empty([len(self.target_array_old), 1])
        for i in range(len(self.target_array_old)):
            self.target_array[i][0] = self.target_array_old[i]
        self.target_array_old = []
        
        for i in range(len(self.dataset)):
            print(i)
            #print(dataset.iloc[i])
            #print(dataset_array[i])
           
            this_sensor = self.sensor_arr[self.dataset.iloc[i]['location']]
            #print(this_sensor)
            
            value_arr = [[]] * self.len_dataset_column_names_input
            
            count = 0
            for j in range(self.len_dataset_column_names_input):
                column_name = self.dataset_column_names_input[j]
                csv = self.dataset.iloc[i][column_name]
                #csv = csv.replace("nan", "0.0")
                #print(csv)
                value_arr[j] = csv.split(",")
                #print(value_arr[j])
                value_arr[j] = np.array(value_arr[j])
                #print(value_arr[j])
                value_arr[j] = value_arr[j].astype(np.float)
                #print(value_arr[j])
                #print("nan")
                #print(np.isnan(value_arr[j]))
                #print(True in np.isnan(value_arr[j]))
                
                if(True in np.isnan(value_arr[j])):
                    count += 1
                
                value_arr[j][np.isnan(value_arr[j])] = np.nanmean(value_arr[j])
                #value_arr[j][np.isnan(value_arr[j])] = 0
                #print(value_arr[j])
            #print("numWithNan", count)
                
                
                
            
                
            num_hours = len(value_arr[0])
            
            for j in range(num_hours):
                #print(self.dataset_array[i][j])
                for k in range(self.len_dataset_column_names_input):
                    self.dataset_array[i][j][k] = value_arr[k][j]#(0.0 if value_arr[k][j] == "nan" else value_arr[k][j])
                #print(self.dataset_array[i][j])
                    
                for k in range(self.len_sensor_column_names_input):
                    self.dataset_array[i][j][self.len_dataset_column_names_input + k] = this_sensor[self.sensor_column_names_input[k]]
                #print(self.dataset_array[i][j])
                
                self.dataset_array[i][j][self.len_dataset_column_names_input + self.len_sensor_column_names_input] = 6-count
                
                #print(self.dataset_array[i][j])
                
    def normalizeNumpyArray(self):
        for k in range(len(self.dataset_array[0][0])):
            max = self.dataset_array[0][0][k]
            min = self.dataset_array[0][0][k]
            for j in range(len(self.dataset_array[0])):
                for i in range(len(self.dataset_array)):
                    val = self.dataset_array[i][j][k]
                    if(val > max):
                        max = val
                    if(val < min):
                        min = val
            
            diff = max - min
            for j in range(len(self.dataset_array[0])):
                for i in range(len(self.dataset_array)):
                    self.dataset_array[i][j][k] = (self.dataset_array[i][j][k]-min)/(diff)
                    #print(self.dataset_array[i][j][k])
                
    def saveToFile(self):
        np.save('data/dataset_array', self.dataset_array)
        np.save('data/target_array', self.target_array)