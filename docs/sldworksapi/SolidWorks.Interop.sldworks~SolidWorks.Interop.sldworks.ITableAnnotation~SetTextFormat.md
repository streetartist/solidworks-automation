# SetTextFormat Method (ITableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetTextFormat`

Sets the text format for this table.
Sets the text format for this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTextFormat( _
   ByVal UseDoc As System.Boolean, _
   ByVal TextFormat As TextFormat _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim UseDoc As System.Boolean
Dim TextFormat As TextFormat
Dim value As System.Boolean
 
value = instance.SetTextFormat(UseDoc, TextFormat)
```

```

System.bool SetTextFormat( 
   System.bool UseDoc,
   TextFormat TextFormat
)
```

```

System.bool SetTextFormat( 
   System.bool UseDoc,
   TextFormat^ TextFormat
) 
```

#### Parameters

*UseDoc*
:   True to use the document setting, false to not

*TextFormat*
:   [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) object

#### Return Value

True if the text format is set successfully, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetTextFormat.md)  
[ITableAnnotation::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetUseDocTextFormat.md)  
[ITableAnnotation::Text Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text.md)  
[ITableAnnotation::TextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TextHorizontalJustification.md)  
[ITableAnnotation::TextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TextVerticalJustification.md)
