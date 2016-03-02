import pickle
def unpickle(file):
    with open(file, 'rb') as f:
        u = pickle._Unpickler(f)
        u.encoding = 'latin1'
        return u.load()    
    
if __name__ == '__main__':
    batch = unpickle('cifar-10-batches-py/data_batch_1')