# GetPiecesToKeepCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~GetPiecesToKeepCount`

Gets the number of pieces to keep for this surface trim feature.
Gets the number of pieces to keep for this surface trim feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPiecesToKeepCount() As System.Integer
```

```

Dim instance As ISurfaceTrimFeatureData
Dim value As System.Integer
 
value = instance.GetPiecesToKeepCount()
```

```

System.int GetPiecesToKeepCount()
```

```

System.int GetPiecesToKeepCount(); 
```

#### Return Value

Number of pieces to keep

Remarks

Call this method before calling [ISurfaceTrimFeatureData::IGetPiecesToKeep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~IGetPiecesToKeep.md) to get the size of the array for that method.

Example

See the [ISurfaceTrimFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.md)  
[ISurfaceTrimFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData_members.md)  
[ISurfaceTrimFeatureData::ISetPiecesToKeep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~ISetPiecesToKeep.md)  
[ISurfaceTrimFeatureData::PiecesToKeep Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~PiecesToKeep.md)
