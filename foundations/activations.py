import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))   
        x =  1 / (1 + np.exp(-z))
        return (np.round(x,5))
        # return np.round(your_answer, 5)
        pass

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:

        return np.maximum(0, z)
        pass

z =np.array([-1.0,0,1])
sol = Solution()
print(sol.sigmoid(z))

z = np.array([-3.0, -1.0, 0.0, 2.0, 5.0])

print(sol.relu(z))