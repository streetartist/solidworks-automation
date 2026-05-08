# Duration Property (ISimulation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~Duration`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Duration As System.Double
```

```

Dim instance As ISimulation
Dim value As System.Double
 
value = instance.Duration
```

```

System.double Duration {get;}
```

```

property System.double Duration {
   System.double get();
}
```

#### Property Value

Elapsed time in seconds

Remarks

If the Physical Simulation has not yet been calculated, then the return value is 0.0.

The return value represents the length of time that the simulation is expected to last. This means that if a bouncing ball takes 15 seconds to come to a stop, then this property returns a value of 15.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.md)  
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.md)
