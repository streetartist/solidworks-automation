# IExtendSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IExtendSurface`

Creates a new temporary body by extending the selected edges.
Creates a new temporary body by extending the selected edges.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IExtendSurface( _
   ByVal EdgeCount As System.Integer, _
   ByRef EdgesToExtend As Edge, _
   ByVal ExtendLinear As System.Boolean, _
   ByVal EndCondition As System.Integer, _
   ByVal Dist As System.Double, _
   ByVal PUpToVtx As Vertex, _
   ByVal PUpToFace As Face _
) As Body2
```

```

Dim instance As IBody2
Dim EdgeCount As System.Integer
Dim EdgesToExtend As Edge
Dim ExtendLinear As System.Boolean
Dim EndCondition As System.Integer
Dim Dist As System.Double
Dim PUpToVtx As Vertex
Dim PUpToFace As Face
Dim value As Body2
 
value = instance.IExtendSurface(EdgeCount, EdgesToExtend, ExtendLinear, EndCondition, Dist, PUpToVtx, PUpToFace)
```

```

Body2 IExtendSurface( 
   System.int EdgeCount,
   ref Edge EdgesToExtend,
   System.bool ExtendLinear,
   System.int EndCondition,
   System.double Dist,
   Vertex PUpToVtx,
   Face PUpToFace
)
```

```

Body2^ IExtendSurface( 
   System.int EdgeCount,
   Edge^% EdgesToExtend,
   System.bool ExtendLinear,
   System.int EndCondition,
   System.double Dist,
   Vertex^ PUpToVtx,
   Face^ PUpToFace
) 
```

#### Parameters

*EdgeCount*
:   Number of edges to extend

*EdgesToExtend*
:   Array of the selected [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) to extend

*ExtendLinear*
:   True to extend the selected edges linearly along the tangent of the face at the edges; false to extend the selected edges in the same direction as the face

*EndCondition*
:   - 0 = Extend selected edges per value specified for Dist
    - 1 = Extend selected edges to PUpToVtx
    - 2 = Extend selected edges to PpUpToFace

*Dist*
:   Distance by which to extend the selected edges (see **Remarks**)

*PUpToVtx*
:   [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) up to which to extend the selected edges  (see Remarks)

*PUpToFace*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) up to which to extend the selected edges (see Remarks)

#### Return Value

Pointer to the newly created [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) object

Remarks

This method supports surface bodies only.

You can extend the edges by a specified distance or up to a vertex or up to a face.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::ExtendSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ExtendSurface.md)
