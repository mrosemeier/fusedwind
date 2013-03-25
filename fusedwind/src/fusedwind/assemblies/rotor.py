from openmdao.main.api import Assembly
from openmdao.main.datatypes.api import Slot, Array, Float, List

from fusedwind.components.rotor import RotorAeroBase, MachineTypeBase
from fusedwind.vartrees.rotor import DistributedLoadsVT, HubLoadsVT


class RotorControllerBase(Assembly):
    """rotor controller"""

    # inputs
    raero = Slot(RotorAeroBase, iotype='in')
    machineType = Slot(MachineTypeBase)
    VLoads = Array(iotype='in')

    # outputs
    V = Array(iotype='out')  # power curve
    P = Array(iotype='out')
    AEP = Float(iotype='out')
    distributedLoads = List(DistributedLoadsVT)
    hubLoads = List(HubLoadsVT)

