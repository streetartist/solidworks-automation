# GetFacesForReplacementCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~GetFacesForReplacementCount`

Gets the number of faces to replace in this feature.
Gets the number of faces to replace in this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFacesForReplacementCount() As System.Integer
```

```

Dim instance As IReplaceFaceFeatureData
Dim value As System.Integer
 
value = instance.GetFacesForReplacementCount()
```

```

System.int GetFacesForReplacementCount()
```

```

System.int GetFacesForReplacementCount(); 
```

#### Return Value

Number of faces to replace

Remarks

Call this method before calling [IReplaceFaceFeatureData::IGetFacesForReplacement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~IGetFacesForReplacement.md).

Example

See the [IReplaceFaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.md)  
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.md)  
[IReplaceFaceFeatureData::ISetFacesForReplacement Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ISetFacesForReplacement.md)  
[IReplaceFaceFeatureData::FacesForReplacement Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~FacesForReplacement.md)
