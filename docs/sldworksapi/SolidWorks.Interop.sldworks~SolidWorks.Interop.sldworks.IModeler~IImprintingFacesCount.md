# IImprintingFacesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFacesCount`

Obsolete. Superseded by IModeler::IImprintingFacesCount2.
Obsolete. Superseded by [IModeler::IImprintingFacesCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFacesCount2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IImprintingFacesCount( _
   ByVal NTargetFaces As System.Integer, _
   ByRef TargetFaceArray As Face, _
   ByVal NToolFaces As System.Integer, _
   ByRef ToolFaceArray As Face, _
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
Dim TargetFaceArray As Face
Dim NToolFaces As System.Integer
Dim ToolFaceArray As Face
Dim Options As System.Integer
Dim NTargetEdges As System.Integer
Dim NtoolEdges As System.Integer
Dim NtargetVertices As System.Integer
Dim ToolVertices As System.Integer
Dim value As System.Boolean
 
value = instance.IImprintingFacesCount(NTargetFaces, TargetFaceArray, NToolFaces, ToolFaceArray, Options, NTargetEdges, NtoolEdges, NtargetVertices, ToolVertices)
```

```

System.bool IImprintingFacesCount( 
   System.int NTargetFaces,
   ref Face TargetFaceArray,
   System.int NToolFaces,
   ref Face ToolFaceArray,
   System.int Options,
   out System.int NTargetEdges,
   out System.int NtoolEdges,
   out System.int NtargetVertices,
   out System.int ToolVertices
)
```

```

System.bool IImprintingFacesCount( 
   System.int NTargetFaces,
   Face^% TargetFaceArray,
   System.int NToolFaces,
   Face^% ToolFaceArray,
   System.int Options,
   [Out] System.int NTargetEdges,
   [Out] System.int NtoolEdges,
   [Out] System.int NtargetVertices,
   [Out] System.int ToolVertices
) 
```

#### Parameters

*NTargetFaces*

*TargetFaceArray*

*NToolFaces*

*ToolFaceArray*

*Options*

*NTargetEdges*

*NtoolEdges*

*NtargetVertices*

*ToolVertices*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
