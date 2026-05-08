# HiddenViewsVisible Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HiddenViewsVisible`

Shows or hides all of the hidden drawing views.
Shows or hides all of the hidden drawing views.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HiddenViewsVisible As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim value As System.Boolean
 
instance.HiddenViewsVisible = value
 
value = instance.HiddenViewsVisible
```

```

System.bool HiddenViewsVisible {get; set;}
```

```

property System.bool HiddenViewsVisible {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if views are visible, false if they are hidden

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::HideShowDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideShowDimensions.md)  
[IDrawingDoc::SuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SuppressView.md)  
[IDrawingDoc::UnsuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~UnsuppressView.md)
