import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) 

x = np.linspace(1, 10, 30)        
noise = np.random.randn(30) * 2   
y = 5 * x + 7 + noise             
print("Hours Studied (X):")
print(x)
print("\nMarks Scored (Y):")
print(y)



x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)

m = numerator / denominator



b = y_mean - m * x_mean

print(f"\nSlope (m)     = {m:.4f}")
print(f"Intercept (b) = {b:.4f}")
print(f"\nFinal Equation: y = {m:.4f} * x + {b:.4f}")



def predict(x_value):
    return m * x_value + b

y_pred = predict(x)

print("\nPredicted Marks (Y_pred):")
print(y_pred)


new_hours = 6.5
print(f"\nPredicted marks for a student who studied {new_hours} hours = {predict(new_hours):.2f}")



mse = np.mean((y - y_pred) ** 2)
print(f"\nMean Squared Error (MSE) = {mse:.4f}")



plt.figure(figsize=(8, 6))
plt.scatter(x, y, color="blue", label="Actual Data")
plt.plot(x, y_pred, color="red", linewidth=2, label="Regression Line (Our Model)")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.title("Linear Regression from Scratch (NumPy only)")
plt.legend()
plt.grid(True)
plt.savefig("linear_regression_output.png")
plt.show()
