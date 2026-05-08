# Ascending Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~Ascending`

Gets and sets whether this is an ascending sort for the specified sort order index.
Gets and sets whether this is an ascending sort for the specified sort order index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Ascending( _
   ByVal SortOrderIndex As System.Integer _
) As System.Boolean
```

```

Dim instance As IBomTableSortData
Dim SortOrderIndex As System.Integer
Dim value As System.Boolean
 
instance.Ascending(SortOrderIndex) = value
 
value = instance.Ascending(SortOrderIndex)
```

```

System.bool Ascending( 
   System.int SortOrderIndex
) {get; set;}
```

```

property System.bool Ascending {
   System.bool get(System.int SortOrderIndex);
   void set (System.int SortOrderIndex, System.bool value);
}
```

#### Parameters

*SortOrderIndex*
:   0 for primary sort, 1 for secondary sort, 2 for tertiary sort (see **Remarks**)

#### Property Value

True if sort is ascending, false if descending

Remarks

BOM tables may be sorted by up to three columns. This property maps the sort order index with a sorting direction (ascending or descending). Call this property three times to set the sorting directions of all three sort order indexes.

Example

See the [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md)  
[IBomTableSortData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.md)
