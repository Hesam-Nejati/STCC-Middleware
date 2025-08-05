import matplotlib.pyplot as plt

# تنظیمات خروجی برداری هماهنگ با لاتک
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

# داده‌ها
x = [0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00]
latency_all = [110, 116, 120, 130, 140, 150, 160, 170]
latency_quorum = [85, 90, 98, 102, 112, 116, 120, 124]
latency_one = [44, 54, 64, 70, 76, 82, 88, 94]

fig, ax = plt.subplots(figsize=(7, 5))

ax.plot(x, latency_all, marker='o', label=r'Consistency ALL', color='gold', linewidth=1.5, markersize=6)
ax.plot(x, latency_quorum, marker='s', label=r'Consistency Quorum', color='orange', linewidth=1.5, markersize=6)
ax.plot(x, latency_one, marker='^', label=r'Consistency ONE', color='red', linewidth=1.5, markersize=6)

ax.set_xlabel(r'Workload Size ($\times 10^6$ Operations)')
ax.set_ylabel(r'Network Latency (ms) [mean or 95$^{\rm th}$ percentile]')

ax.set_title(
    r'Network Latency vs. Workload Size' + '\n' +
    r'Workload-C, Replication Factor: Full',
    pad=20,
    loc='center'
)

ax.grid(True, which='both', linestyle='--', color='gray', alpha=0.5, linewidth=0.5)
ax.legend(loc='best')

# 1e6 زیر محور 2.00
ax.text(2.00, ax.get_ylim()[0] - (ax.get_ylim()[1] * 0.1), r'$10^6$', ha='center')

plt.tight_layout()

# نمایش
plt.show()

# ذخیره خروجی برداری
# plt.savefig('network_latency_workload_c.pdf', bbox_inches='tight')
# plt.savefig('network_latency_workload_c.pgf', bbox_inches='tight')
