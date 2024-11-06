import numpy as np # type: ignore

# Define system matrices
A = np.array([[1, 1], [0, 1]])   # State transition matrix
H = np.array([[1, 0]])           # Measurement matrix
Q = np.array([[0.01, 0], [0, 0.01]]) # Process noise covariance
R = np.array([[0.1]])            # Measurement noise covariance
B = np.array([[0.5], [1]])       # Control matrix
u = 1                            # Control input

# Initial guesses
x_est = np.array([[0], [0]])     # Initial state estimate
P = np.eye(2)                    # Initial error covariance

# Measurements (example)
z = [1.1, 2.0, 2.9, 4.1, 4.9, 6.0]

for k in range(len(z)):
    # Prediction step
    x_pred = A @ x_est + B * u
    P_pred = A @ P @ A.T + Q

    # Update step
    K = P_pred @ H.T @ np.linalg.inv(H @ P_pred @ H.T + R)
    x_est = x_pred + K @ (z[k] - H @ x_pred)
    P = (np.eye(2) - K @ H) @ P_pred

    print(f"Estimate at step {k+1}: {x_est.flatten()}")
