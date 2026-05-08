# LoadLineStyles Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~LoadLineStyles`

Loads the specified line styles into the current drawing.
Loads the specified line styles into the current drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LoadLineStyles( _
   ByVal StyleFiles As System.String, _
   ByVal StyleNameList As System.Object, _
   ByVal ReplaceExisting As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim StyleFiles As System.String
Dim StyleNameList As System.Object
Dim ReplaceExisting As System.Boolean
Dim value As System.Boolean
 
value = instance.LoadLineStyles(StyleFiles, StyleNameList, ReplaceExisting)
```

```

System.bool LoadLineStyles( 
   System.string StyleFiles,
   System.object StyleNameList,
   System.bool ReplaceExisting
)
```

```

System.bool LoadLineStyles( 
   System.String^ StyleFiles,
   System.Object^ StyleNameList,
   System.bool ReplaceExisting
) 
```

#### Parameters

*StyleFiles*
:   Full pathname of file containing line styles to import

*StyleNameList*
:   Array of strings containing style names

*ReplaceExisting*
:   True to replace existing styles, false to not

#### Return Value

True if successful, false if not

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
[IDrawingDoc::AddLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddLineStyle.md)  
[IDrawingDoc::DeleteLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DeleteLineStyle.md)  
[IDrawingDoc::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineStyles.md)  
[IDrawingDoc::SaveLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SaveLineStyles.md)  
[ISldWorks::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLineStyles.md)
