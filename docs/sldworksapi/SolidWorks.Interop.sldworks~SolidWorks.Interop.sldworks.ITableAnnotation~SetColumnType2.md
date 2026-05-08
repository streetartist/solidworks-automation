# SetColumnType2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType2`

Obsolete. Superseded by ITableAnnotation::SetColumnType3.
Obsolete. Superseded by [ITableAnnotation::SetColumnType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetColumnType2( _
   ByVal Index As System.Integer, _
   ByVal Type As System.Integer, _
   ByVal IncludeHidden As System.Boolean _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim Type As System.Integer
Dim IncludeHidden As System.Boolean
Dim value As System.Boolean
 
value = instance.SetColumnType2(Index, Type, IncludeHidden)
```

```

System.bool SetColumnType2( 
   System.int Index,
   System.int Type,
   System.bool IncludeHidden
)
```

```

System.bool SetColumnType2( 
   System.int Index,
   System.int Type,
   System.bool IncludeHidden
) 
```

#### Parameters

*Index*
:   Index of the column whose type to set

*Type*
:   Column type as defined by [swTableColumnTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableColumnTypes_e.html)

*IncludeHidden*
:   True to set the hidden column type, false to not

#### Return Value

True if column type is set, false if not

Remarks

The index for both rows and columns is 0-based.

When you set a column type, the title is automatically changed to match that column type. If you change the column type to be a custom property column, then the column title is empty and you must set the column title using [ITableAnnotation::SetColumnTitle2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle2.md).

A BOM table column cannot be changed to a Quantity type column in the SOLIDWORKS user interface. This method is consistent with the user interface.

Example

[Insert Column in BOM Table (VBA)](Insert_Column_in_BOM_Table_Example_VB.htm)  
[Insert Column in BOM Table (VB.NET)](Insert_Column_in_BOM_Table_Example_VBNET.htm)  
[Insert Column in BOM Table (C#)](Insert_Column_in_BOM_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetColumnType2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType2.md)
