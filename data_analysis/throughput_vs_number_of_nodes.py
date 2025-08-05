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
num_nodes = [10, 15, 20]

data = {
    'userspace 2.0 GHz': {
        'A': [3000, 4500, 6000],
        'B': [2800, 4200, 5500],
        'C': [5000, 7200, 8500]
    },
    'powersave': {
        'A': [2000, 3000, 4000],
        'B': [1800, 2800, 3800],
        'C': [3500, 5000, 6500]
    },
    'ondemand': {
        'A': [2500, 3750, 5000],
        'B': [2300, 3400, 4600],
        'C': [4000, 6000, 7500]
    },
    'performance': {
        'A': [3200, 4700, 6200],
        'B': [2900, 4400, 5800],
        'C': [5200, 7500, 9000]
    },
    'conservative': {
        'A': [2400, 3600, 4800],
        'B': [2200, 3300, 4400],
        'C': [3800, 5700, 7200]
    }
}

# رسم
for governor, workloads in data.items():
    fig, ax = plt.subplots(figsize=(7, 5))

    ax.plot(num_nodes, workloads['A'], marker='o', linestyle='-', label='Workload A')
    ax.plot(num_nodes, workloads['B'], marker='s', linestyle='--', label='Workload B')
    ax.plot(num_nodes, workloads['C'], marker='^', linestyle='-.', label='Workload C')

    ax.set_xlabel(r'Number of Nodes')
    ax.set_ylabel(r'System Throughput (ops/sec)')
    ax.set_title(
        r'Throughput vs Number of Nodes' + '\n' +
        rf'Governor: {governor}, Replication: Full, Consistency: Quorum,' + '\n' +
        r'2M Ops, 320 Threads',
        pad=20,
        loc='center'
    )

    ax.grid(True, linestyle='--', color='gray', alpha=0.5, linewidth=0.5)
    ax.legend(loc='best')

    plt.tight_layout()

    # ذخیره خروجی برداری (در صورت نیاز فعال کن)
    filename = governor.replace(' ', '_').replace('.', '') + '_throughput_vs_nodes.pdf'
    plt.savefig(filename, bbox_inches='tight')

    # اگر خواستی PGF:
    # filename_pgf = governor.replace(' ', '_').replace('.', '') + '_throughput_vs_nodes.pgf'
    # plt.savefig(filename_pgf, bbox_inches='tight')

    plt.show()
