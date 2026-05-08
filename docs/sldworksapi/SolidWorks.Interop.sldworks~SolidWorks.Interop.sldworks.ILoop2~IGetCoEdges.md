# IGetCoEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetCoEdges`

Gets the coedges in this loop.
Gets the coedges in this loop.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCoEdges( _
   ByVal NumCoEdges As System.Integer _
) As CoEdge
```

```

Dim instance As ILoop2
Dim NumCoEdges As System.Integer
Dim value As CoEdge
 
value = instance.IGetCoEdges(NumCoEdges)
```

```

CoEdge IGetCoEdges( 
   System.int NumCoEdges
)
```

```

CoEdge^ IGetCoEdges( 
   System.int NumCoEdges
) 
```

#### Parameters

*NumCoEdges*
:   Number of coedges in this loop

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [coedges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ILoop2::GetCoEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdgeCount.md) to get NumCoEdges.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)  
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.md)  
[ILoop2::GetCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdges.md)  
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.md)  
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.md)  
[ICoEdge::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetNext.md)  
[ICoEdge::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetNext.md)
