# IGetSkippedItemArray Method (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetSkippedItemArray`

Gets the skipped items in this table-driven pattern feature.
Gets the skipped items in this table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSkippedItemArray( _
   ByVal Count As System.Integer _
) As System.Integer
```

```

Dim instance As ITablePatternFeatureData
Dim Count As System.Integer
Dim value As System.Integer
 
value = instance.IGetSkippedItemArray(Count)
```

```

System.int IGetSkippedItemArray( 
   System.int Count
)
```

```

System.int IGetSkippedItemArray( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of skipped items

#### Return Value

- in-process, unmanaged C++: Pointer to an array of skipped items

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Call [ITablePatternFeatureData::GetSkippedItemCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetSkippedItemCount.md) before calling this method to get the size of the array.

Because this is a 0-based array, if you skipped the third feature and fifth feature in the pattern, then:

- 0 = 3
- 1 = 5

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[ITablePatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetSkippedItemArray.md)  
[ITablePatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~SkippedItemArray.md)
