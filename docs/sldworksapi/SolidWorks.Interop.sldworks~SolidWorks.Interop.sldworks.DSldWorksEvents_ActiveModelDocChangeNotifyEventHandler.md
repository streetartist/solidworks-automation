# DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler`

Post-notifies the user program when the active IModelDoc2 object has changed.
Post-notifies the user program when the active [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) object has changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler() As System.Integer
```

```

Dim instance As New DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler()
```

```

public delegate System.int DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler();
```

Remarks

The active [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) object represents the document that is currently being edited by the end-user. This notification is not sent when a part or subassembly is being edited in the context of an assembly. On receiving this event, you can call [ISldWorks::ActiveDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md) or [ISldWorks:IActiveDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.md) to get the actual IModelDoc2 pointer.

This event is only sent when the active window in the SOLIDWORKS session actually changes to a new active model document. Window changes are not guaranteed during, for example, the shutdown of the SOLIDWORKS application. For example, if the SOLIDWORKS application closes a non-active document, there is no need to activate a new document window.

If developing a C++ application, use [swAppModelDocChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_ActiveModelDocChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
