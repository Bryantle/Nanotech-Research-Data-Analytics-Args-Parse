import matplotlib.pyplot as plt
import numpy as np
import argparse

#Unapplied = pd.read_csv("/Users/ghaidael-saied/Desktop/Data_Analytics/6_originalnoRC.csv")
#signal_2 = Unapplied['Curr_mA 1']

#Applied = pd.read_csv("/Users/ghaidael-saied/Desktop/Data_Analytics/6_appliedRC.csv")
#signal_1 = Applied['Curr_mA 16']

def get_cross_correlation(time, signal_1, signal_2, shift):

    shifted_signal_1 = signal_1[:-1-shift]
    time_1 = time[shift:-1]

    shifted_signal_2 = signal_2[shift:-1]
    time_2 = time[shift:-1]

    #plt.plot(time_2,shifted_signal_2, label="signal 2")
    #plt.plot(time_1,shifted_signal_1, label="signal 1")
    #plt.legend()
    #plt.show()
    signal_dot_product = np.dot(shifted_signal_1, shifted_signal_2)
    signal_1_norm = np.dot(shifted_signal_1, shifted_signal_1)
    signal_2_norm = np.dot(shifted_signal_2, shifted_signal_2)

    cross_correlation = signal_dot_product/np.sqrt(signal_1_norm*signal_2_norm)

    return cross_correlation

def get_signal_time_delay(time, signal_1, signal_2):
    max_cor = 0
    signal_shift = 0
    for t,value in enumerate(time):
        cor = get_cross_correlation(time, signal_1,signal_2,t)
        if (cor > max_cor):
            max_cor = cor
            signal_shift = t

    return signal_shift

sample_time = 0.001 # (s)

final_time = 2

time = np.arange(0, final_time, step=sample_time)

omega_1 = 1 # 1 hz
test_signal_1 = np.cos(2*np.pi*omega_1*time)

omega_2 = 1 # 1 hz
test_signal_2 = np.sin(2*np.pi*omega_2*time)

def Main():
    parser = argparse.ArgumentParser();
    parser.add_argument('signal_1', help = 'The unapplied signal.')
    parser.add_argument('signal_2', help = 'The applied signal. ')
    args = parser.parse_args()

    sig_1 = args.signal_1
    sig_2 = args.signal_2

    plt.plot(time, test_signal_2, label="signal 1")
    plt.plot(time,test_signal_2, label="signal 2")
    plt.legend()
    plt.show()

    print ("Cross Correlation of the same signal (highly correlated)",\
     get_cross_correlation(time, test_signal_1,test_signal_1, 0))
    print ("Cross Correlation of two uncorrelated signals (90 deg out of phase)",\
     get_cross_correlation(time, test_signal_1,test_signal_2,0))
    print ("Corss Correlation of two uncorrelated signals shifted by 90 degs",\
     get_cross_correlation(time, test_signal_1, test_signal_2, 250))
    print ("Signal Time Delay (#number of samples)",\
     get_signal_time_delay(time,test_signal_1,test_signal_2))

if __name__ == '__main__':
    Main()
