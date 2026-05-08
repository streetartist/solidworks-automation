# IGetPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetPoint`

Gets the point corresponding to this vertex.
Gets the point corresponding to this vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPoint() As System.Double
```

```

Dim instance As IVertex
Dim value As System.Double
 
value = instance.IGetPoint()
```

```

System.double IGetPoint()
```

```

System.double IGetPoint(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of three doubles representing the x, y, and z coordinates of the point

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)  
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.md)  
[IVertex::GetPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetPoint.md)
