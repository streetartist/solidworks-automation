# ColumnIndex Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~ColumnIndex`

Gets and sets the column index for the specified sort order index.
Gets and sets the column index for the specified sort order index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ColumnIndex( _
   ByVal SortOrderIndex As System.Integer _
) As System.Integer
```

```

Dim instance As IBomTableSortData
Dim SortOrderIndex As System.Integer
Dim value As System.Integer
 
instance.ColumnIndex(SortOrderIndex) = value
 
value = instance.ColumnIndex(SortOrderIndex)
```

```

System.int ColumnIndex( 
   System.int SortOrderIndex
) {get; set;}
```

```

property System.int ColumnIndex {
   System.int get(System.int SortOrderIndex);
   void set (System.int SortOrderIndex, System.int value);
}
```

#### Parameters

*SortOrderIndex*
:   0 for primary sort, 1 for secondary sort, 2 for tertiary sort (see **Remarks**)

#### Property Value

0-based column index mapped to the specified SortOrderIndex; specify -1 if the specified SortOrderIndex is not used

Remarks

BOM tables may be sorted by up to three columns. This property maps one column to a sort order index. Call this property three times to set the sort order indexes of all three columns.

Example

See the [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md)  
[IBomTableSortData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.md)
