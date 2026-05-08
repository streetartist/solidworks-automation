# ImprintingFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ImprintingFaces`

Imprints the specified tool faces onto the specified target faces.
Imprints the specified tool faces onto the specified target faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ImprintingFaces( _
   ByVal TargetFaceArray As System.Object, _
   ByVal ToolFaceArray As System.Object, _
   ByVal Options As System.Integer, _
   ByRef TargetEdges As System.Object, _
   ByRef ToolEdges As System.Object, _
   ByRef TargetVertices As System.Object, _
   ByRef ToolVertices As System.Object _
) As System.Boolean
```

```

Dim instance As IModeler
Dim TargetFaceArray As System.Object
Dim ToolFaceArray As System.Object
Dim Options As System.Integer
Dim TargetEdges As System.Object
Dim ToolEdges As System.Object
Dim TargetVertices As System.Object
Dim ToolVertices As System.Object
Dim value As System.Boolean
 
value = instance.ImprintingFaces(TargetFaceArray, ToolFaceArray, Options, TargetEdges, ToolEdges, TargetVertices, ToolVertices)
```

```

System.bool ImprintingFaces( 
   System.object TargetFaceArray,
   System.object ToolFaceArray,
   System.int Options,
   out System.object TargetEdges,
   out System.object ToolEdges,
   out System.object TargetVertices,
   out System.object ToolVertices
)
```

```

System.bool ImprintingFaces( 
   System.Object^ TargetFaceArray,
   System.Object^ ToolFaceArray,
   System.int Options,
   [Out] System.Object^ TargetEdges,
   [Out] System.Object^ ToolEdges,
   [Out] System.Object^ TargetVertices,
   [Out] System.Object^ ToolVertices
) 
```

#### Parameters

*TargetFaceArray*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that describe the target body

*ToolFaceArray*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that describe the tool body

*Options*
:   Options for this operation as defined in [swImprintingFacesOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImprintingFacesOpts_e.html)

*TargetEdges*
:   Array target [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

*ToolEdges*
:   Array of tool [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

*TargetVertices*
:   Array of target [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

*ToolVertices*
:   Array of tool [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

#### Return Value

True if the operation was successful, false if not

Remarks

The target and tool faces must:

- belong to different bodies.
- intersect each other.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::IImprintingFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFaces.md)  
[IModeler::IImprintingFacesCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFacesCount2.md)
