# SetColumnTitle2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle2`

Sets the title of the specified column.
Sets the title of the specified column.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetColumnTitle2( _
   ByVal Index As System.Integer, _
   ByVal Title As System.String, _
   ByVal IncludeHidden As System.Boolean _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim Title As System.String
Dim IncludeHidden As System.Boolean
Dim value As System.Boolean
 
value = instance.SetColumnTitle2(Index, Title, IncludeHidden)
```

```

System.bool SetColumnTitle2( 
   System.int Index,
   System.string Title,
   System.bool IncludeHidden
)
```

```

System.bool SetColumnTitle2( 
   System.int Index,
   System.String^ Title,
   System.bool IncludeHidden
) 
```

#### Parameters

*Index*
:   Index of the column whose title to set

*Title*
:   Column title

*IncludeHidden*
:   True to set the hidden column title, false to not

#### Return Value

True if title is set, false if not

Remarks

The index for both rows and columns is 0-based.

False is returned if the table does not have a header enabled. The title cannot be set to empty text.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetColumnTitle2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle2.md)  
[ITableAnnotation::SetColumnType2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType2.md)
