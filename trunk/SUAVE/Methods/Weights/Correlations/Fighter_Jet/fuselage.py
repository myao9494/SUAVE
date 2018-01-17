## @ingroup Methods-Weights-Correlations-Fighter_Jet
# tube.py
#
# Created:  Jan 2018, M. Clarke 

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Units
import numpy as np

# ----------------------------------------------------------------------
#   Tube
# ----------------------------------------------------------------------

## @ingroup MMethods-Weights-Correlations-Fighter_Jet
def fuselage (w_fus,h_fus,l_fus,Nlim,TOW,wt_zf,K_dwf) :
    """ Calculate the weight of a fuselage in the state tube and wing configuration
    
    Assumptions:
        fuselage in a standard fighter jet configuration         
    
    Source: 
        Aircraft Design: A Conceptual Approach, 5th Edition by Daniel P. Raymer 
        
    Inputs:
        w_fus - width of the fuselage                                          [meters]
        h_fus - height of the fuselage                                         [meters]
        l_fus - length of the fuselage                                         [meters]
        Nlim - limit load factor at zero fuel weight of the aircraft           [dimensionless]
        wt_zf - zero fuel weight of the aircraft                               [kilograms]
        TOW - maximum takeoff weight of the aircraft                           [kilograms]

        
    Outputs:
        weight - weight of the fuselage                                        [kilograms]
            
    Properties Used:
        N/A
    """     
    # unpack inputs
   
    width = w_fus / Units.ft # Convert meters to ft
    height = h_fus / Units.ft # Convert meters to ft
    mtow  = TOW / Units.lb # Convert kg to lbs
    zfw   = wt_zf / Units.lb # Convert kg to lbs
    
    # setup
    length = l_fus / Units.ft # Convert meters to ft
    fuel_weight = mtow - zfw
    W_dg        = fuel_weight * 0.55 # 0.5 to 0.6 

    
    #Calculate weight of wing for traditional aircraft vertical tail without rudder
    fuselage_weight = 0.4999*K_dwf*(W_dg**0.35)*(Nlim**0.25)*(length**0.5)*(height**0.894)*(width**0.685)
    fuselage_weight = fuselage_weight * Units.lb # Convert from lbs to kg
    
    return fuselage_weight