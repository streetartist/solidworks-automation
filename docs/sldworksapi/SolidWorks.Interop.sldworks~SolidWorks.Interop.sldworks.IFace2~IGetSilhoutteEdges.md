# IGetSilhoutteEdges Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdges`

Gets the silhouette edges for this face with the specified root point and in the specified direction.
Gets the silhouette edges for this face with the specified root point and in the specified direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSilhoutteEdges( _
   ByRef Root As System.Double, _
   ByRef Normal As System.Double _
) As Edge
```

```

Dim instance As IFace2
Dim Root As System.Double
Dim Normal As System.Double
Dim value As Edge
 
value = instance.IGetSilhoutteEdges(Root, Normal)
```

```

Edge IGetSilhoutteEdges( 
   ref System.double Root,
   ref System.double Normal
)
```

```

Edge^ IGetSilhoutteEdges( 
   System.double% Root,
   System.double% Normal
) 
```

#### Parameters

*Root*
:   Array of doubles defining the root point

*Normal*
:   Array of doubles defining the direction vector

#### Return Value

- in-process, unmanaged C++: Pointer to an array to hold the edge pointers

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

These edges are not added to the face and cannot be found using [IFace2::IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetEdges.md). They are created and handed back to the caller as an array of edges packed with edges.

The vector root point (root) and a vector direction (normal) define the orientation for the silhouette edge creation.

The return array has two elements for each edge: the first is the silhouette edge and the second is  not used. To iterate through the edges, an application needs to step through every second element.

Before calling this method, call [IFace2::IGetSilhoutteEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdgeCount.md) to get the size of array required to hold the edges.

The returned edges are transient and cannot be selected.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetSilhoutteEdgesVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSilhoutteEdgesVB.md)
