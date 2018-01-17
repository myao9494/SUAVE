## @ingroup Methods-Weights-Correlations-Fighter_Jet
# wing_main.py
#
# Created:  Jan 2018, M. Clarke

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Units
import numpy as np

# ----------------------------------------------------------------------
#   Wing Main
# ----------------------------------------------------------------------

## @ingroup Methods-Weights-Correlations-Fighter_Jet
def wing_main(S_gross_w,b,lambda_w,t_c_w,sweep_w,Nult,TOW,wt_zf,K_dw,K_vs):
    """ Calculate the wing weight of the aircraft based on the fully-stressed 
    bending weight of the wing box
    
    Assumptions:
        Control Surface of wing is 0.05% of wing area
    Source: 
        Aircraft Design: A Conceptual Approach, 5th Edition by Daniel P. Raymer
        
    Inputs:
        S_gross_w - area of the wing                 [meters**2]
        b - span of the wing                         [meters**2]
        lambda_w - taper ratio of the wing           [dimensionless]
        t_c_w - thickness-to-chord ratio of the wing [dimensionless]
        sweep_w - sweep of the wing                  [radians]
        Nult - ultimate load factor of the aircraft  [dimensionless]
        TOW - maximum takeoff weight of the aircraft [kilograms]
        wt_zf - zero fuel weight of the aircraft     [kilograms]
    
    Outputs:
        weight - weight of the wing                  [kilograms]          
        
    Properties Used:
        N/A
    """ 
    
    # unpack inputs
    span  = b / Units.ft # Convert meters to ft
    taper = lambda_w
    sweep = sweep_w
    area  = S_gross_w / Units.ft**2 # Convert meters squared to ft squared
    mtow  = TOW / Units.lb # Convert kg to lbs
    zfw   = wt_zf / Units.lb # Convert kg to lbs

    #Calculate weight of wing for fighter jet 
    fuel_weight = mtow - zfw
    W_dg        = fuel_weight * 0.55 # 0.5 to 0.6 
    S_cws       = area*0.05  
    A  = span**2/area
    weight = 0.0103* K_dw * K_vs *((W_dg*Nult)**0.5)*((area)**0.622)*(A**0.785)*(t_c_w**-0.4)*((1+taper)**0.05)*((np.cos(sweep))**-1)*(S_cws**0.806)
    weight = weight * Units.lb # Convert lb to kg

    return weight