# IImprintingFacesCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFacesCount2`

Gets the number of imprinted edges and vertices in the model.
Gets the number of imprinted edges and vertices in the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IImprintingFacesCount2( _
   ByVal NTargetFaces As System.Integer, _
   ByRef TargetFaceArray As Face2, _
   ByVal NToolFaces As System.Integer, _
   ByRef ToolFaceArray As Face2, _
   ByVal Options As System.Integer, _
   ByRef NTargetEdges As System.Integer, _
   ByRef NtoolEdges As System.Integer, _
   ByRef NtargetVertices As System.Integer, _
   ByRef ToolVertices As System.Integer _
) As System.Boolean
```

```

Dim instance As IModeler
Dim NTargetFaces As System.Integer
Dim TargetFaceArray As Face2
Dim NToolFaces As System.Integer
Dim ToolFaceArray As Face2
Dim Options As System.Integer
Dim NTargetEdges As System.Integer
Dim NtoolEdges As System.Integer
Dim NtargetVertices As System.Integer
Dim ToolVertices As System.Integer
Dim value As System.Boolean
 
value = instance.IImprintingFacesCount2(NTargetFaces, TargetFaceArray, NToolFaces, ToolFaceArray, Options, NTargetEdges, NtoolEdges, NtargetVertices, ToolVertices)
```

```

System.bool IImprintingFacesCount2( 
   System.int NTargetFaces,
   ref Face2 TargetFaceArray,
   System.int NToolFaces,
   ref Face2 ToolFaceArray,
   System.int Options,
   out System.int NTargetEdges,
   out System.int NtoolEdges,
   out System.int NtargetVertices,
   out System.int ToolVertices
)
```

```

System.bool IImprintingFacesCount2( 
   System.int NTargetFaces,
   Face2^% TargetFaceArray,
   System.int NToolFaces,
   Face2^% ToolFaceArray,
   System.int Options,
   [Out] System.int NTargetEdges,
   [Out] System.int NtoolEdges,
   [Out] System.int NtargetVertices,
   [Out] System.int ToolVertices
) 
```

#### Parameters

*NTargetFaces*
:   Number of faces in the target body

*TargetFaceArray*
:   Array of the [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that describe the target body

*NToolFaces*
:   Number of faces in the tool body

*ToolFaceArray*
:   Array of the [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that describe the tool body

*Options*
:   Options for this operation as defined in [swImprintingFacesOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImprintingFacesOpts_e.html)

*NTargetEdges*
:   Number of edges returned from this operation

*NtoolEdges*
:   Number of tool edges returned from this operation

*NtargetVertices*
:   Number of target vertices returned from this operation

*ToolVertices*
:   Number of tool vertices returned from this operation

#### Return Value

True if the operation is successful, false if not

Remarks

Call this method before calling [IModeler::IImprintingFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFaces.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::ImprintingFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ImprintingFaces.md)
