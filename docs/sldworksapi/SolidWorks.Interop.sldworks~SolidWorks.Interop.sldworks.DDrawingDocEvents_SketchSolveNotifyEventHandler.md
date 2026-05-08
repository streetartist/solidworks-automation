# DDrawingDocEvents_SketchSolveNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_SketchSolveNotifyEventHandler`

Fired whenever the sketch is solved; for example, when dragging a sketch entity, adding or editing relations, changing dimensions, and so on. This event returns the name of the sketch feature being updated.
Fired whenever the sketch is solved; for example, when dragging a sketch entity, adding or editing relations, changing dimensions, and so on. This event returns the name of the sketch feature being updated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_SketchSolveNotifyEventHandler( _
   ByVal featName As System.String _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_SketchSolveNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_SketchSolveNotifyEventHandler( 
   System.string featName
)
```

```

public delegate System.int DDrawingDocEvents_SketchSolveNotifyEventHandler( 
   System.String^ featName
)
```

#### Parameters

*featName*
:   Name of sketch feature being updated

Remarks

Pressing the Ctrl+Q keys rebuilds drawing sketches ([IView::GetSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketch.md) or [IView::IGetSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSketch.md)), which causes this event to fire.

If developing a C++ application, use [swDrawingSketchSolveNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_SketchSolveNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_SketchSolveNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
