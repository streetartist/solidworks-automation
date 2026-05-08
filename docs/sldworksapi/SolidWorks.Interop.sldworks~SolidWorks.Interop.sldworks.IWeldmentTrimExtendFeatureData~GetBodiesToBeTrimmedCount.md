# GetBodiesToBeTrimmedCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetBodiesToBeTrimmedCount`

Gets the number of bodies to trim.
Gets the number of bodies to trim.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBodiesToBeTrimmedCount() As System.Integer
```

```

Dim instance As IWeldmentTrimExtendFeatureData
Dim value As System.Integer
 
value = instance.GetBodiesToBeTrimmedCount()
```

```

System.int GetBodiesToBeTrimmedCount()
```

```

System.int GetBodiesToBeTrimmedCount(); 
```

#### Return Value

Number of bodies to trim

Remarks

Only end-trim corner types (swEndConditionTrim) can have multiple bodies to trim. Use [IWeldmentTrimExtendFeatureData::CornerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.md) to determine the type of corner.

Call this method before calling [IWeldmentTrimExtendFeatureData::IGetBodiesToBeTrimmed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetBodiesToBeTrimmed.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.md)  
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.md)  
[IWeldmentTrimExtendFeatureData::ISetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::BodiesToBeTrimmed Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~BodiesToBeTrimmed.md)
