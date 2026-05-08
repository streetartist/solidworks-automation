# AddLineStyle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddLineStyle`

Adds a line style to the current drawing.
Adds a line style to the current drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddLineStyle( _
   ByVal StyleName As System.String, _
   ByVal StyleDefinition As System.String _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim StyleName As System.String
Dim StyleDefinition As System.String
Dim value As System.Boolean
 
value = instance.AddLineStyle(StyleName, StyleDefinition)
```

```

System.bool AddLineStyle( 
   System.string StyleName,
   System.string StyleDefinition
)
```

```

System.bool AddLineStyle( 
   System.String^ StyleName,
   System.String^ StyleDefinition
) 
```

#### Parameters

*StyleName*
:   Name of line style

*StyleDefinition*
:   Comma-delimited string of line lengths and spacing values for the line style

#### Return Value

True if successful, false if not

Remarks

Read about line style options in SOLIDWORKS Help.

Example

[Manage Drawing Document Line Styles (C#)](Manage_Drawing_Document_Line_Styles_Example_CSharp.htm)  
[Manage Drawing Document Line Styles (VB.NET)](Manage_Drawing_Document_Line_Styles_Example_VBNET.htm)  
[Manage Drawing Document Line Styles (VBA)](Manage_Drawing_Document_Line_Styles_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::DeleteLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DeleteLineStyle.md)  
[IDrawingDoc::LoadLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~LoadLineStyles.md)  
[IDrawingDoc::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineStyles.md)  
[IDrawingDoc::SaveLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SaveLineStyles.md)  
[ISldWorks::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLineStyles.md)
