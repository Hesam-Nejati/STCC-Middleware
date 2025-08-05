import matplotlib.pyplot as plt
import numpy as np

# تنظیمات برای خروجی هماهنگ با لاتک
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
    "Ondemand", "Performance", "Conservative", "Powersave"
]

x = np.arange(len(labels))
width = 0.25

throughput_all = np.array([4583, 4752, 4933, 5124, 5389, 5617, 5886, 5997, 6129, 6347, 5803, 6457, 5964, 4209])
throughput_quorum = np.array([5009, 5183, 5417, 5398, 5868, 6018, 6219, 6429, 6671, 6895, 6215, 7005, 6355, 4706])
throughput_one = np.array([5384, 5692, 5937, 6044, 6195, 6292, 6483, 6886, 7017, 7153, 6568, 7354, 6720, 4963])

fig, ax = plt.subplots(figsize=(7, 5))

bars1 = ax.bar(x - width, throughput_all, width, yerr=0.02 * throughput_all, capsize=4,
               color='lightskyblue', edgecolor='black', linewidth=1, label='ALL')
bars2 = ax.bar(x, throughput_quorum, width, yerr=0.02 * throughput_quorum, capsize=4,
               color='palegreen', edgecolor='black', linewidth=1, label='Quorum')
bars3 = ax.bar(x + width, throughput_one, width, yerr=0.02 * throughput_one, capsize=4,
               color='moccasin', edgecolor='black', linewidth=1, label='ONE')

ax.set_title(r'Throughput for Workload-C at 2{,}000{,}000 Operations', pad=20)
ax.set_ylabel(r'System Throughput (ops/sec)')

# برچسب‌های محور X بماند
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')

# حذف عنوان محور X
ax.set_xlabel('')

ax.set_ylim(0, 8000)
ax.legend(loc='best', facecolor='white', edgecolor='black')

# فلش‌ها و توضیحات
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

ax.yaxis.grid(True, linestyle='--', color='gray', alpha=0.3, linewidth=0.5)

plt.subplots_adjust(top=0.85, bottom=0.35)

plt.show()

# برای خروجی برداری:
# plt.savefig("figure_throughput_workload_c.pdf", bbox_inches='tight')
# یا
# plt.savefig("figure_throughput_workload_c.pgf", bbox_inches='tight')
