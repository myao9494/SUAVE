## @ingroup Methods-Weights-Correlations-Drone
# empty.py
# 
# Created:  Feb 2018, M. Clarke
# Modified: 

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------
import SUAVE
from SUAVE.Core import Units, Data
from SUAVE.Methods.Weights.Correlations import Propulsion as Propulsion
import warnings

# ----------------------------------------------------------------------
#  Empty
# ----------------------------------------------------------------------
## @ingroup Methods-Weights-Correlations-Drone
def empty(vehicle):
    """ output = SUAVE.Methods.Weights.Correlations.Drone.empty(wing,center_body)
        Computes the empty weight breakdown of a small drone  
        
        Inputs:
            vehicle - a data dictionary with the fields:                    
                    payload        -  payload weight                                           [kilograms]
                
                fuselage
                    fuselages['center_body'] - center body weight                              [kilograms]
                propulsors - a data dictionary with the fields: 
                    propeller
                       prop radius                                                             [meters]             
                                           
                       number_motors - integer indicating the number of engines on the aircraft

                wings - a data dictionary with the fields:    
                    wing - a data dictionary with the fields:
                        areas.reference           - reference area of wing                     [meters**2]
                        thickness_to_chord        - thickness-to-chord ratio of the wing       [dimensionless]
                      
            
        Outputs:
            output - a data dictionary with fields:
                wing - wing weight                            [kilograms]
                center_body - center_body weight              [kilograms]
                propulsion - propulsion                       [kilograms]

       Assumptions:
            calculated aircraft weight from correlations created per component of historical aircraft
            plastic props
            foam wings  - http://www.foamular.com/foam/docs/ASTM_C578_Types.pdf
    """     

    # Compute drone payload weight
    wt_payload    = vehicle.propulsors.network.payload.mass_properties.mass
  
    # Compute drone motor weight weight
    Kv = vehicle.propulsors.network.motor.speed_constant 
    wt_motor       = 10**4.0499*Kv**-0.5329
    
    # Compute drone propeller weight weight
    num_eng        = vehicle.propulsors.network.number_of_engines
    D              = vehicle.propulsors.network.propeller.prop_attributes.tip_radius*2
    wt_propulsion  = num_eng * (0.05555*D**2 + 0.2216*D)
    
    # Compute drone wing weight
    if len(vehicle.wings.keys())==0:
        total_drone_wt_wing  = 0.0        
    else:
        for wing in vehicle.wings():
            b          = wing.spans.projected
            mac        = wing.chords.mean_aerodynamic
            t_c_w      = wing.thickness_to_chord
            density_foam =  20 
            wt_wing    = (8221*t_c_w/12000)*density_foam*b*mac**2
            total_drone_wt_wing += wt_wing  
    
   
    # Compute drone center body weight      
    if len(vehicle.fuselages.keys())==0:
        wt_center_body = 0.0
    else:
        wt_center_body =  vehicle.fuselages['center_body'].mass_properties.mass
        
    # total drone weight
    wt_drone = wt_center_body + total_drone_wt_wing + wt_payload + wt_propulsion
    
    # Pack
    weight = Data()
    weight.empty = wt_drone  
    
    return weight