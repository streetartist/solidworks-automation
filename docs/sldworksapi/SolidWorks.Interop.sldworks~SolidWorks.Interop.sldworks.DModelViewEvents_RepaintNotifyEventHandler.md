# DModelViewEvents_RepaintNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_RepaintNotifyEventHandler`

Pre-notifies the user program when a view is about to be repainted and returns the paint type.
Pre-notifies the user program when a view is about to be repainted and returns the paint type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_RepaintNotifyEventHandler( _
   ByVal paintType As System.Integer _
) As System.Integer
```

```

Dim instance As New DModelViewEvents_RepaintNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_RepaintNotifyEventHandler( 
   System.int paintType
)
```

```

public delegate System.int DModelViewEvents_RepaintNotifyEventHandler( 
   System.int paintType
)
```

#### Parameters

*paintType*
:   Valid paint type as defined in [swRepaintTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRepaintTypes_e.html) (only the first two types are supported)

Remarks

Returns S\_false to stop from proceeding with the action that caused the notification. This also prevents sending the IModelView [BufferSwapNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_BufferSwapNotifyEventHandler.md) event.

If developing a C++ application, use [swViewBufferSwapNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_RepaintNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_RepaintNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
