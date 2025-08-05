import matplotlib.pyplot as plt
import numpy as np

# تنظیمات برای خروجی با کیفیت و فونت یکدست با لاتک
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

power_all = [18, 22, 24, 27, 31, 34, 37, 40, 43, 45, 33, 48, 42, 35]
power_quorum = [15, 17, 20, 23, 26, 29, 31, 34, 37, 40, 27, 44, 39, 28]
power_one = [11, 14, 18, 20, 23, 26, 28, 30, 32, 34, 25, 38, 32, 25]
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

# محورهای نمودار
ax.set_ylabel(r'Dynamic Power (Watt)')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')

# عنوان
plt.title(
    r'Dynamic Power Consumption of Workload Size: 250K operations, No. threads: 160,' + '\n'
    r'Replication Factor: Partial, YCSB: Workload-C',
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

plt.subplots_adjust(top=0.75, bottom=0.35)

plt.show()

# خروجی برداری وقتی خواستی ذخیره کنی:
# plt.savefig("figure_workload_c_partial.pdf", bbox_inches='tight')
# یا plt.savefig("figure_workload_c_partial.pgf", bbox_inches='tight')
