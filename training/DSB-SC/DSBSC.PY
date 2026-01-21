import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a time base
t = np.linspace(0, 0.05, 1000)   # 0 to 0.05 sec, 1000 points

# Step 2: Create a message signal (low frequency)
fm = 50   # message frequency = 50 Hz
m = np.sin(2 * np.pi * fm * t)   # message signal

# Step 3: Create a carrier signal (high frequency)
fc = 500   # carrier frequency = 500 Hz
c = np.cos(2 * np.pi * fc * t)   # carrier signal

# Step 4: DSB-SC Modulation (multiply message and carrier)
s = m * c   # modulated signal

# Step 5: Demodulation (multiply again with carrier)
demod = s * c

# Step 6: Low-pass filter (approximation using np.convolve)
# This removes high-frequency parts and keeps the original message
from scipy.signal import butter, filtfilt
b, a = butter(5, 0.1)             # design a low-pass filter
m_rec = filtfilt(b, a, demod)     # recovered message

# Step 7: Plot all signals
plt.figure(figsize=(10,8))

plt.subplot(4,1,1)
plt.title("Message Signal m(t)")
plt.plot(t, m)
plt.grid(True)

plt.subplot(4,1,2)
plt.title("Carrier Signal c(t)")
plt.plot(t, c)
plt.grid(True)

plt.subplot(4,1,3)
plt.title("DSB-SC Modulated Signal s(t)")
plt.plot(t, s)
plt.grid(True)

plt.subplot(4,1,4)
plt.title("Recovered Message Signal after Demodulation")
plt.plot(t, m_rec)
plt.grid(True)

plt.tight_layout()
plt.show()
