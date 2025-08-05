import matplotlib.pyplot as plt

# تنظیمات برای خروجی بسیار با کیفیت
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 14,
    "axes.labelsize": 14,
    "axes.titlesize": 16,
    "legend.fontsize": 12,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "lines.linewidth": 2,
    "lines.markersize": 8
})

num_nodes = [10, 15, 20]
latency_a_all = [150, 200, 250]
latency_a_quorum = [100, 130, 160]
latency_a_one = [50, 60, 70]

latency_b_all = [180, 230, 280]
latency_b_quorum = [120, 150, 180]
latency_b_one = [60, 70, 80]

latency_c_all = [140, 180, 220]
latency_c_quorum = [90, 120, 150]
latency_c_one = [45, 55, 65]

# بزرگتر کردن figure برای خروجی با کیفیت
fig, ax = plt.subplots(figsize=(7, 5))

ax.plot(num_nodes, latency_a_all, marker='o', linestyle='-', label=r'ALL - Workload A')
ax.plot(num_nodes, latency_a_quorum, marker='s', linestyle='--', label=r'Quorum - Workload A')
ax.plot(num_nodes, latency_a_one, marker='^', linestyle='-.', label=r'ONE - Workload A')

ax.plot(num_nodes, latency_b_all, marker='o', linestyle='-', label=r'ALL - Workload B')
ax.plot(num_nodes, latency_b_quorum, marker='s', linestyle='--', label=r'Quorum - Workload B')
ax.plot(num_nodes, latency_b_one, marker='^', linestyle='-.', label=r'ONE - Workload B')

ax.plot(num_nodes, latency_c_all, marker='o', linestyle='-', label=r'ALL - Workload C')
ax.plot(num_nodes, latency_c_quorum, marker='s', linestyle='--', label=r'Quorum - Workload C')
ax.plot(num_nodes, latency_c_one, marker='^', linestyle='-.', label=r'ONE - Workload C')

ax.set_xlabel(r'Number of Nodes')
ax.set_ylabel(r'Network Latency (ms) [mean or 95th percentile]')
ax.set_title(r'Network Latency vs Number of Nodes' + '\n' +
             r'Replication: Full, Consistency: Quorum-based, 2M Ops, 320 Threads, 2.0 GHz')

ax.grid(True, linestyle='--', alpha=0.3)
ax.legend(frameon=True, edgecolor='black', ncol=2, loc='best')

plt.tight_layout()

# ذخیره با dpi بالا
plt.savefig("network_no_nodes_scalable.pdf", bbox_inches="tight", dpi=600)
plt.savefig("network_no_nodes_scalable.pgf", bbox_inches="tight", dpi=600)
plt.show()
