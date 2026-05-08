# Status Property (ISimulation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~Status`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Status As System.Boolean
```

```

Dim instance As ISimulation
Dim value As System.Boolean
 
value = instance.Status
```

```

System.bool Status {get;}
```

```

property System.bool Status {
   System.bool get();
}
```

#### Property Value

True if the Physical Simulation has been calculated, false if it has not or if the calculation was unsuccessful

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.md)  
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.md)
