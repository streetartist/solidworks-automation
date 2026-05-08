# IGetFaceFacets Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacets`

Obsolete. Superseded by ITessellation::IGetFaceFacets2.
Obsolete. Superseded by [ITessellation::IGetFaceFacets2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacets2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFaceFacets( _
   ByVal FaceObj As Face _
) As System.Integer
```

```

Dim instance As ITessellation
Dim FaceObj As Face
Dim value As System.Integer
 
value = instance.IGetFaceFacets(FaceObj)
```

```

System.int IGetFaceFacets( 
   Face FaceObj
)
```

```

System.int IGetFaceFacets( 
   Face^ FaceObj
) 
```

#### Parameters

*FaceObj*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)
