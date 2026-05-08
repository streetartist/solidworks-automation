# DDrawingDocEvents_DrawingStateChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DrawingStateChangeNotifyEventHandler`

Fired when a drawing's state changes.
Fired when a drawing's state changes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_DrawingStateChangeNotifyEventHandler( _
   ByVal PreviousState As System.Short, _
   ByVal newState As System.Short _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_DrawingStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_DrawingStateChangeNotifyEventHandler( 
   System.short PreviousState,
   System.short newState
)
```

```

public delegate System.int DDrawingDocEvents_DrawingStateChangeNotifyEventHandler( 
   System.short PreviousState,
   System.short newState
)
```

#### Parameters

*PreviousState*
:   Previous state as defined by [swDrawingMode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDrawingMode_e.html)

*newState*
:   New state as defined by swDrawingMode\_e

Remarks

If developing a C++ application, use [swDrawingDrawingStateChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_DrawingStateChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DrawingStateChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
