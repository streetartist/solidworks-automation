# IGetEdgeFinsCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetEdgeFinsCount`

Gets the number of fins corresponding to an edge.
Gets the number of fins corresponding to an edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEdgeFinsCount( _
   ByVal EdgeObj As Edge _
) As System.Integer
```

```

Dim instance As ITessellation
Dim EdgeObj As Edge
Dim value As System.Integer
 
value = instance.IGetEdgeFinsCount(EdgeObj)
```

```

System.int IGetEdgeFinsCount( 
   Edge EdgeObj
)
```

```

System.int IGetEdgeFinsCount( 
   Edge^ EdgeObj
) 
```

#### Parameters

*EdgeObj*
:   [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) object of which to get the number

#### Return Value

Number of fins corresponding to the specified edge

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)
