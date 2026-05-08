# ISetSkippedItemArray Method (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetSkippedItemArray`

Sets the skipped items in this table-driven pattern feature.
Sets the skipped items in this table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetSkippedItemArray( _
   ByVal Count As System.Integer, _
   ByRef ArrayDataIn As System.Integer _
) 
```

```

Dim instance As ITablePatternFeatureData
Dim Count As System.Integer
Dim ArrayDataIn As System.Integer
 
instance.ISetSkippedItemArray(Count, ArrayDataIn)
```

```

void ISetSkippedItemArray( 
   System.int Count,
   ref System.int ArrayDataIn
)
```

```

void ISetSkippedItemArray( 
   System.int Count,
   System.int% ArrayDataIn
) 
```

#### Parameters

*Count*
:   Number of skipped items

*ArrayDataIn*
:   - in-process, unmanaged C++: Pointer to an array of skipped items

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[ITablePatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetSkippedItemCount.md)  
[ITablePatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetSkippedItemArray.md)  
[ITablePatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~SkippedItemArray.md)
