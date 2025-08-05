import matplotlib.pyplot as plt
import numpy as np

# تنظیمات LaTeX برای یکپارچگی فونت با لاتک
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
    "1.0 GHz", "1.2 GHz", "1.4 GHz", "1.6 GHz", "1.8 GHz",
    "2.0 GHz", "2.2 GHz", "2.4 GHz", "2.6 GHz", "2.8 GHz",
    "Power save", "Performance", "Conservative", "OnDemand"
]

x = np.arange(len(labels))
width = 0.25

power_all = [16, 21, 28, 32, 34, 36, 39, 41, 43, 47, 32, 56, 43, 35]
power_quorum = [14, 19, 22, 25, 29, 32, 34, 37, 41, 42, 27, 49, 38, 28]
power_one = [11, 16, 18, 21, 23, 26, 29, 30, 33, 32, 24, 39, 32, 25]
power_std = [0.025] * len(labels)

# ابعاد بزرگ برای خروجی برداری
fig, ax = plt.subplots(figsize=(7, 5))

# بارها
bar1 = ax.bar(x - width, power_all, width, yerr=power_std, capsize=4,
              color='lightskyblue', edgecolor='black', linewidth=1, label='Consistency ALL')
bar2 = ax.bar(x, power_quorum, width, yerr=power_std, capsize=4,
              color='palegreen', edgecolor='black', linewidth=1, label='Consistency Quorum')
bar3 = ax.bar(x + width, power_one, width, yerr=power_std, capsize=4,
              color='moccasin', edgecolor='black', linewidth=1, label='Consistency ONE')

# محورها
ax.set_ylabel(r'Dynamic Power (Watt)')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')

# عنوان
plt.title(
    r'Dynamic Power Consumption of Workload Size: 250K operations, No. threads: 160,' + '\n'
    r'Replication Factor: Partial, YCSB: Workload-A',
    pad=20
)

# لجند
ax.legend(loc='upper left', facecolor='white', edgecolor='black')

# فلش‌ها
ax.annotate(
    '', xy=(0.02, -0.4), xytext=(0.62, -0.4),
    xycoords='axes fraction', textcoords='axes fraction',
    arrowprops=dict(arrowstyle='<->', color='black', linewidth=1)
)
ax.text(0.35, -0.45, r'Fixed Frequencies (Userspace Governor)',
        transform=ax.transAxes, ha='center', va='top')

ax.annotate(
    '', xy=(0.65, -0.4), xytext=(0.97, -0.4),
    xycoords='axes fraction', textcoords='axes fraction',
    arrowprops=dict(arrowstyle='<->', color='black', linewidth=1)
)
ax.text(0.835, -0.45, r'Default Governors',
        transform=ax.transAxes, ha='center', va='top')

# گرید
ax.grid(True, linestyle='--', color='gray', alpha=0.3, linewidth=0.5)

# چیدمان بهینه
plt.subplots_adjust(top=0.75, bottom=0.35)

plt.show()

# خروجی برداری (زمانی که خواستی ذخیره کنی)
# plt.savefig("figure_workload_a_partial.pdf", bbox_inches='tight')
# یا plt.savefig("figure_workload_a_partial.pgf", bbox_inches='tight')
