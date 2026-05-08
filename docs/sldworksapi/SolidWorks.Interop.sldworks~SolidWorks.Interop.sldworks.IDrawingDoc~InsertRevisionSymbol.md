# InsertRevisionSymbol Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionSymbol`

Inserts a revision symbol note in this drawing.
Inserts a revision symbol note in this drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertRevisionSymbol( _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
) As Note
```

```

Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim value As Note
 
value = instance.InsertRevisionSymbol(X, Y)
```

```

Note InsertRevisionSymbol( 
   System.double X,
   System.double Y
)
```

```

Note^ InsertRevisionSymbol( 
   System.double X,
   System.double Y
) 
```

#### Parameters

*X*
:   X coordinate  at which to insert revision symbol note

*Y*
:   Y coordinate at which to insert revision symbol note

#### Return Value

Pointer to the newly created [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) object

Remarks

To attach the revision symbol to entities in the drawing, the end-user must interactively preselect those entities. The revision symbol is then inserted with leaders to those selected entities. If there are no preselected entities, the symbol is free-standing.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::CreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateCompoundNote.md)  
[IDrawingDoc::CreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText2.md)  
[IDrawingDoc::ICreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateCompoundNote.md)  
[IDrawingDoc::ICreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateText2.md)  
[IDrawingDoc::InsertNewNote2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote2.md)
