# IGetErrorList Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList`

Obsolete. Superseded by ITessellation::IGetErrorList2.
Obsolete. Superseded by [ITessellation::IGetErrorList2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetErrorList( _
   ByRef FaceErrArray As Face, _
   ByRef FacetErrArray As System.Integer, _
   ByRef VertexPointErrArray As System.Integer, _
   ByRef VertexNormalErrArray As System.Integer, _
   ByRef VertexParamsErrArray As System.Integer _
) 
```

```

Dim instance As ITessellation
Dim FaceErrArray As Face
Dim FacetErrArray As System.Integer
Dim VertexPointErrArray As System.Integer
Dim VertexNormalErrArray As System.Integer
Dim VertexParamsErrArray As System.Integer
 
instance.IGetErrorList(FaceErrArray, FacetErrArray, VertexPointErrArray, VertexNormalErrArray, VertexParamsErrArray)
```

```

void IGetErrorList( 
   out Face FaceErrArray,
   out System.int FacetErrArray,
   out System.int VertexPointErrArray,
   out System.int VertexNormalErrArray,
   out System.int VertexParamsErrArray
)
```

```

void IGetErrorList( 
   [Out] Face^ FaceErrArray,
   [Out] System.int FacetErrArray,
   [Out] System.int VertexPointErrArray,
   [Out] System.int VertexNormalErrArray,
   [Out] System.int VertexParamsErrArray
) 
```

#### Parameters

*FaceErrArray*

*FacetErrArray*

*VertexPointErrArray*

*VertexNormalErrArray*

*VertexParamsErrArray*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)
