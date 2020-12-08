import pickle

file='2016.pkl'
with open(file, 'rb') as fo:
    dict = pickle.load(fo)
    print(dict)

