from cycler import cycler
import matplotlib as mpl
import matplotlib.pyplot as plt


def use_amethyst_theme():
    plt.style.use("default")

    mpl.rcParams.update({
        "figure.facecolor": "#202020",
        "axes.facecolor": "#232323",
        "axes.edgecolor": "white",
        "axes.titlecolor": "white",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "grid.color": "#555555",

        "figure.constrained_layout.w_pad": 0.15,
        "figure.constrained_layout.h_pad": 0.15,
        "axes.titlepad": 10,
        "axes.labelpad": 10,

        "font.family": "JetBrainsMono NF",
        "font.size": 12,
    })

    mpl.rcParams["axes.prop_cycle"] = cycler(color=[
        "#B48EAD",  # Amethyst
        "#88C0D0",  # Ice blue
        "#5E81AC",  # Deep blue
        "#A3BE8C",  # Soft green
        "#8FBCBB",  # Teal
        "#D8B4F8",  # Light lavender
        "#7AA2F7",  # Bright blue
    ])
