# GetSkippedItemCount Method (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetSkippedItemCount`

Gets the number of skipped items in this }}-->table-driven pattern feature.
Gets the number of skipped items in this table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSkippedItemCount() As System.Integer
```

```

Dim instance As ITablePatternFeatureData
Dim value As System.Integer
 
value = instance.GetSkippedItemCount()
```

```

System.int GetSkippedItemCount()
```

```

System.int GetSkippedItemCount(); 
```

#### Return Value

Number of skipped items

Remarks

Call this method before calling [ITablePatternFeatureData::IGetSkippedItemArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetSkippedItemArray.md) to get the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[ITablePatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetSkippedItemArray.md)  
[ITablePatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetSkippedItemArray.md)  
[ITablePatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~SkippedItemArray.md)
