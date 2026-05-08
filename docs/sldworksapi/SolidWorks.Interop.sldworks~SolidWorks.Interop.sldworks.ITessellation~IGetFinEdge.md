# IGetFinEdge Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFinEdge`

Gets the edge corresponding to a fin.
Gets the edge corresponding to a fin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFinEdge( _
   ByVal FinId As System.Integer _
) As Edge
```

```

Dim instance As ITessellation
Dim FinId As System.Integer
Dim value As Edge
 
value = instance.IGetFinEdge(FinId)
```

```

Edge IGetFinEdge( 
   System.int FinId
)
```

```

Edge^ IGetFinEdge( 
   System.int FinId
) 
```

#### Parameters

*FinId*
:   ID of the fin from which you want to return the edge

#### Return Value

[Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) with which this fin is shared

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)
