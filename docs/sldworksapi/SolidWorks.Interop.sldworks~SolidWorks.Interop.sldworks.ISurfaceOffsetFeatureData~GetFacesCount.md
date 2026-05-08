# GetFacesCount Method (ISurfaceOffsetFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~GetFacesCount`

Obsolete. Superseded by ISurfaceOffsetFeatureData::GetEntitiesCount.
Obsolete. Superseded by [ISurfaceOffsetFeatureData::GetEntitiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~GetEntitiesCount.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFacesCount() As System.Integer
```

```

Dim instance As ISurfaceOffsetFeatureData
Dim value As System.Integer
 
value = instance.GetFacesCount()
```

```

System.int GetFacesCount()
```

```

System.int GetFacesCount(); 
```

#### Return Value

Number of offset faces

Remarks

Call this method before calling [ISurfaceOffsetFeatureData::IGetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~IGetFaces.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.md)  
[ISurfaceOffsetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData_members.md)  
[ISurfaceOffsetFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~ISetFaces.md)  
[ISurfaceOffsetFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~Faces.md)
