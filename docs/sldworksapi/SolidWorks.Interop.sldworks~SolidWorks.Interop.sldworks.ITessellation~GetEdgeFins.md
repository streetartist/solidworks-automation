# GetEdgeFins Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetEdgeFins`

Gets all of the fin IDs corresponding to a edge.
Gets all of the fin IDs corresponding to a edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEdgeFins( _
   ByVal EdgeDisp As System.Object _
) As System.Object
```

```

Dim instance As ITessellation
Dim EdgeDisp As System.Object
Dim value As System.Object
 
value = instance.GetEdgeFins(EdgeDisp)
```

```

System.object GetEdgeFins( 
   System.object EdgeDisp
)
```

```

System.Object^ GetEdgeFins( 
   System.Object^ EdgeDisp
) 
```

#### Parameters

*EdgeDisp*
:   [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) object

#### Return Value

Array of long or integer values describing the unique fin ID of every fin shared by this edge

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellation::IGetEdgeFins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetEdgeFins.md)
