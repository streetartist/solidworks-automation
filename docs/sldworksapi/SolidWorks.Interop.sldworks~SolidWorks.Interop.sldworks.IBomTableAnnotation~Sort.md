# Sort Method (IBomTableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Sort`

Sorts this BOM table using the specified sorting data.
Sorts this BOM table using the specified sorting data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Sort( _
   ByVal SortData As BomTableSortData _
) As System.Boolean
```

```

Dim instance As IBomTableAnnotation
Dim SortData As BomTableSortData
Dim value As System.Boolean
 
value = instance.Sort(SortData)
```

```

System.bool Sort( 
   BomTableSortData SortData
)
```

```

System.bool Sort( 
   BomTableSortData^ SortData
) 
```

#### Parameters

*SortData*
:   [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md)

#### Return Value

True if sorted successfully, false if not

Remarks

Before calling this method, call [IBomTableAnnotation::GetBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetBomTableSortData.md) to populate SortData.

See [Sorting Tables](sldworksapiprogguide.chm::/OVERVIEW/Sorting_Tables.htm) for more information.

Example

[Sort Table (C#)](Sort_Table_Example_CSharp.htm)  
[Sort Table (VB.NET)](Sort_Table_Example_VBNET.htm)  
[Sort Table (VBA)](Sort_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::ApplySavedSortScheme Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~ApplySavedSortScheme.md)
