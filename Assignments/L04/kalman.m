
A = [1, 1; 0, 1]; % State transition matrix
B = [0.5; 1];     % Control input matrix
H = [1, 0];       % Measurement matrix
Q = [0.1, 0; 0, 0.1]; % Process noise covariance
R = 1;               % Measurement noise covariance
x = [0; 1];         % Initial state [position; velocity]
P = eye(2);         % Initial covariance

num_steps = 50;
for k = 1:num_steps % kalman filter loop
    % Prediction step
    x = A * x + B * 0;  % Assuming no control input
    P = A * P * A' + Q;

    % Measurement with noise
    z = H * x + sqrt(R) * randn;

    % Kalman Gain
    K = P * H' / (H * P * H' + R);

    % Update step
    x = x + K * (z - H * x);
    P = (eye(2) - K * H) * P;

    disp(x); % Display the estimated state
end
