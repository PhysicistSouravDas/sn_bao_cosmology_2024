import numpy as np
import matplotlib.pyplot as plt

# Probability function (target distribution) - Gaussian (Normal) Distribution
def p(x, mu=0, sigma=1):
    # Gaussian probability density function (PDF)
    return (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def metropolis_hastings_gaussian(n, burnin, delta, mu, sigma):
    x = np.zeros(n-burnin)

    # running Metropolis-Hastings algorithm
    x0 = 100  # Initial state
    for i in range(n):
        r = np.random.random()
        dx = (2 * r - 1) * delta  # proposal step
        xtest = x0 + dx
        w = p(xtest, mu, sigma) / p(x0, mu, sigma)  # acceptance ratio

        if w >= 1.0:
            x1 = xtest
        else:
            r = np.random.random()
            if r <= w:
                x1 = xtest
            else:
                x1 = x0

        x0 = x1
        if i >= burnin:
            x[i-burnin] = x1  # Save the result after "burn-in" period
    
    return x

# Running the program
if __name__ == "__main__":
    # Generate samples from Gaussian distribution using Metropolis-Hastings
    # dist = metropolis_hastings_gaussian(n=110000, burnin=10000, delta=0.3, mu=0, sigma=1)
    dist = metropolis_hastings_gaussian(n=1000, burnin=100, delta=10, mu=0, sigma=10)
    
    # Plot the resulting distribution
    plt.figure(figsize=(18,9))
    plt.subplot(2, 1, 1)
    plt.hist(dist, label="Sampled Gaussian Distribution", bins=50, density=True)
    xx = np.linspace(-30, 30, 1000)
    plt.plot(xx, p(xx, mu=0, sigma=10), label="Normal distribution model")
    plt.title("Gaussian Distribution using Metropolis-Hastings")
    plt.xlabel("x")
    plt.ylabel("Probability Density")
    plt.grid(True)
    plt.legend(loc='upper right')

    plt.subplot(2, 1, 2)
    plt.plot(dist)
    plt.xlabel("# mcmc cycle")
    plt.ylabel("walker position")
    plt.show()
