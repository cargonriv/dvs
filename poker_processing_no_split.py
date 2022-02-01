import tonic
import matplotlib.pyplot as plt
from core.utils import coordinate_point

dataset = tonic.datasets.POKERDVS(save_to='./data', train=True)
data, target = dataset[0]

print('Poker card label (int): ', target)
print('coordinate data points: ', data)

datapoints_list = []
for i, ref_point in enumerate(data):
    datapoints_list.append(coordinate_point(ref_point[0],ref_point[1],ref_point[2],ref_point[3]))
data_sorted_timestamps = sorted(datapoints_list, key=lambda point: point.timestep)


fig = plt.figure()
for sorted_data_point in data_sorted_timestamps:
    fig.patch.set_facecolor('tab:gray')
    fig.patch.set_alpha(0.8)
    ax = fig.add_subplot(111)
    ax.patch.set_facecolor('tab:gray')
    ax.patch.set_alpha(0.0)
    # Change AXES' ALPHA FROM 0% TO 10% TO 50% TO 80% TO MODULATE THE MOTION FADE
    plt.xlim(0,35)
    plt.ylim(0,35)
    if sorted_data_point.polarity == 1:
        ax.set_facecolor('tab:gray')
        plt.scatter(sorted_data_point.x_point, sorted_data_point.y_point, color = 'white')
        # CHANGE PAUSE TO DIFF OF sorted_data_point.timestep and (sorted_data_point - 1)
        plt.pause(10**-18)
    else:
        ax.set_facecolor('tab:gray')
        plt.scatter(sorted_data_point.x_point, sorted_data_point.y_point, color = 'black')
        plt.pause(10**-18)
plt.show()