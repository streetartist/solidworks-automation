# DModelViewEvents_UserClearSelectionsNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_UserClearSelectionsNotifyEventHandler`

Fired when a user: Clicks the right-mouse button when the pointer is over a selection box on a PropertyManager page. Selects Clear Selections on the short-cut menu.
Fired when a user:

1. Clicks the right-mouse button when the pointer is over a selection box on a PropertyManager page.
2. Selects Clear Selections on the short-cut menu.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_UserClearSelectionsNotifyEventHandler() As System.Integer
```

```

Dim instance As New DModelViewEvents_UserClearSelectionsNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_UserClearSelectionsNotifyEventHandler()
```

```

public delegate System.int DModelViewEvents_UserClearSelectionsNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swViewUserClearSelectionsNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_UserClearSelectionsNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_UserClearSelectionsNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
