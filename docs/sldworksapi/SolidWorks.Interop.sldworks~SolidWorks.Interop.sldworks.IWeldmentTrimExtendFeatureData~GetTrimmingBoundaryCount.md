# GetTrimmingBoundaryCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundaryCount`

Gets the number of trimming boundaries.
Gets the number of trimming boundaries.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTrimmingBoundaryCount() As System.Integer
```

```

Dim instance As IWeldmentTrimExtendFeatureData
Dim value As System.Integer
 
value = instance.GetTrimmingBoundaryCount()
```

```

System.int GetTrimmingBoundaryCount()
```

```

System.int GetTrimmingBoundaryCount(); 
```

#### Return Value

Number of trimming boundaries

Remarks

Only end-trim corner types (swEndConditionTrim) can have multiple boundaries. Use [IWeldmentTrimExtendFeatureData::CornerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.md) to determine the type of corner.

Call this method before calling [IWeldmentTrimExtendFeaturedata::IGetTrimmingBoundary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetTrimmingBoundary.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.md)  
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.md)  
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::ISetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::SetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~SetTrimmingBoundary.md)
