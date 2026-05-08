# DModelViewEvents_DisplayModeChangePreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_DisplayModeChangePreNotifyEventHandler`

Pre-notifies the user program when a model view display mode is about to be changed.
Pre-notifies the user program when a model view display mode is about to be changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_DisplayModeChangePreNotifyEventHandler() As System.Integer
```

```

Dim instance As New DModelViewEvents_DisplayModeChangePreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_DisplayModeChangePreNotifyEventHandler()
```

```

public delegate System.int DModelViewEvents_DisplayModeChangePreNotifyEventHandler();
```

Remarks

This event occurs when the display mode is about to be changed using [IModelDocExtension::DisplayMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayMode.md).

If developing a C++ application, use [swViewDisplayModeChangePreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

Example

Contact SOLIDWORKS API Support to obtain **Event Monitor for SOLIDWORKS 2012 (VBA)**.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_DisplayModeChangePreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_DisplayModeChangePreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
