# ISimulation Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation`

This interface is: obsolete and has not been superseded. nonfunctional in SOLIDWORKS 2008 and later. Use the interfaces related to motion studies introduced in SOLIDWORKS 2008 to access animation a
This interface is:

- obsolete and has not been superseded.
- nonfunctional in SOLIDWORKS 2008 and later.

Use the interfaces related to [motion studies](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudyManager.md) introduced in SOLIDWORKS 2008 to access animation and simulation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISimulation 
```

```

Dim instance As ISimulation
```

```

public interface ISimulation 
```

```

public interface class ISimulation 
```

Remarks

Do not confuse Physical Simulation with [animation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation.md). The SOLIDWORKS software computes a Physical Simulation, which generates a number of steps (and transforms) and elapsed time for those steps. The SOLIDWORKS software then displays the computed Physical Simulation using animation. To create the display, the animation process takes the Physical Simulation steps and does a linear interpolation of those steps for the elapsed time. The elapsed time and frames of Physical Simulation will most likely be different than the elapsed time and frames of an animation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
