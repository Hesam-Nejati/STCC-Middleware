import matplotlib.pyplot as plt

# تنظیمات LaTeX-friendly
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 12,
    "axes.titlesize": 14,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "lines.linewidth": 2,
    "lines.markersize": 8
})

# داده‌ها
replication_factors = [3, 5, 7, 10]
latency_a = [100, 130, 160, 200]
latency_b = [120, 160, 190, 240]
latency_c = [80, 100, 120, 150]

# شکل
fig, ax = plt.subplots(figsize=(6, 4))  # متناسب با 0.3 تا \textwidth

# خطوط
ax.plot(replication_factors, latency_a, marker='o', linestyle='-', label=r'Workload A')
ax.plot(replication_factors, latency_b, marker='s', linestyle='--', label=r'Workload B')
ax.plot(replication_factors, latency_c, marker='^', linestyle='-.', label=r'Workload C')

# برچسب‌ها و عنوان
ax.set_xlabel(r'Replication Factor (Number)')
ax.set_ylabel(r'Network Latency (ms) [mean or 95th percentile]')
ax.set_title(r'Network Latency vs Replication Factor\\20 Nodes, 2M Ops, 320 Threads, 2.0 GHz, Quorum')

# گرید
ax.grid(True, linestyle='--', color='gray', alpha=0.3)

# لجند با کادر
ax.legend(frameon=True, edgecolor='black', fontsize=10)

plt.tight_layout()

plt.show()

# خروجی برداری
# plt.savefig('latency_vs_replication_quorum.pdf', bbox_inches='tight')
# plt.savefig('latency_vs_replication_quorum.pgf', bbox_inches='tight')
