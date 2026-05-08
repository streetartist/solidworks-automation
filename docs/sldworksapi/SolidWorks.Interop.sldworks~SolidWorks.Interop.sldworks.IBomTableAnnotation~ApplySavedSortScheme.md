# ApplySavedSortScheme Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~ApplySavedSortScheme`

Sorts this BOM table using the sort data that was previously saved in the table.
Sorts this BOM table using the sort data that was previously saved in the table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ApplySavedSortScheme( _
   ByVal SortData As BomTableSortData _
) As System.Boolean
```

```

Dim instance As IBomTableAnnotation
Dim SortData As BomTableSortData
Dim value As System.Boolean
 
value = instance.ApplySavedSortScheme(SortData)
```

```

System.bool ApplySavedSortScheme( 
   BomTableSortData SortData
)
```

```

System.bool ApplySavedSortScheme( 
   BomTableSortData^ SortData
) 
```

#### Parameters

*SortData*
:   [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md)

#### Return Value

True if BOM table is successfully sorted, false if not

Remarks

Before calling this method, you must:

1. Set [IBomTableSortData::SaveCurrentSortParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~SaveCurrentSortParameters.md) to true to indicate that the sort settings should be saved in the BOM table in the drawing.
2. [IBomTableAnnotation::Sort](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Sort.md) to actually save the sort settings in the BOM table in the drawing.
3. [IBomTableAnnotation::GetBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetBomTableSortData.md) to populate SortData.

See [Sorting Tables](sldworksapiprogguide.chm::/OVERVIEW/Sorting_Tables.htm) for more information.

Example

[Sort Table (VBA)](Sort_Table_Example_VB.htm)  
[Sort Table (VB.NET)](Sort_Table_Example_VBNET.htm)  
[Sort Table (C#)](Sort_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)
