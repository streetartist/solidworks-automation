# IGetErrorListCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorListCount`

Gets number of tessellation errors by error type.
Gets number of tessellation errors by error type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetErrorListCount( _
   ByRef FaceErrArrayCount As System.Integer, _
   ByRef FacetErrArrayCount As System.Integer, _
   ByRef VertexPointErrArrayCount As System.Integer, _
   ByRef VertexNormalErrArrayCount As System.Integer, _
   ByRef VertexParamsErrArrayCount As System.Integer _
) 
```

```

Dim instance As ITessellation
Dim FaceErrArrayCount As System.Integer
Dim FacetErrArrayCount As System.Integer
Dim VertexPointErrArrayCount As System.Integer
Dim VertexNormalErrArrayCount As System.Integer
Dim VertexParamsErrArrayCount As System.Integer
 
instance.IGetErrorListCount(FaceErrArrayCount, FacetErrArrayCount, VertexPointErrArrayCount, VertexNormalErrArrayCount, VertexParamsErrArrayCount)
```

```

void IGetErrorListCount( 
   out System.int FaceErrArrayCount,
   out System.int FacetErrArrayCount,
   out System.int VertexPointErrArrayCount,
   out System.int VertexNormalErrArrayCount,
   out System.int VertexParamsErrArrayCount
)
```

```

void IGetErrorListCount( 
   [Out] System.int FaceErrArrayCount,
   [Out] System.int FacetErrArrayCount,
   [Out] System.int VertexPointErrArrayCount,
   [Out] System.int VertexNormalErrArrayCount,
   [Out] System.int VertexParamsErrArrayCount
) 
```

#### Parameters

*FaceErrArrayCount*
:   Number of face errors

*FacetErrArrayCount*
:   Number of facet errors

*VertexPointErrArrayCount*
:   Number of vertex point errors

*VertexNormalErrArrayCount*
:   Number of vertex point errors

*VertexParamsErrArrayCount*
:   Number of vertex parameter errors

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellation::IGetErrorList2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList2.md)  
[ITessellation::GetErrorList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetErrorList.md)  
[ITessellate::NeedErrorList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedErrorList.md)
