# DPartDocEvents_NewSelectionNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_NewSelectionNotifyEventHandler`

Post-notifies the user program when the selection list has changed.
Post-notifies the user program when the selection list has changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_NewSelectionNotifyEventHandler() As System.Integer
```

```

Dim instance As New DPartDocEvents_NewSelectionNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_NewSelectionNotifyEventHandler()
```

```

public delegate System.int DPartDocEvents_NewSelectionNotifyEventHandler();
```

Remarks

This notification is generated when items are added, removed, or reordered in the selection list.

If developing a C++ application, use [swPartNewSelectionNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_NewSelectionNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_NewSelectionNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
