import matplotlib.pyplot as plt

def config_plot():
    plt.style.use('classic')
    VFont=16
    plt.rcParams['figure.facecolor'] = '1.0'
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family'] = 'STIXGeneral'
    plt.rcParams['font.sans-serif'] = 'stix'
    #plt.rcParams['mathtext.fontset'] = 'dejavusans'
    #plt.rcParams['font.family'] = 'DejaVu Sans'
    #plt.rcParams['font.sans-serif'] = 'dejavusans'
    plt.rcParams['axes.titlesize'] = VFont*1.1
    plt.rcParams['axes.labelsize'] = VFont
    plt.rcParams['xtick.labelsize'] = VFont*0.9
    plt.rcParams['ytick.labelsize'] = VFont*0.9
    plt.rcParams['legend.fontsize'] = VFont*0.9
    plt.rcParams['axes.formatter.useoffset'] = False
    plt.rcParams['savefig.directory'] = ""
    plt.rcParams['savefig.format'] = 'pdf'
    plt.rcParams["figure.dpi"] = 280
    plt.rcParams["figure.figsize"] = ( 6, 4.5 )
    plt.rcParams["lines.markersize"] = 5
    
    plt.rcParams['figure.subplot.left'  ] = 0.14
    plt.rcParams['figure.subplot.right' ] = 0.96
    plt.rcParams['figure.subplot.bottom'] = 0.14
    plt.rcParams['figure.subplot.top'   ] = 0.95
    plt.rcParams['figure.subplot.wspace'] = 0.20
    plt.rcParams['figure.subplot.hspace'] = 0.20

def inline_label( lbl, x, y, i, fontsize = 8, color = 'k' ):
    
  # get screen coordinates (physical display)
  screen_dx, screen_dy = plt.gca().transData.transform( (x[i+1], y[i+1]) ) \
                       - plt.gca().transData.transform( (x[i-1], y[i-1]) )
    
  angle = ( np.degrees( np.arctan2( screen_dy, screen_dx ) ) + 90 ) % 180 - 90
  
  plt.gca().text( x[i], y[i], lbl,
                  rotation=angle,
                  fontsize=fontsize, color=color, 
                  horizontalalignment='center',
                  verticalalignment='center', 
                  bbox=dict( boxstyle='round, pad=-0.2', 
                             edgecolor='k', facecolor='w',  
                             linewidth=0,
                             alpha=0.90) 
                )
