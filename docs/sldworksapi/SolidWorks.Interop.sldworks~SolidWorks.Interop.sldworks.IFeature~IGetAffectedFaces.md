# IGetAffectedFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetAffectedFaces`

Gets the faces modified by a feature, such as a draft feature.
Gets the faces modified by a feature, such as a draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAffectedFaces( _
   ByRef NCount As System.Integer _
) As Face2
```

```

Dim instance As IFeature
Dim NCount As System.Integer
Dim value As Face2
 
value = instance.IGetAffectedFaces(NCount)
```

```

Face2 IGetAffectedFaces( 
   ref System.int NCount
)
```

```

Face2^ IGetAffectedFaces( 
   System.int% NCount
) 
```

#### Parameters

*NCount*
:   Number of faces modified by a feature

#### Return Value

- in-process, unmanaged C++: Pointer to array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

To determine size the of the array, call [IFeature::GetAffectedFaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaceCount.md) before calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetAffectedFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaceCount.md)  
[IFeature::GetAffectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaces.md)
