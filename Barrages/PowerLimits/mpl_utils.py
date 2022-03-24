import matplotlib.pyplot as mpl
import numpy as np

def config_plots():
    #mpl.style.use('classic')
    VFont=14
    mpl.rcParams['figure.facecolor'] = '1.0'
    #mpl.rcParams['mathtext.fontset'] = 'stix'
    #mpl.rcParams['font.family'] = 'STIXGeneral'
    #mpl.rcParams['font.sans-serif'] = 'stix'
    #mpl.rcParams['mathtext.fontset'] = 'dejavusans'
    #mpl.rcParams['font.family'] = 'DejaVu Sans'
    #mpl.rcParams['font.sans-serif'] = 'dejavusans'
    #mpl.rcParams['axes.titlesize'] = VFont
    #mpl.rcParams['axes.labelsize'] = VFont
    #mpl.rcParams['xtick.labelsize'] = VFont*0.9
    #mpl.rcParams['ytick.labelsize'] = VFont*0.9
    #mpl.rcParams['legend.fontsize'] = VFont*0.9
    #mpl.rcParams['savefig.directory'] = ""
    mpl.rcParams['savefig.format'] = 'pdf'
    mpl.rcParams["figure.figsize"] = (11, 5)
    mpl.rcParams['axes.formatter.useoffset'] = False

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
