# RemoveRedundantTopology Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveRedundantTopology`

Removes redundant topology from the body.
Removes redundant topology from the body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveRedundantTopology() As System.Boolean
```

```

Dim instance As IBody2
Dim value As System.Boolean
 
value = instance.RemoveRedundantTopology()
```

```

System.bool RemoveRedundantTopology()
```

```

System.bool RemoveRedundantTopology(); 
```

#### Return Value

True if the redundant topology is removed successfully, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IEdge::RemoveRedundantTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveRedundantTopology.md)  
[IFace2::RemoveRedundantTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveRedundantTopology.md)
