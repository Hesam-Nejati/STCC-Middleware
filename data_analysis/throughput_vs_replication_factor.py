import matplotlib.pyplot as plt

# تنظیمات خروجی هماهنگ با لاتک
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
replication_factors = [3, 5, 10]
throughput_a = [6000, 5000, 4000]
throughput_b = [5500, 4500, 3500]
throughput_c = [7000, 6200, 5500]

fig, ax = plt.subplots(figsize=(7, 5))

# رسم
ax.plot(replication_factors, throughput_a, marker='o', linestyle='-', linewidth=1.5, markersize=6, label=r'Workload A')
ax.plot(replication_factors, throughput_b, marker='s', linestyle='--', linewidth=1.5, markersize=6, label=r'Workload B')
ax.plot(replication_factors, throughput_c, marker='^', linestyle='-.', linewidth=1.5, markersize=6, label=r'Workload C')

# محورها
ax.set_xlabel(r'Replication Factor (Number)')
ax.set_ylabel(r'System Throughput (ops/sec)')

# عنوان چند خطی متقارن
ax.set_title(
    r'System Throughput vs Replication Factor' + '\n' +
    r'20 Nodes, 2M Ops, 320 Threads, Frequency: 2.0 GHz, Consistency: Quorum',
    pad=20,
    loc='center'
)

ax.grid(True, linestyle='--', color='gray', alpha=0.5, linewidth=0.5)
ax.legend(loc='best')

plt.tight_layout()

# نمایش
plt.show()

# برای ذخیره خروجی برداری (فعال کن اگر خواستی):
# plt.savefig('throughput_vs_replication.pdf', bbox_inches='tight')
# یا
# plt.savefig('throughput_vs_replication.pgf', bbox_inches='tight')
