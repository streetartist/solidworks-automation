# GetLineStyles Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLineStyles`

Gets all of the line styles in the specified file.
Gets all of the line styles in the specified file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLineStyles( _
   ByVal StyleFile As System.String, _
   ByRef StyleNameList As System.Object, _
   ByRef StyleList As System.Object _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim StyleFile As System.String
Dim StyleNameList As System.Object
Dim StyleList As System.Object
Dim value As System.Boolean
 
value = instance.GetLineStyles(StyleFile, StyleNameList, StyleList)
```

```

System.bool GetLineStyles( 
   System.string StyleFile,
   out System.object StyleNameList,
   out System.object StyleList
)
```

```

System.bool GetLineStyles( 
   System.String^ StyleFile,
   [Out] System.Object^ StyleNameList,
   [Out] System.Object^ StyleList
) 
```

#### Parameters

*StyleFile*
:   Full pathname of the file containing line styles to get

*StyleNameList*
:   Array of strings containing line style names

*StyleList*
:   Array of strings containing line style types

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

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[IDrawingDoc::AddLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddLineStyle.md)  
[IDrawingDoc::DeleteLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DeleteLineStyle.md)  
[IDrawingDoc::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineStyles.md)  
[IDrawingDoc::LoadLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~LoadLineStyles.md)  
[IDrawingDoc::SaveLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SaveLineStyles.md)
