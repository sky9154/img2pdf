class Config:

  def __init__(self):
    self.WINDOW = {
        'APP_NAME': 'Image to PDF Converter',
        'STYLE': 'Breeze',
        'WIDTH': 350,
        'HEIGHT': 230
    }

    self.WIDGET = {
        'DIALOG': {
            'PDF': 'Select PDF Folder',
            'STORAGE': 'Choose Storage Location'
        }
    }

    self.config = {'WINDOW': self.WINDOW, 'WIDGET': self.WIDGET}

  def __getitem__(self, item):
    return self.config[item]
