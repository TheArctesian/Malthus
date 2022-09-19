from coalas import csvReader as c

if __name__ == "__main__":
    c.importCSV('global-food.csv')
    c.printHeaders()
