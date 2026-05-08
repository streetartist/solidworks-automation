# GetColumnTitle2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle2`

Gets the title of the specified column.
Gets the title of the specified column.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetColumnTitle2( _
   ByVal Index As System.Integer, _
   ByVal IncludeHidden As System.Boolean _
) As System.String
```

```

Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim IncludeHidden As System.Boolean
Dim value As System.String
 
value = instance.GetColumnTitle2(Index, IncludeHidden)
```

```

System.string GetColumnTitle2( 
   System.int Index,
   System.bool IncludeHidden
)
```

```

System.String^ GetColumnTitle2( 
   System.int Index,
   System.bool IncludeHidden
) 
```

#### Parameters

*Index*
:   0-based index indicating the column

*IncludeHidden*
:   True to get the title of the hidden column, false to not

#### Return Value

Column title

Example

[Export BOMs to XML (VBA)](Export_BOMs_to_XML_Example_VB.htm)  
[Export BOMs to XML (VB.NET)](Export_BOMs_to_XML_Example_VBNET.htm)  
[Export BOMs to XML (C#)](Export_BOMs_to_XML_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::SetColumnTitle2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle2.md)
