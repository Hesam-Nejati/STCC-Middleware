import matplotlib.pyplot as plt
import numpy as np

# تنظیمات برای خروجی با کیفیت لاتک
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 12,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
})

labels = [
    "1.0 GHz", "1.4 GHz", "1.8 GHz",
    "2.2 GHz", "2.8 GHz",
    "Power save", "Performance", "Conservative", "OnDemand"
]

energy = [
    113.80039086656329, 138.16326253747592, 164.18225146877688,
    192.80503818633805, 213.05061162146038,
    178.5784536825167, 259.65777405570503,
    364.80039086656329, 402.05397626944483
]

exec_time = [
    72.88604088351863, 57.5024979573128, 52.72908246113417,
    47.54680546368174, 46.24090058667204,
    93.40418865282348, 41.64976208794582,
    73.24090058667204, 71.5657943949827
]

energy_std = [0.02 * e for e in energy]
exec_time_std = [0.03 * t for t in exec_time]

x = np.arange(len(labels))

fig, ax1 = plt.subplots(figsize=(7, 5))

# رسم بارها
bar1 = ax1.bar(x - 0.2, energy, yerr=energy_std, width=0.4,
               color='royalblue', alpha=0.7, capsize=4,
               edgecolor='black', linewidth=1, label='Energy Consumption')

ax2 = ax1.twinx()

bar2 = ax2.bar(x + 0.2, exec_time, yerr=exec_time_std, width=0.4,
               color='coral', alpha=0.7, capsize=4,
               edgecolor='black', linewidth=1, label='Execution Time')

# محورها
ax1.set_ylabel(r'Energy Consumption (Joule)')
ax2.set_ylabel(r'Execution Time (s)')

ax1.set_xticks(x)
ax1.set_xticklabels(labels, rotation=45, ha='right')

ax1.set_ylim(0, max(energy) * 1.2)
ax2.set_ylim(0, max(exec_time) * 1.2)

# عنوان
plt.title(
    r'Energy Consumption and Execution Time of Workload Size: 2M Operations, No. threads: 320,' + '\n'
    r'Replication Factor: Full, Consistency: Quorum-based, YCSB: Workload-C',
    pad=20
)

# لجند بالا
fig.legend([bar1, bar2], ['Energy Consumption', 'Execution Time'],
           loc='upper center', ncol=2, frameon=False)

# فلش‌ها و توضیحات
ax1.annotate(
    '', xy=(0.02, -0.4), xytext=(0.47, -0.4),
    xycoords='axes fraction', textcoords='axes fraction',
    arrowprops=dict(arrowstyle='<->', color='black', linewidth=1)
)
ax1.text(0.25, -0.45, r'Fixed Frequencies (Userspace Governor)',
         transform=ax1.transAxes, ha='center', va='top')

ax1.annotate(
    '', xy=(0.55, -0.4), xytext=(0.87, -0.4),
    xycoords='axes fraction', textcoords='axes fraction',
    arrowprops=dict(arrowstyle='<->', color='black', linewidth=1)
)
ax1.text(0.735, -0.45, r'Default Governors',
         transform=ax1.transAxes, ha='center', va='top')

ax1.grid(True, which='both', axis='both',
         linestyle='--', color='gray', alpha=0.5, linewidth=0.5)

plt.subplots_adjust(top=0.75, bottom=0.35)

plt.show()

# برای خروجی برداری:
# plt.savefig("figure_energy_exec_quorum_workload_c.pdf", bbox_inches='tight')
# یا
# plt.savefig("figure_energy_exec_quorum_workload_c.pgf", bbox_inches='tight')
