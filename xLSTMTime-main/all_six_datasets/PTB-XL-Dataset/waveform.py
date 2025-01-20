import wfdb
import matplotlib.pyplot as plt

# Specify the record name (without file extension)
record_name = '00000/00001_hr'  # Replace with the actual record name

# Load the ECG record
record = wfdb.rdrecord(f'PTB-XL-Dataset/records500/{record_name}')

# Plot the ECG waveform
plt.figure(figsize=(15, 6))
wfdb.plot_wfdb(record, title=f'ECG Waveform for {record_name}', time_units='seconds')
plt.show()
