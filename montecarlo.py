import numpy as np
import random

def main():
    circle = 0
    computed_pi = 0
    num_samples = 5000000 #2-3 decimals
    x, y = gen_rand(num_samples)
    for i in range(num_samples):
        r = (x[i]**2 + y[i]**2)**0.5
        if r <= 1:
            circle += 1
    computed_pi = 4 * circle / num_samples #Area of circle  / Area of Square = pi / 4
    return computed_pi, num_samples


def gen_rand(num_samples):
    x = np.random.uniform(-1,1,num_samples)
    y = np.random.uniform(-1,1,num_samples)
    return x, y


if __name__ == "__main__":
    computed_value_pi, num_samples = main()
    print(f'The computed value of pi with {num_samples} samples is {computed_value_pi}')
