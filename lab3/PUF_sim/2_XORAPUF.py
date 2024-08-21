import numpy as np

class XORPUF_2XOR():
    def __init__(self, weight, noise=0.0):
        self.weight = weight
        self.noise = noise
    
    def getResponse(self, phi):
        weight = self.weight + \
            np.random.normal(0, self.noise, size=self.weight.shape)
        outs = np.sum(phi * weight, axis=-1, keepdims=False)
        res = int(outs[0] >= 0) ^ int(outs[1] >= 0)
        return res
    
    def randomSample(Xnum, length=32, alpha=0.05, noise=0.0):
        weight = np.random.normal(0, alpha, size=(Xnum, length + 1))
        return XORPUF_2XOR(weight, alpha * noise)
