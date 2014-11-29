import pylab as P
import sys

try:
    averageReturns=P.loadtxt(sys.argv[1])
except:
    print("Please provide a file with a list of average returns")
    sys.exit(1)

f=P.figure()
ax=f.add_subplot(111)
ax.plot(range(1,len(averageReturns)+1),averageReturns)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.get_yaxis().set_tick_params(direction='out')
ax.get_xaxis().set_tick_params(direction='out')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
P.ylim(-1000,0)
P.xlim(0,len(averageReturns)+1)
P.xticks([1,20,50,100,150,200])
P.title("Average Return from Q-learning")
P.xlabel("Episode Number")
P.ylabel("Average\nReturn",rotation='horizontal')
P.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.1)
P.savefig("AverageReturn.pdf")
