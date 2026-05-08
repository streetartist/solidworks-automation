# DropDrawingViewFromPalette Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DropDrawingViewFromPalette`

Obsolete. Superseded by IDrawingDoc::DropDrawingViewFromPalette2.
Obsolete. Superseded by [IDrawingDoc::DropDrawingViewFromPalette2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DropDrawingViewFromPalette2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DropDrawingViewFromPalette( _
   ByVal Layout As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As View
```

```

Dim instance As IDrawingDoc
Dim Layout As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As View
 
value = instance.DropDrawingViewFromPalette(Layout, X, Y, Z)
```

```

View DropDrawingViewFromPalette( 
   System.int Layout,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

View^ DropDrawingViewFromPalette( 
   System.int Layout,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*Layout*
:   ID of the drawing view to move to the drawing sheet

*X*
:   x coordinate where to drop the drawing view

*Y*
:   y coordinate where to drop the drawing view

*Z*
:   z coordinate where to drop the drawing view; this coordinate is always 0

#### Return Value

Pointer to the [IView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
