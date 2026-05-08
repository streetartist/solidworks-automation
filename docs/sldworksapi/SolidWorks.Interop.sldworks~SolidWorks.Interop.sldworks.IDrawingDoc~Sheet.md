# Sheet Property (IDrawingDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Sheet`

Gets the specified sheet.
Gets the specified sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Sheet( _
   ByVal Name As System.String _
) As Sheet
```

```

Dim instance As IDrawingDoc
Dim Name As System.String
Dim value As Sheet
 
value = instance.Sheet(Name)
```

```

Sheet Sheet( 
   System.string Name
) {get;}
```

```

property Sheet^ Sheet {
   Sheet^ get(System.String^ Name);
}
```

#### Parameters

*Name*
:   Name of sheet

#### Property Value

[Sheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)

Example

[Get Sheet in Multi-sheet Drawing (C#)](Get_Sheet_in_Multi-sheet_Drawing_Example_CSharp.htm)  
[Get Sheet in Multi-Sheet Drawing (VB.NET)](Get_Sheet_in_Multi-Sheet_Drawing_Example_VBNET.htm)  
[Get Sheet in Multi-sheet Drawing (VBA)](Get_Sheet_in_Multi-sheet_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
