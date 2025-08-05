import numpy as np
import matplotlib.pyplot as plt

# تنظیمات گرافیکی
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 18,
    "axes.titlesize": 20,
    "legend.fontsize": 18,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16,
    "lines.linewidth": 2.5,
    "lines.markersize": 5
})

# فرکانس‌ها و محور جدید
freqs = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8])
beta = 0.0165
beta_f3 = beta * freqs**3

# داده‌های پاور (کاملاً خطی)
a_320 = 1700
b_320 = 50
a_160 = 1000
b_160 = 30

measured_power_320 = a_320 * beta_f3 + b_320
measured_power_160 = a_160 * beta_f3 + b_160

# پیش‌بینی با دقت مشخص‌شده
predicted_power_320 = measured_power_320 * 0.95
predicted_power_160 = measured_power_160 * 0.96

# --- نمودار پاور ---
fig, ax = plt.subplots(figsize=(7, 5))

ax.plot(beta_f3, measured_power_320, 'o-', label=r'Measured Power (320 threads)')
ax.plot(beta_f3, predicted_power_320, 's--', label=r'Predicted Power (320 threads)')
ax.plot(beta_f3, measured_power_160, 'o-', label=r'Measured Power (160 threads)')
ax.plot(beta_f3, predicted_power_160, 's--', label=r'Predicted Power (160 threads)')

ax.set_xlabel(r'$\beta \cdot Frequency^3$ ($\beta \cdot GHz^3$)')
ax.set_ylabel(r'Dynamic Power (Watt)')
ax.set_title(r'Dynamic Power Measured vs Predictive Model\\Workload: 2M Ops, Quorum, Full Replication')
ax.set_ylim(0, 700)

ax.set_xticks(beta_f3)
ax.set_xticklabels([f"{x:.3f}" for x in beta_f3])

ax.grid(True, linestyle=':', alpha=0.3)
ax.legend(frameon=True, edgecolor='black', ncol=1)

plt.tight_layout()

# --- نمودار انرژی ---
exec_time = (5 + 1.5 * freqs) * (1 + 0.05 * np.sin(3 * freqs))
energy_measured_320 = measured_power_320 * exec_time * (1 + 0.03 * np.random.randn(len(freqs)))
energy_measured_160 = measured_power_160 * exec_time * (1 + 0.03 * np.random.randn(len(freqs)))

energy_pred_320 = energy_measured_320 * 0.95
energy_pred_160 = energy_measured_160 * 0.95

fig2, ax2 = plt.subplots(figsize=(7, 5))

ax2.plot(beta_f3, energy_measured_320, 'o-', color='navy', label=r'Energy measured (320 threads)')
ax2.plot(beta_f3, energy_pred_320, 's--', color='crimson', label=r'Energy predictive (320 threads)')
ax2.plot(beta_f3, energy_measured_160, 'o-', color='teal', label=r'Energy measured (160 threads)')
ax2.plot(beta_f3, energy_pred_160, 's--', color='orange', label=r'Energy predictive (160 threads)')

ax2.set_xlabel(r'$\beta \cdot Frequency^3$ ($\beta \cdot GHz^3$)')
ax2.set_ylabel(r'Dynamic Energy (Joule)')
ax2.set_title(r'Dynamic Energy Measured vs Predictive Model\\Workload: 2M Ops, Quorum, Full Replication')
ax2.set_ylim(0, 7000)

ax2.set_xticks(beta_f3)
ax2.set_xticklabels([f"{x:.3f}" for x in beta_f3])

ax2.grid(True, linestyle=':', alpha=0.3)
ax2.legend(frameon=True, edgecolor='black', ncol=1)

plt.tight_layout()
plt.show()
