import matplotlib.pyplot as plt
import numpy as np

# تنظیمات برای خروجی برداری با کیفیت عالی و هماهنگ با لاتک
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

throughput_all = np.array([3826, 3995, 4188, 4474, 4749, 4957, 5139, 5418, 5709, 5948, 4991, 5877, 5116, 3664])
throughput_quorum = np.array([4489, 4673, 4912, 5088, 5289, 5524, 5871, 5924, 6017, 6179, 5593, 6318, 5844, 4039])
throughput_one = np.array([4963, 5119, 5358, 5562, 5789, 5995, 6102, 6384, 6481, 6568, 6024, 6786, 6142, 4399])

fig, ax = plt.subplots(figsize=(7, 5))

bars1 = ax.bar(x - width, throughput_all, width, yerr=0.02 * throughput_all, capsize=4,
               color='lightskyblue', edgecolor='black', linewidth=1, label='ALL')
bars2 = ax.bar(x, throughput_quorum, width, yerr=0.02 * throughput_quorum, capsize=4,
               color='palegreen', edgecolor='black', linewidth=1, label='Quorum')
bars3 = ax.bar(x + width, throughput_one, width, yerr=0.02 * throughput_one, capsize=4,
               color='moccasin', edgecolor='black', linewidth=1, label='ONE')

ax.set_title(r'Throughput for Workload-B at 2{,}000{,}000 Operations', pad=20)
ax.set_ylabel(r'System Throughput (ops/sec)')

# برچسب‌های محور X بماند
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')

# حذف عنوان محور X
ax.set_xlabel('')

ax.set_ylim(0, 7000)
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
# plt.savefig("figure_throughput_workload_b.pdf", bbox_inches='tight')
# یا
# plt.savefig("figure_throughput_workload_b.pgf", bbox_inches='tight')
