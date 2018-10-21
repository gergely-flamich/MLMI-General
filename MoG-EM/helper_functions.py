import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def get_normal_std_ellipse(mean, cov, std=1):
    """
    Adapted from https://stackoverflow.com/questions/20126061/creating-a-confidence-ellipses-in-a-sccatterplot-using-matplotlib
    """
    lambda_, v = np.linalg.eig(cov)
    lambda_ = np.sqrt(lambda_)

    ell = Ellipse(xy=(mean[0], mean[1]),
                width=lambda_[0] * std * 2, height=lambda_[1] * std * 2,
                angle=np.rad2deg(np.arccos(v[0, 0])))
    ell.set_facecolor('none')
    ell.set_edgecolor('black')
    return ell
