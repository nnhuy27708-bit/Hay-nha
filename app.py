import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Mô phỏng Ném Xiên Có Lực Cản", page_icon="🚀", layout="centered"
)

st.title("🚀 Mô phỏng Chuyển động Ném Xiên")
st.write(
    "Khảo sát quỹ đạo chuyển động của vật trong trọng trường có kể đến lực cản môi trường ($\vec{F}_c = -k\vec{v}$)."
)

# Thanh điều khiển (Sidebar)
st.sidebar.header("⚙️ Thông số đầu vào")
v0 = st.sidebar.slider(
    "Vận tốc ban đầu $v_0$ (m/s)", 5.0, 50.0, 20.0, 0.5
)
alpha_deg = st.sidebar.slider("Góc ném $\alpha$ (độ)", 10.0, 80.0, 45.0, 1.0)
k = st.sidebar.slider("Hệ số cản $k$", 0.0, 1.0, 0.2, 0.02)
m = st.sidebar.number_input("Khối lượng $m$ (kg)", 0.1, 10.0, 1.0, 0.1)
g = 9.81

# Tính toán vật lý
alpha = np.radians(alpha_deg)
t = np.linspace(0, 6, 600)

# Có lực cản
if k > 0:
    x_drag = (m * v0 * np.cos(alpha) / k) * (1 - np.exp(-k * t / m))
    y_drag = (
        m / k
    ) * (v0 * np.sin(alpha) + m * g / k) * (1 - np.exp(-k * t / m)) - (
        m * g / k
    ) * t
    idx = y_drag >= 0
    x_drag, y_drag = x_drag[idx], y_drag[idx]
else:
    x_drag, y_drag = [], []

# Lý tưởng (không cản)
x_ideal = v0 * np.cos(alpha) * t
y_ideal = v0 * np.sin(alpha) * t - 0.5 * g * t**2
idx_ideal = y_ideal >= 0
x_ideal, y_ideal = x_ideal[idx_ideal], y_ideal[idx_ideal]

# Vẽ biểu đồ
fig, ax = plt.subplots(figsize=(9, 5))
if k > 0:
    ax.plot(
        x_drag,
        y_drag,
        label=f"Có lực cản ($F_c = -{k}v$)",
        color="crimson",
        linewidth=2.5,
    )
ax.plot(
    x_ideal,
    y_ideal,
    label="Lý tưởng (không cản)",
    color="dodgerblue",
    linestyle="--",
    linewidth=2,
)

ax.set_title("So sánh quỹ đạo ném xiên thực tế và lý tưởng")
ax.set_xlabel("Tầm xa $x$ (m)")
ax.set_ylabel("Độ cao $y$ (m)")
ax.legend()
ax.grid(True, linestyle=":", alpha=0.6)

st.pyplot(fig)
