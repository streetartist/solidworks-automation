# GetLineStyles Method (IDrawingDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineStyles`

Gets all of the line styles used in the current document.
Gets all of the line styles used in the current document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLineStyles( _
   ByRef StyleNameList As System.Object, _
   ByRef StyleList As System.Object _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim StyleNameList As System.Object
Dim StyleList As System.Object
Dim value As System.Boolean
 
value = instance.GetLineStyles(StyleNameList, StyleList)
```

```

System.bool GetLineStyles( 
   out System.object StyleNameList,
   out System.object StyleList
)
```

```

System.bool GetLineStyles( 
   [Out] System.Object^ StyleNameList,
   [Out] System.Object^ StyleList
) 
```

#### Parameters

*StyleNameList*
:   Array of strings containing style names

*StyleList*
:   Array of strings containing style types

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
[IDrawingDoc::LoadLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~LoadLineStyles.md)  
[IDrawingDoc::SaveLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SaveLineStyles.md)  
[ISldWorks::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLineStyles.md)
