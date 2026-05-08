# GetVisibleBox Method (IModelView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetVisibleBox`

Gets the boundaries of the visible model view window.
Gets the boundaries of the visible model view window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVisibleBox() As System.Object
```

```

Dim instance As IModelView
Dim value As System.Object
 
value = instance.GetVisibleBox()
```

```

System.object GetVisibleBox()
```

```

System.Object^ GetVisibleBox(); 
```

#### Return Value

Array of four longs (win\_x\_min, win-y\_min, win\_x\_max, and win\_y\_max) in screen pixels indicating the boundaries of the visible model view window; any part of the model view window blocked by the  FeatureManager design tree is excluded

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::IGetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetVisibleBox.md)
