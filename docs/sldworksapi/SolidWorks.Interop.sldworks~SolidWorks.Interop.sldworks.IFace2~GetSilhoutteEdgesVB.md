# GetSilhoutteEdgesVB Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSilhoutteEdgesVB`

Gets the silhouette edges.
Gets the silhouette edges.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSilhoutteEdgesVB( _
   ByVal Xroot As System.Double, _
   ByVal Yroot As System.Double, _
   ByVal Zroot As System.Double, _
   ByVal Xnormal As System.Double, _
   ByVal Ynormal As System.Double, _
   ByVal Znormal As System.Double _
) As System.Object
```

```

Dim instance As IFace2
Dim Xroot As System.Double
Dim Yroot As System.Double
Dim Zroot As System.Double
Dim Xnormal As System.Double
Dim Ynormal As System.Double
Dim Znormal As System.Double
Dim value As System.Object
 
value = instance.GetSilhoutteEdgesVB(Xroot, Yroot, Zroot, Xnormal, Ynormal, Znormal)
```

```

System.object GetSilhoutteEdgesVB( 
   System.double Xroot,
   System.double Yroot,
   System.double Zroot,
   System.double Xnormal,
   System.double Ynormal,
   System.double Znormal
)
```

```

System.Object^ GetSilhoutteEdgesVB( 
   System.double Xroot,
   System.double Yroot,
   System.double Zroot,
   System.double Xnormal,
   System.double Ynormal,
   System.double Znormal
) 
```

#### Parameters

*Xroot*
:   X component of the root point

*Yroot*
:   Y component of the root point

*Zroot*
:   Z component of the root point

*Xnormal*
:   X component of the direction vector

*Ynormal*
:   Y component of the direction vector

*Znormal*
:   Z component of the direction vector

#### Return Value

Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

Remarks

The return array has two elements for each edge: the first is the silhouette edge and the second is unused. To iterate through the edges, an application needs to step through every second element.

The returned edges are transient and cannot be selected.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::IGetSilhoutteEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdges.md)  
[IFace2::IGetSilhoutteEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdgeCount.md)  
[IModelDoc2::InsertSplitLineSil Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineSil.md)
