# IGetSketch Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSketch`

Gets the sketch used by this view.
Gets the sketch used by this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketch() As Sketch
```

```

Dim instance As IView
Dim value As Sketch
 
value = instance.IGetSketch()
```

```

Sketch IGetSketch()
```

```

Sketch^ IGetSketch(); 
```

#### Return Value

[Sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)

Remarks

Each drawing view contains an underlying sketch. The user can activate the sketch for a drawing view by double-clicking the view. Once the drawing view is active, you can add sketch directly to the view's sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketch.md)
