# RemoveRedundantTopology Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveRedundantTopology`

Removes redundant topology from the face.
Removes redundant topology from the face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveRedundantTopology() As System.Boolean
```

```

Dim instance As IFace2
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

True if the redundant topology was removed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IEdge::RemoveRedundantTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveRedundantTopology.md)  
[IBody2::RemoveRedundantTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveRedundantTopology.md)
