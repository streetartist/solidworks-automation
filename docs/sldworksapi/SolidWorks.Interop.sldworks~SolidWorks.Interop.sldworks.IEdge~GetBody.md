# GetBody Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetBody`

Gets the body for this edge.
Gets the body for this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBody() As Body2
```

```

Dim instance As IEdge
Dim value As Body2
 
value = instance.GetBody()
```

```

Body2 GetBody()
```

```

Body2^ GetBody(); 
```

#### Return Value

Pointer to the [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) object for this edge

Example

[Extend Surface (VBA)](Extend_Surface_Example_VB.htm)  
[Create Temporary Bodies by Offsetting Surface Body (C#)](Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_CSharp.htm)  
[Create Temporary Bodies by Offsetting Surface Body (VB.NET)](Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_VBNET.htm)  
[Create Temporary Bodies by Offsetting Surface Body (VBA)](Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)
