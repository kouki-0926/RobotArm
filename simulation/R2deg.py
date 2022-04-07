import numpy as np


def R2deg(R):  # R2deg に同次変換行列の入力可
    φ = np.arctan2(R[1, 2], R[0, 2])
    θ = np.arctan2(np.sqrt(R[0, 2]**2+R[1, 2]**2), R[2, 2])
    ψ = np.arctan2(R[2, 1], -R[2, 0])
    return np.array([φ, θ, ψ])


def R2degAll(R):  # R2deg に同次変換行列の入力可
    φ = np.array([np.arctan2(R[1, 2], R[0, 2]),
                  np.arctan2(-R[1, 2], -R[0, 2])])
    θ = np.array([np.arctan2(np.sqrt(R[0, 2]**2+R[1, 2]**2), R[2, 2]),
                  np.arctan2(-np.sqrt(R[0, 2]**2+R[1, 2]**2), R[2, 2])])
    ψ = np.array([np.arctan2(R[2, 1], -R[2, 0]),
                  np.arctan2(-R[2, 1], R[2, 0])])
    return np.rad2deg(np.array([φ, θ, ψ])).T


def T2deg(T):
    return R2deg(T[0:3, 0:3])


if __name__ == '__main__':
    T = np.array([[1, 0, 0, 2],
                  [0, 0, -1, 2],
                  [0, 1, 0, 2],
                  [0, 0, 0, 1]])
    print(R2deg(T))
