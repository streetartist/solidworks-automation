# IGetSilhoutteEdgeCount Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdgeCount`

Gets the number of silhouette edges for this face.
Gets the number of silhouette edges for this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSilhoutteEdgeCount( _
   ByRef Root As System.Double, _
   ByRef Normal As System.Double _
) As System.Integer
```

```

Dim instance As IFace2
Dim Root As System.Double
Dim Normal As System.Double
Dim value As System.Integer
 
value = instance.IGetSilhoutteEdgeCount(Root, Normal)
```

```

System.int IGetSilhoutteEdgeCount( 
   ref System.double Root,
   ref System.double Normal
)
```

```

System.int IGetSilhoutteEdgeCount( 
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

Number of silhouette edges

Remarks

This method calculates the number of edges returned by [IFace2::IGetSilhoutteEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdges.md) for a given vector root point (root) and a vector direction (normal). Call this method before calling IFace2::IGetSilhoutte.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetSilhoutteEdgesVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSilhoutteEdgesVB.md)
