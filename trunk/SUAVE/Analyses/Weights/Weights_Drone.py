## @ingroup Analyses-Weights
# Weights_Drone.py
#
# Created: May 2018, Matthew Clarke

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
from SUAVE.Core import Data
from Weights import Weights


# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

## @ingroup Analyses-Weights
class Weights_Drone(Weights):
    """ This is class that evaluates the weight of a small drone
    
    Assumptions:
        None

    Source:
        N/A

    Inputs:
        None
      
    Outputs:
        None

    Properties Used:
        N/A
    """
    def __defaults__(self):
        """This sets the default values and methods for the Drone weight analysis.
    
        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        None

        Properties Used:
        N/A
        """           
        self.tag = 'weights_drone'
        
        self.vehicle  = Data()
        self.settings = Data()
        
        
    def evaluate(self,conditions=None):
        """Evaluate the weight analysis.
    
        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        results

        Properties Used:
        N/A
        """         
        # unpack
        vehicle = self.vehicle
        empty   = SUAVE.Methods.Weights.Correlations.Drone.empty     

        
        # evaluate
        results = empty(vehicle)
        
        # storing weigth breakdown into vehicle
        vehicle.weight_breakdown = results 

        # updating empty weight
        vehicle.mass_properties.operating_empty = results.empty
              
        # done!
        return results
    
    
    def finalize(self):
        """Finalize the weight analysis.
    
        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        None

        Properties Used:
        N/A
        """           
        self.mass_properties = self.vehicle.mass_properties
        
        return
        