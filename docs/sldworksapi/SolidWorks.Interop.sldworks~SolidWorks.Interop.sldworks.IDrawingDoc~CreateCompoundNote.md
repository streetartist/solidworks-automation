# CreateCompoundNote Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateCompoundNote`

Obsolete for documents created in SOLIDWORKS 2016 and later. Superseded by ISketchBlockDefinition and ISketchBlockInstance. Creates and returns a compound note.
Obsolete for documents created in SOLIDWORKS 2016 and later. Superseded by [ISketchBlockDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md) and [ISketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md). Creates and returns a compound note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCompoundNote( _
   ByVal Height As System.Double, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim Height As System.Double
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object
 
value = instance.CreateCompoundNote(Height, X, Y, Z)
```

```

System.object CreateCompoundNote( 
   System.double Height,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.Object^ CreateCompoundNote( 
   System.double Height,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*Height*
:   Note height in meters

*X*
:   x location of note in meters

*Y*
:   y location of note in meters

*Z*
:   z location of note in meters

#### Return Value

Newly created compound note

Remarks

A compound note is a note that can contain multiple text strings and sketch geometry.

Compound notes are equivalent to a user-defined symbol. After creating a compound note, you can use the other compound note methods to add text and sketch geometry to the object.

This object appears to the end-user as though it were one item. If the user selects the compound note and drags it, all of the entities and text move together.

Because a compound note can have multiple pieces of text, many of the compound note methods require that you specify the index value of the text. For example, the first piece of text added to the compound note using [INote::AddText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AddText.md) has index number 1, the second text added has index number 2, and so on.

SOLIDWORKS adds the note to the view of the current selection, so you must make a selection before you call this method.

Example

[Create Compound Note (VBA)](Create_Compound_Note_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ICreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateCompoundNote.md)  
[IDrawingDoc::InsertRevisionSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionSymbol.md)  
[IDrawingDoc::ICreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateText2.md)  
[IDrawingDoc::CreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText2.md)  
[IDrawingDoc::InsertNewNote2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote2.md)  
[IDrawingDoc::NewNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewNote.md)
