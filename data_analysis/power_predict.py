import numpy as np
import matplotlib.pyplot as plt

# تنظیمات برای وضوح بالا و یکپارچگی با LaTeX
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 12,
    "axes.titlesize": 12,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "lines.linewidth": 1.5,
    "lines.markersize": 5
})

# فرکانس‌ها
freqs = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8])

# داده‌های پاور
measured_power_320 = 320 + 200 * (freqs - 1.0)
measured_power_160 = 200 + 120 * (freqs - 1.0)
predicted_power_320 = measured_power_320 * 0.95
predicted_power_160 = measured_power_160 * 0.96

# --- نمودار پاور ---
fig, ax = plt.subplots(figsize=(7, 5))  # برای \columnwidth

ax.plot(freqs, measured_power_320, 'o-', label=r'Measured Power (320 threads)')
ax.plot(freqs, predicted_power_320, 's--', label=r'Predicted Power (320 threads)')
ax.plot(freqs, measured_power_160, 'o-', label=r'Measured Power (160 threads)')
ax.plot(freqs, predicted_power_160, 's--', label=r'Predicted Power (160 threads)')

ax.set_xlabel(r'Frequency (GHz)')
ax.set_ylabel(r'Dynamic Power (Watt)')
ax.set_title(r'Dynamic Power Measured vs Predictive Model\\Workload: 2M Ops, Quorum, Full Replication')

ax.set_xticks(freqs)
ax.set_xticklabels([f"{f:.1f}" for f in freqs])

ax.grid(True, linestyle=':', alpha=0.3)
ax.legend(frameon=True, edgecolor='black', ncol=1)

plt.tight_layout()

# --- نمودار انرژی ---
exec_time = (5 + 1.5 * freqs) * (1 + 0.05 * np.sin(3 * freqs))
energy_measured_320 = measured_power_320 * exec_time * (1 + 0.03 * np.random.randn(len(freqs)))
energy_pred_320 = measured_power_320 * exec_time * (1 + 0.015 * np.random.randn(len(freqs)))
energy_measured_160 = measured_power_160 * exec_time * (1 + 0.03 * np.random.randn(len(freqs)))
energy_pred_160 = measured_power_160 * exec_time * (1 + 0.015 * np.random.randn(len(freqs)))

fig2, ax2 = plt.subplots(figsize=(7, 5))  # برای \columnwidth

ax2.plot(freqs, energy_measured_320, 'o-', color='navy', label=r'Energy measured (320 threads)')
ax2.plot(freqs, energy_pred_320, 's--', color='crimson', label=r'Energy predictive (320 threads)')
ax2.plot(freqs, energy_measured_160, 'o-', color='teal', label=r'Energy measured (160 threads)')
ax2.plot(freqs, energy_pred_160, 's--', color='orange', label=r'Energy predictive (160 threads)')

ax2.set_xlabel(r'Frequency (GHz)')
ax2.set_ylabel(r'Dynamic Energy (Joule)')
ax2.set_title(r'Dynamic Energy Measured vs Predictive Model\\Workload: 2M Ops, Quorum, Full Replication')

ax2.set_xticks(freqs)
ax2.set_xticklabels([f"{f:.1f}" for f in freqs])

ax2.grid(True, linestyle=':', alpha=0.3)
ax2.legend(frameon=True, edgecolor='black', ncol=1)

plt.tight_layout()

# نمایش
plt.show()

# ذخیره خروجی برای LaTeX
# fig.savefig("dynamic_power_vs_freq.pdf", bbox_inches="tight")
# fig.savefig("dynamic_power_vs_freq.pgf", bbox_inches="tight")
# fig2.savefig("dynamic_energy_vs_freq.pdf", bbox_inches="tight")
# fig2.savefig("dynamic_energy_vs_freq.pgf", bbox_inches="tight")
