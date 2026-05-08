# IGetEdgeFins Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetEdgeFins`

Gets all of the fin IDs corresponding to a edge.
Gets all of the fin IDs corresponding to a edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEdgeFins( _
   ByVal EdgeObj As Edge _
) As System.Integer
```

```

Dim instance As ITessellation
Dim EdgeObj As Edge
Dim value As System.Integer
 
value = instance.IGetEdgeFins(EdgeObj)
```

```

System.int IGetEdgeFins( 
   Edge EdgeObj
)
```

```

System.int IGetEdgeFins( 
   Edge^ EdgeObj
) 
```

#### Parameters

*EdgeObj*
:   [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) object

#### Return Value

- in-process, unmanaged C++: Pointer to an array of long or integer values describing the unique fin ID of every fin shared by this edge

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellation::GetEdgeFins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetEdgeFins.md)
