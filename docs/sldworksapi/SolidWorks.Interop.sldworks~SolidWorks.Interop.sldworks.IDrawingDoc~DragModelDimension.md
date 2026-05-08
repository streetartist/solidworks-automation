# DragModelDimension Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DragModelDimension`

Copies or moves dimensions to a different drawing view.
Copies or moves dimensions to a different drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub DragModelDimension( _
   ByVal ViewName As System.String, _
   ByVal DropEffect As System.Short, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) 
```

```

Dim instance As IDrawingDoc
Dim ViewName As System.String
Dim DropEffect As System.Short
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
 
instance.DragModelDimension(ViewName, DropEffect, X, Y, Z)
```

```

void DragModelDimension( 
   System.string ViewName,
   System.short DropEffect,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

void DragModelDimension( 
   System.String^ ViewName,
   System.short DropEffect,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*ViewName*
:   Name of the drawing view to which you want to copy or move the selected model dimension

*DropEffect*
:   - Copy = 1
    - Move = 2

*X*
:   X location in sheet space for the newly copied or moved dimension

*Y*
:   Y location in sheet space for the newly copied or moved dimension

*Z*
:   Z location in sheet space for the newly copied or moved dimension; set to  0

#### Return Value

The ViewName argument cannot be the current view for the dimension.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::Dimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Dimensions.md)
