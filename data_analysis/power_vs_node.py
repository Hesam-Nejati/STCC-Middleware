import matplotlib.pyplot as plt

# تنظیمات لاتک برای خروجی برداری با کیفیت
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

num_nodes = [5, 10, 15, 20]

data = {
    'userspace 2.0 GHz': {
        'A': [260, 440, 620, 800],
        'B': [230, 390, 550, 710],
        'C': [200, 350, 500, 650]
    },
    'powersave': {
        'A': [180, 310, 440, 570],
        'B': [160, 270, 380, 490],
        'C': [140, 240, 340, 440]
    },
    'ondemand': {
        'A': [220, 380, 540, 700],
        'B': [200, 340, 480, 620],
        'C': [170, 290, 410, 530]
    },
    'performance': {
        'A': [280, 470, 660, 850],
        'B': [250, 420, 590, 760],
        'C': [220, 370, 520, 670]
    },
    'conservative': {
        'A': [200, 340, 480, 620],
        'B': [180, 300, 420, 540],
        'C': [160, 270, 380, 490]
    }
}

line_width = 1.5

for governor, workloads in data.items():
    fig, ax = plt.subplots(figsize=(7, 5))

    ax.plot(num_nodes, workloads['A'], marker='o', linestyle='-', linewidth=line_width, markersize=6, label=r'Workload A (Write-heavy)')
    ax.plot(num_nodes, workloads['B'], marker='s', linestyle='--', linewidth=line_width, markersize=6, label=r'Workload B (Mixed)')
    ax.plot(num_nodes, workloads['C'], marker='^', linestyle='-.', linewidth=line_width, markersize=6, label=r'Workload C (Read-heavy)')

    ax.set_xlabel(r'Number of Nodes')
    ax.set_ylabel(r'Dynamic Power (Watt)')

    ax.set_title(
        r'Dynamic Power vs Number of Nodes' + '\n' +
        rf'Governor: {governor}, Replication Factor: Full, Consistency: Quorum-based, 2M Ops, 320 Threads',
        pad=20,
        loc='center'
    )

    ax.grid(True, linestyle='--', color='gray', alpha=0.5, linewidth=0.5)
    ax.legend(loc='best')

    plt.tight_layout()

    filename = governor.replace(' ', '_').replace('.', '') + '_dynamic_power_vs_nodes.pdf'
    plt.savefig(filename, bbox_inches='tight')

    # اگر PGF خواستی:
    # filename_pgf = governor.replace(' ', '_').replace('.', '') + '_dynamic_power_vs_nodes.pgf'
    # plt.savefig(filename_pgf, bbox_inches='tight')

    plt.show()
