# GetReplacementSurfacesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~GetReplacementSurfacesCount`

Gets the number of replacement surfaces for this feature.
Gets the number of replacement surfaces for this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReplacementSurfacesCount() As System.Integer
```

```

Dim instance As IReplaceFaceFeatureData
Dim value As System.Integer
 
value = instance.GetReplacementSurfacesCount()
```

```

System.int GetReplacementSurfacesCount()
```

```

System.int GetReplacementSurfacesCount(); 
```

#### Return Value

Number of replacement surfaces

Remarks

Call this method before calling [IReplaceFaceFeatureData::IGetReplacementSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~IGetReplacementSurfaces.md).

Example

See the [IReplaceFaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.md)  
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.md)  
[IReplaceFaceFeatureData::ISetReplacementSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ISetReplacementSurfaces.md)  
[IReplaceFaceFeatureData::ReplacementSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ReplacementSurfaces.md)
