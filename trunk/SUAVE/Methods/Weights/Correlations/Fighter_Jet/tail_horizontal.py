## @ingroup Methods-Weights-Correlations-Fighter_Jet
# tail_horizontal.py
#
# Created:  Jan 2018, M. Clarke

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Units
import numpy as np

# ----------------------------------------------------------------------
#   Tail Horizontal
# ----------------------------------------------------------------------

## @ingroup Methods-Weights-Correlations-Fighter_Jet
def tail_horizontal(b_h,w_fus,Nult,TOW,wt_zf,S_h)   :      
    """ Calculate the weight of the horizontal tail in a standard configuration
    
    Assumptions:
    
    Source: 
        Aircraft Design: A Conceptual Approach, 5th Edition by Daniel P. Raymer
        
    Inputs:
        b_h - span of the horizontal tail                                                               [meters]
        Nult - ultimate design load of the aircraft                                                     [dimensionless]
        S_h - area of the horizontal tail                                                               [meters**2]
        TOW - maximum takeoff weight of the aircraft                                                    [kilograms]
        w_fus - fuselage width                                                                          [meters]
        wt_zf - zero fuel weight                                                                        [kilograms]
        
    Outputs:
        weight - weight of the horizontal tail                                                          [kilograms]
       
    Properties Used:
        N/A
    """   
    # unpack inputs
    span       = b_h / Units.ft # Convert meters to ft
    area       = S_h / Units.ft**2 # Convert meters squared to ft squared
    mtow       = TOW / Units.lb # Convert kg to lbs
    zfw   = wt_zf / Units.lb # Convert kg to lbs
    
    #Calculate weight of wing for traditional aircraft horizontal tail
    fuel_weight = mtow - zfw
    W_dg        = fuel_weight * 0.55 # 0.5 to 0.6 
    
    weight_English = 3.316*((1+w_fus/span)**2.)*(((W_dg*Nult)/1000)*0.260)*(area**0.806)

    weight = weight_English * Units.lbs # Convert from lbs to kg

    return weight