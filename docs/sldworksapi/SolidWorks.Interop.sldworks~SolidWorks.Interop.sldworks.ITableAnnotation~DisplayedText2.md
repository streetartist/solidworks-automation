# DisplayedText2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DisplayedText2`

Gets the actual text displayed in the specified cell in this table.
Gets the actual text displayed in the specified cell in this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property DisplayedText2( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean _
) As System.String
```

```

Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim value As System.String
 
value = instance.DisplayedText2(Row, Column, IncludeHidden)
```

```

System.string DisplayedText2( 
   System.int Row,
   System.int Column,
   System.bool IncludeHidden
) {get;}
```

```

property System.String^ DisplayedText2 {
   System.String^ get(System.int Row, System.int Column, System.bool IncludeHidden);
}
```

#### Parameters

*Row*
:   Index of the row

*Column*
:   Index of the column

*IncludeHidden*
:   True to get the text displayed in the hidden cell, false to not

#### Property Value

Actual text displayed in the specified cell

Remarks

Index for both rows and columns is 0-based.

To get the parameterized string that drives this displayed text, use [ITableAnnotation::Text2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text2.md).

Example

[Get Table Annotation and Contents (VBA)](Get_Table_Annotation_and_Contents_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)
