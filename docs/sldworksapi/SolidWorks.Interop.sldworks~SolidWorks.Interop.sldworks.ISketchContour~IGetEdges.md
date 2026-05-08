# IGetEdges Method (ISketchContour)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~IGetEdges`

Gets the edges in this sketch contour.
Gets the edges in this sketch contour.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEdges( _
   ByVal Count As System.Integer _
) As Edge
```

```

Dim instance As ISketchContour
Dim Count As System.Integer
Dim value As Edge
 
value = instance.IGetEdges(Count)
```

```

Edge IGetEdges( 
   System.int Count
)
```

```

Edge^ IGetEdges( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of edges

#### Return Value

- in-process, unmanaged C++: Pointer to an array of the [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISketchContour::GetEdgesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetEdgesCount.md) to get the value for Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md)  
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.md)  
[ISketchContour::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetEdges.md)
