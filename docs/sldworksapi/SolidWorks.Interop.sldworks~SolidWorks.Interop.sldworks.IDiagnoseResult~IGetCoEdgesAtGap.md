# IGetCoEdgesAtGap Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~IGetCoEdgesAtGap`

Gets the coedges at the specified gap.
Gets the coedges at the specified gap.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCoEdgesAtGap( _
   ByVal Index As System.Integer, _
   ByVal CoEdgeCount As System.Integer _
) As CoEdge
```

```

Dim instance As IDiagnoseResult
Dim Index As System.Integer
Dim CoEdgeCount As System.Integer
Dim value As CoEdge
 
value = instance.IGetCoEdgesAtGap(Index, CoEdgeCount)
```

```

CoEdge IGetCoEdgesAtGap( 
   System.int Index,
   System.int CoEdgeCount
)
```

```

CoEdge^ IGetCoEdgesAtGap( 
   System.int Index,
   System.int CoEdgeCount
) 
```

#### Parameters

*Index*
:   Index number of the gap to get

*CoEdgeCount*
:   Number of coedges at that gap

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [ICoEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md) objects

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call:

- [IDiagnoseResult::GetGapsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~GetGapsCount.md) before calling this method to determine the index number of the gap to get on this body.
- [IDiagnoseResult::GetCoEdgesCountAtGap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~GetCoEdgesCountAtGap.md) before calling this method to get the number of coedges at the gap on this body.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDiagnoseResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.md)  
[IDiagnoseResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult_members.md)
