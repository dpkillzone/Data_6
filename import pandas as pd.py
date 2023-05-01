import matplotlib.pyplot as plt
import pandas as pd

# Indlæs data fra CSV-fil
data = pd.read_csv('periodic_table.csv')

# Opret histogram
plt.hist(data['group'], bins=18, range=(0.5, 18.5))

# Tilføj aksetitler og en titel
plt.xlabel('Gruppe')
plt.ylabel('Antal grundstoffer')
plt.title('Antal grundstoffer i hver gruppe')

# Gruppér data efter periode og gruppe og tæl antallet af grundstoffer
counts = data.groupby(['period', 'group'])['name'].count().unstack()

# Opret søjlediagram
counts.plot(kind='bar', stacked=True)

# Tilføj aksetitler og en titel
plt.xlabel('Periode')
plt.ylabel('Antal grundstoffer')
plt.title('Antal grundstoffer i hver periode og gruppe')

# Opret scatter plot
plt.scatter(data['atomic_radius'], data['electronegativity'], s=data['molar_heat'], alpha=0.5)

# Tilføj aksetitler og en titel
plt.xlabel('Atomradius')
plt.ylabel('Elektronegativitet')
plt.title('Sammenhæng mellem atomradius, elektronegativitet og molar varmekapacitet')
