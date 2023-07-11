import pandas
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        data = pandas.read_csv(self.filename)
        return data.to_dict(orient="records")

    def upload_data(self, data):
        pandas.DataFrame(data).to_csv(
            self.filename,
            index=False
        )
