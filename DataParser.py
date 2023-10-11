class DataParser:
    def __init__(self, fileName):
        self.folderPath = "NN_HW1_DataSet/basic/"
        self.filepath = self.folderPath + fileName
        self.X = []
        self.Y = []
        self._parse_data()

    def _parse_data(self):
        with open(self.filepath, 'r') as f:
            for line in f.readlines():
                data = line.split()
                x_val = [float(data[0]), float(data[1])]
                y_val = int(data[2])

                self.X.append(x_val)
                self.Y.append(y_val)