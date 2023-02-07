import numpy as np
import matplotlib as plt
import scipy
designmatrix=[]
C_all=[]
row_0_all=[]
for i in designmatrix:
    row_0=i[0,:]  # 第一个横行，第一个squat
    N=50
    t=np.r_[0:i.shape[1]] # row-wise merging
    t1 = x1 = np.linspace(0, i.shape[1] - 1, N, endpoint=True)
    f = scipy.interpolate.interp1d(t, row_0,'cubic')
    row_0_interp = f(t1)
    row_0_all.append(row_0_interp)
    plt.plot(t, row_0, 'o', t1, row_0_interp, '.')
    plt.show()
    # Now let's interpolate whole Squat
    C = np.zeros((36, N))
    t = np.r_[0:i.shape[1]]
    t1 = x1 = np.linspace(0, i.shape[1] - 1, N, endpoint=True)
    for j in range(0, i.shape[0]):
        f = np.interpolate.interp1d(t, i[j, :], 'cubic')
        row_0_interp = f(t1)
        C[j, :] = f(t1)
    C_all.append(C)
    #plot_squat(C)

