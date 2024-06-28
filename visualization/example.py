import numpy as np

# degree: 30°
rad = np.pi / 6
# 正弦: 1/2, 余弦: \sqrt{3}/2, 正切: \sqrt{3}/3
print(f"sine: {np.sin(rad)}, cosine: {np.cos(rad)}, tangent: {np.tan(rad)}")
# 余切: \sqrt{3}, 正割: 2/\sqrt{3}, 余割: 2
print(
    f"cotangent: {1 / np.tan(rad)}, secant: {1 / np.cos(rad)}, cosecant: {1 / np.sin(rad)}"
)
# 反正弦: 30°, numpy.pi/6
print(np.rad2deg(np.arcsin(0.5)))
# 反余弦：45°, numpy.pi/4
print(np.rad2deg(np.arccos(np.sqrt(2) / 2)))
# 反正切：45°, numpy.pi/4
print(np.rad2deg(np.arctan(1)))
