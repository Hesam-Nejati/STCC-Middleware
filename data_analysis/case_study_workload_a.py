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

# انرژی (Joule)
energy = [
    220.0, 260.0, 300.0, 340.0,
    370.0, 400.0, 420.0, 440.0,
    450.0, 460.0, 320.0, 455.0,
    440.0, 450.0
]

# زمان اجرا (seconds)
exec_time = [
    420.0, 390.0, 370.0, 350.0,
    330.0, 310.0, 295.0, 280.0,
    265.0, 250.0, 360.0, 240.0,
    260.0, 270.0
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
    r'Replication Factor: Full, Consistency: Quorum-based, YCSB: Workload-A',
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
#plt.savefig("energy_exec_time_workload_c.pdf", bbox_inches="tight", dpi=600)
#plt.savefig("energy_exec_time_workload_c.pgf", bbox_inches="tight", dpi=600)
plt.show()
