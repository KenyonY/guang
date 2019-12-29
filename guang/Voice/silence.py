import soundfile as sf
import numpy as np
import warnings
warnings.filterwarnings('ignore')
def find_no_silence(filename):
    """read the sound file, return you the voice start end voice end.
    
    Return:
        start(/s), end(/s), arg_start, arg_end
    """
    voice, sr = sf.read(filename)
#     diff = np.diff(voice, n=2)
#     print(diff)
#     plt.plot(diff)
#     print(np.argwhere(diff>1e-4))
    argvoice = np.argwhere(np.log(voice, )>-6)
    a= argvoice/sr
    win = 15
    for i in range(len(a)):
        if abs(np.mean(a[i:i+win])-a[i]) < 1e-3:
            start = a[i]
            arg_start = argvoice[i]
            break

    for i in range(-1, -len(a), -1):
        if abs(np.mean(a[i-win:i])-a[i]) < 1e-3:
            end = a[i-win]
            arg_end = argvoice[i-win]
            break
    
    return start[0], end[0], arg_start[0], arg_end[0]
