# GetColumnType2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType2`

Obsolete. Superseded by ITableAnnotation::GetColumnType3.
Obsolete. Superseded by [ITableAnnotation::GetColumnType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetColumnType2( _
   ByVal Index As System.Integer, _
   ByVal IncludeHidden As System.Boolean _
) As System.Integer
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim IncludeHidden As System.Boolean
Dim value As System.Integer
 
value = instance.GetColumnType2(Index, IncludeHidden)
```

```

System.int GetColumnType2( 
   System.int Index,
   System.bool IncludeHidden
)
```

```

System.int GetColumnType2( 
   System.int Index,
   System.bool IncludeHidden
) 
```

#### Parameters

*Index*
:   0-based index indicating the column whose type to get

*IncludeHidden*
:   True to get the type of the hidden column, false to not

#### Return Value

Type of column as defined by [swTableColumnTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableColumnTypes_e.html)

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
[ITableAnnotation::SetColumnType2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType2.md)
