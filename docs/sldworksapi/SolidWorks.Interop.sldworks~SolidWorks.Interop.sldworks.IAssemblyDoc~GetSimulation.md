# GetSimulation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetSimulation`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSimulation() As Simulation
```

```

Dim instance As IAssemblyDoc
Dim value As Simulation
 
value = instance.GetSimulation()
```

```

Simulation GetSimulation()
```

```

Simulation^ GetSimulation(); 
```

#### Return Value

[ISimulation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.md)

Remarks

The Simulation folder is returned even if the folder does not yet exist or does not currently appear in the FeatureManager design tree.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
