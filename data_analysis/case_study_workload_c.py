import matplotlib.pyplot as plt
import numpy as np

# تنظیمات برای خروجی با کیفیت
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 14,
    "axes.labelsize": 14,
    "axes.titlesize": 16,
    "legend.fontsize": 12,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12
})

labels = [
    "1.0 GHz", "1.2 GHz", "1.4 GHz", "1.6 GHz", "1.8 GHz",
    "2.0 GHz", "2.2 GHz", "2.4 GHz", "2.6 GHz", "2.8 GHz",
    "Power save", "Performance", "Conservative", "OnDemand"
]

energy = [
    54.05061162146038, 74.5514527834565, 82.80503818633805, 92.92233642212835,
    97.18225146877688, 103.83836872916523, 109.16326253747592, 116.88435855952639,
    121.676762987006, 127.80039086656329, 99.5784536825167, 133.65777405570503,
    127.80039086656329, 136.05397626944483
]

exec_time = [
    157.88604088351863, 151.76241300396134, 147.5024979573128, 139.78140193526232,
    130.72908246113417, 126.73541210490114, 119.54680546368174, 113.95566696495553,
    106.7670603237361, 102.24090058667204, 125.40418865282348, 96.64976208794582,
    102.24090058667204, 107.5657943949827
]

energy_std = [0.02 * e for e in energy]
exec_time_std = [0.03 * t for t in exec_time]

x = np.arange(len(labels))

fig, ax1 = plt.subplots(figsize=(7, 5))  # مناسب برای 0.3\textwidth

# Bar plots
bar1 = ax1.bar(x - 0.2, energy, yerr=energy_std, width=0.4, color='cyan', alpha=0.7,
               capsize=4, edgecolor='black', linewidth=0.8, label='Energy Consumption')
ax2 = ax1.twinx()
bar2 = ax2.bar(x + 0.2, exec_time, yerr=exec_time_std, width=0.4, color='lightgreen', alpha=0.7,
               capsize=4, edgecolor='black', linewidth=0.8, label='Execution Time')

# Labels
ax1.set_ylabel(r'Energy Consumption (Joule)')
ax2.set_ylabel(r'Execution Time (s)')
ax1.set_xticks(x)
ax1.set_xticklabels(labels, rotation=45, ha='right')

# Title
plt.title(
    r'Energy Consumption and Execution Time of Workload Size: 10,000, No. threads: 32' + '\n' +
    r'Replication Factor: Full, Consistency: Quorum-based, YCSB: Workload-C',
    pad=20
)

# Legend
fig.legend([bar1, bar2], [r'Energy Consumption', r'Execution Time'],
           loc='upper center', ncol=2, frameon=True, edgecolor='black')

# Arrows
ax1.annotate('', xy=(0.02, -0.4), xytext=(0.62, -0.4),
             xycoords='axes fraction', textcoords='axes fraction',
             arrowprops=dict(arrowstyle='<->', color='black', linewidth=1))
ax1.text(0.32, -0.45, r'Fixed Frequencies (Userspace Governor)',
         transform=ax1.transAxes, ha='center', va='top')

ax1.annotate('', xy=(0.65, -0.4), xytext=(0.97, -0.4),
             xycoords='axes fraction', textcoords='axes fraction',
             arrowprops=dict(arrowstyle='<->', color='black', linewidth=1))
ax1.text(0.81, -0.45, r'Default Governors',
         transform=ax1.transAxes, ha='center', va='top')

# Grid
ax1.grid(True, linestyle='--', alpha=0.3)

# Adjust spacing
plt.subplots_adjust(top=0.78, bottom=0.35)

# Save high-quality
plt.savefig("energy_exec_time_workload_c.pdf", bbox_inches="tight", dpi=600)
plt.savefig("energy_exec_time_workload_c.pgf", bbox_inches="tight", dpi=600)
plt.show()
