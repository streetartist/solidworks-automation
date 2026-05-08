# DAssemblyDocEvents_SketchSolveNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SketchSolveNotifyEventHandler`

Fired whenever the sketch is solved; for example, when dragging a sketch entity, adding or editing relations, changing dimensions, and so on.
Fired whenever the sketch is solved; for example, when dragging a sketch entity, adding or editing relations, changing dimensions, and so on.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_SketchSolveNotifyEventHandler( _
   ByVal featName As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_SketchSolveNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_SketchSolveNotifyEventHandler( 
   System.string featName
)
```

```

public delegate System.int DAssemblyDocEvents_SketchSolveNotifyEventHandler( 
   System.String^ featName
)
```

#### Parameters

*featName*
:   Name of the sketch feature being updated

Remarks

If developing a C++ application, use [swAssemblySketchSolveNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

This event returns the name of the sketch feature being updated.

Pressing the Ctrl+Q keys in an assembly-level sketch does not always result in a sketch being solved. A sketch is only solved if it needs to be updated. If the sketch is not solved, then this event is not fired.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_SketchSolveNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SketchSolveNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
