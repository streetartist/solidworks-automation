# BehindSheet Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~BehindSheet`

Places this note, located on the sheet format in a drawing, behind the drawing sheet.
Places this note, located on the sheet format in a drawing, behind the drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BehindSheet As System.Boolean
```

```

Dim instance As INote
Dim value As System.Boolean
 
instance.BehindSheet = value
 
value = instance.BehindSheet
```

```

System.bool BehindSheet {get; set;}
```

```

property System.bool BehindSheet {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to place this note, located on the sheet format in a drawing, behind the drawing sheet; false to not

Remarks

This property places a note on the sheet format behind a drawing sheet, which allows you to display the note as watermark in a drawing. Before calling this property, you must call [IDrawingDoc::EditTemplate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditTemplate.md) and [IDrawingDoc::EditSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.md).

Use these properties to modify watermarks in parts and assemblies:

- [INote::WatermarkNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkNote.md)
- [INote::WatermarkBehindGeometry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkBehindGeometry.md)
- [INote::WatermarkTransparencyLevel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkTransparencyLevel.md)

Example

[Place Note Behind Drawing Sheet (C#)](Place_Note_Behind_Drawing_Sheet_Example_CSharp.htm)  
[Place Note Behind Drawing Sheet (VB.NET)](Place_Note_Behind_Drawing_Sheet_Example_VBNET.htm)  
[Place Note Behind Drawing Sheet (VBA)](Place_Note_Behind_Drawing_Sheet_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)
