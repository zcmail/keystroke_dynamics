import numpy as np
import matplotlib
from matplotlib import pyplot

from keystroke_dynamics import KeyDwellTime, NormalFeature, CompositeFeature

def synthesize_data( normal_feature, n=10000 ):
    d= normal_feature.distribution
    return np.random.normal( loc= d.mean, scale=d.stddev, size=normal_feature.nsamples)

def normal_to_bar( normal_feature ):
    '''returns bottom and top of a bar'''
    dis= normal_feature.distribution
    delta= dis.stddev * 2
    return dis.mean-delta, dis.mean+delta

def visualize_normal_composite( composite, color='blue', offset=0.0, width=0.8, show=True ):
    '''visualizes a composite key composed of normal features'''
    key_list= [composite[k] for k in sorted(composite.keys())]
    assert all( [isinstance( key, KeyDwellTime ) for key in key_list])
    heights, bottoms= zip(*map(normal_to_bar, key_list))
    labels= [ k.name for k in key_list ]

    xs= np.arange(len(heights)) + offset
    pyplot.bar(xs, heights, bottom=bottoms, color=color, width=width )
    pyplot.setp( pyplot.gca(), label= labels )
    if show:
        pyplot.show()

def visualize_normal_composites( composites, show=True ):
    COLORS= ('red', 'orange','yellow','green', 'blue', 'violet')
    n= len(composites)
    width= 0.9-(0.1*n)
    common= CompositeFeature.getCommonFeatures( *composites )
    colors= COLORS[:n]
    for i,c,color in zip(range(n),common, colors):
        visualize_normal_composite( c, color=color, show=False, offset=i*0.1, width=width)
    if show:
        pyplot.show()


