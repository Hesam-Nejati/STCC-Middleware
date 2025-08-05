import matplotlib.pyplot as plt

# تنظیمات برای خروجی با کیفیت و فونت هماهنگ با لاتک
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
latency_all = [121, 148, 173, 192, 213, 226, 238, 251]
latency_quorum = [80, 100, 120, 135, 145, 150, 155, 160]
latency_one = [37, 58, 76, 88, 97, 102, 104, 106]

# رسم نمودار
fig, ax = plt.subplots(figsize=(7, 5))

ax.plot(x, latency_all, marker='o', label=r'Consistency ALL', color='gold', linewidth=1.5, markersize=6)
ax.plot(x, latency_quorum, marker='s', label=r'Consistency Quorum', color='orange', linewidth=1.5, markersize=6)
ax.plot(x, latency_one, marker='^', label=r'Consistency ONE', color='red', linewidth=1.5, markersize=6)

# عناوین و محورها
ax.set_xlabel(r'Workload Size ($\times 10^6$ Operations)')
ax.set_ylabel(r'Network Latency (ms) [mean or 95$^{\rm th}$ percentile]')

ax.set_title(
    r'Network Latency vs. Workload Size' + '\n' +
    r'Workload-B, Replication Factor: Partial',
    pad=20,
    loc='center'
)

# گرید
ax.grid(True, which='both', linestyle='--', color='gray', alpha=0.5, linewidth=0.5)

# لجند
ax.legend(loc='best')

# 1e6 زیر محور 2.00
ax.text(2.00, ax.get_ylim()[0] - (ax.get_ylim()[1] * 0.1), r'$10^6$', ha='center')

plt.tight_layout()

plt.show()

# ذخیره خروجی با کیفیت
# plt.savefig('network_latency_workload_b_partial.pdf', bbox_inches='tight')
# plt.savefig('network_latency_workload_b_partial.pgf', bbox_inches='tight')
