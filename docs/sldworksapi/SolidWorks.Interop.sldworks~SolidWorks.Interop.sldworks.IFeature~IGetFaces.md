# IGetFaces Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces`

Obsolete. Superseded by IFeature::IGetFaces2.
Obsolete. Superseded by [IFeature::IGetFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFaces( _
   ByRef FaceCount As System.Integer _
) As Face
```

```

Dim instance As IFeature
Dim FaceCount As System.Integer
Dim value As Face
 
value = instance.IGetFaces(FaceCount)
```

```

Face IGetFaces( 
   out System.int FaceCount
)
```

```

Face^ IGetFaces( 
   [Out] System.int FaceCount
) 
```

#### Parameters

*FaceCount*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)
