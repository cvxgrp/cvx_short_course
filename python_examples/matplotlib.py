# Plot the train and test error over the trade-off curve.
import matplotlib.pyplot as plt
plt.plot(lambda_vals, train_error, label="Train error")
plt.plot(lambda_vals, test_error, label="Test error")
plt.xscale('log')
plt.xlabel(r"$\lambda$", fontsize=16)
plt.show()
