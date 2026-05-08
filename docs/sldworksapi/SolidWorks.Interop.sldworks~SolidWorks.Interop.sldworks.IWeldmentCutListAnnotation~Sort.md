# Sort Method (IWeldmentCutListAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~Sort`

Sorts this weldment cut list by the specified column in the specified sorting direction.
Sorts this weldment cut list by the specified column in the specified sorting direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Sort( _
   ByVal ColumnIndex As System.Integer, _
   ByVal SortAscending As System.Boolean _
) As System.Boolean
```

```

Dim instance As IWeldmentCutListAnnotation
Dim ColumnIndex As System.Integer
Dim SortAscending As System.Boolean
Dim value As System.Boolean
 
value = instance.Sort(ColumnIndex, SortAscending)
```

```

System.bool Sort( 
   System.int ColumnIndex,
   System.bool SortAscending
)
```

```

System.bool Sort( 
   System.int ColumnIndex,
   System.bool SortAscending
) 
```

#### Parameters

*ColumnIndex*
:   0-based index of column to sort by (see **Remarks**)

*SortAscending*
:   True to sort ascending, false to sort descending

#### Return Value

True if sorted successfully, false if not

Remarks

Weldment cut lists must be sorted by any column except Item Number.

See [Sorting Tables](sldworksapiprogguide.chm::/OVERVIEW/Sorting_Tables.htm) for more information.

Example

[Sort Table (VBA)](Sort_Table_Example_VB.htm)  
[Sort Table (VB.NET)](Sort_Table_Example_VBNET.htm)  
[Sort Table (C#)](Sort_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.md)  
[IWeldmentCutListAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation_members.md)
