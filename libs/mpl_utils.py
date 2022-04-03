import matplotlib.pyplot as mpl
import numpy as np
from cycler import cycler

def config_plots():
    mpl.style.use('classic')
    VFont=16
    mpl.rcParams['figure.facecolor'] = '1.0'
    mpl.rcParams['mathtext.fontset'] = 'stix'
    mpl.rcParams['font.family'] = 'STIXGeneral'
    mpl.rcParams['font.sans-serif'] = 'stix'
    #mpl.rcParams['mathtext.fontset'] = 'dejavusans'
    #mpl.rcParams['font.family'] = 'DejaVu Sans'
    #mpl.rcParams['font.sans-serif'] = 'dejavusans'
    mpl.rcParams['axes.titlesize'] = VFont
    mpl.rcParams['axes.labelsize'] = VFont
    mpl.rcParams['xtick.labelsize'] = VFont*0.9
    mpl.rcParams['ytick.labelsize'] = VFont*0.9
    mpl.rcParams['legend.fontsize'] = VFont*0.9
    mpl.rcParams['axes.formatter.useoffset'] = False
    mpl.rcParams['savefig.directory'] = ""
    mpl.rcParams['savefig.format'] = 'pdf'
    mpl.rcParams["figure.dpi"] = 280
    mpl.rcParams["figure.figsize"] = ( 6, 4.5 )
    mpl.rcParams["lines.markersize"] = 5
    
    dc = ( cycler( linestyle = [ \
              (0,(6,0)), (0,(6,2)), (0,(6,1.5,1.5,1.5)), \
              (0,(8,1.5,1.5,1.5,1.5,1.5)), (0,(11,3)), (0,(2,2)), \
              (0,(11,3,3,3,)), (0,(11,2,5,2)), (0,(17,2)), \
              (0,(17,2,2,2)) ] ) + \
           cycler('color', [ \
              '#1f77b4', '#ff7f0e', '#2ca02c', \
              '#d62728', '#9467bd', '#8c564b', \
              '#e377c2', '#7f7f7f', '#bcbd22', \
              '#17becf'] ) \
          )    
    mpl.rcParams["axes.prop_cycle"] = dc
    
    mpl.rcParams['lines.linewidth'] = 1.5

    mpl.rcParams['figure.subplot.left'  ] = 0.14
    mpl.rcParams['figure.subplot.right' ] = 0.96
    mpl.rcParams['figure.subplot.bottom'] = 0.14
    mpl.rcParams['figure.subplot.top'   ] = 0.95
    mpl.rcParams['figure.subplot.wspace'] = 0.20
    mpl.rcParams['figure.subplot.hspace'] = 0.20

def inline_label( lbl, x, y, i, fontsize = 8, color = 'k' ):
    
  # get screen coordinates (physical display)
  screen_dx, screen_dy = mpl.gca().transData.transform( (x[i+1], y[i+1]) ) \
                       - mpl.gca().transData.transform( (x[i-1], y[i-1]) )
    
  angle = ( np.degrees( np.arctan2( screen_dy, screen_dx ) ) + 90 ) % 180 - 90
  
  mpl.gca().text( x[i], y[i], lbl,
                  rotation=angle,
                  fontsize=fontsize, color=color, 
                  horizontalalignment='center',
                  verticalalignment='center', 
                  bbox=dict( boxstyle='round, pad=-0.2', 
                             edgecolor='k', facecolor='w',  
                             linewidth=0,
                             alpha=0.90) 
                )
