# HideShowDrawingViews Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideShowDrawingViews`

Sets whether to hide or show hidden drawing views.
Sets whether to hide or show hidden drawing views.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub HideShowDrawingViews() 
```

```

Dim instance As IDrawingDoc
 
instance.HideShowDrawingViews()
```

```

void HideShowDrawingViews()
```

```

void HideShowDrawingViews(); 
```

Remarks

If this setting is enabled, then SOLIDWORKS shows drawing views that were hidden using [IDrawingDoc::SuppressView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SuppressView.md) with an **X**.

Example

[Display Hidden Lines in Drawing (VBA)](Display_Hidden_Lines_in_Drawing_Example_VB.htm)  
[Display Hidden Lines in Drawing (VB.NET)](Display_Hidden_Lines_in_Drawing_Example_VBNET.htm)  
[Display Hidden Lines in Drawing (C#)](Display_Hidden_Lines_in_Drawing_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView.md)  
[IDrawingDoc::SuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SuppressView.md)  
[IDrawingDoc::UnsuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~UnsuppressView.md)  
[IDrawingDoc::ViewDisplayHidden Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewDisplayHidden.md)  
[IDrawingDoc::ViewDisplayHiddengreyed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewDisplayHiddengreyed.md)  
[IDrawingDoc::ViewDisplayShaded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewDisplayShaded.md)  
[IDrawingDoc::ViewDisplayWireframe Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewDisplayWireframe.md)  
[IDrawingDoc::ViewFullPage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewFullPage.md)  
[IDrawingDoc::ViewHlrQuality Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewHlrQuality.md)  
[IDrawingDoc::ActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.md)  
[IDrawingDoc::AutomaticViewUpdate Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutomaticViewUpdate.md)  
[IDrawingDoc::HiddenViewsVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HiddenViewsVisible.md)  
[IDrawingDoc::IActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IActiveDrawingView.md)
