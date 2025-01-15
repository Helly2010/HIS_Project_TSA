import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import wfdb

# Load the metadata
data = pd.read_csv('PTB-XL-Dataset/ptbxl_database.csv')

# Visualize age distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='age', kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Visualize sex distribution
plt.figure(figsize=(8, 6))
data['sex'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Sex Distribution')
plt.ylabel('')
plt.show()

# Visualize diagnostic superclasses
superclasses = data['scp_codes'].apply(lambda x: eval(x)).apply(lambda x: [k.split('_')[0] for k in x.keys()])
superclass_counts = pd.Series([item for sublist in superclasses for item in sublist]).value_counts()

plt.figure(figsize=(12, 6))
superclass_counts.plot(kind='bar')
plt.title('Distribution of Diagnostic Superclasses')
plt.xlabel('Superclass')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualize an ECG waveform
record_name = data['filename_hr'].iloc[0].split('/')[-1].split('.')[0]
record = wfdb.rdrecord(f'PTB-XL-Dataset/records500/00000/{record_name}')

plt.figure(figsize=(20, 10))
wfdb.plot_wfdb(record, title='Sample ECG Waveform')
plt.show()
