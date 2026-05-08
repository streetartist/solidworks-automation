# DModelViewEvents_DisplayModeChangePostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_DisplayModeChangePostNotifyEventHandler`

Post-notifies the user program when a model view display mode is changed.
Post-notifies the user program when a model view display mode is changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_DisplayModeChangePostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DModelViewEvents_DisplayModeChangePostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_DisplayModeChangePostNotifyEventHandler()
```

```

public delegate System.int DModelViewEvents_DisplayModeChangePostNotifyEventHandler();
```

Remarks

This event occurs after the display mode has been changed using [IModelDocExtension::DisplayMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayMode.md).

If developing a C++ application, use [swViewDisplayModeChangePostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

Example

Contact SOLIDWORKS API Support to obtain **Event Monitor for SOLIDWORKS 2012 (VBA)**.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_DisplayModeChangePostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_DisplayModeChangePostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
