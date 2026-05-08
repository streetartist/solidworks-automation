# DSldWorksEvents_DestroyNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DestroyNotifyEventHandler`

Sent to an MFC-based or a COM-based DLL add-in when SOLIDWORKS is about to be destroyed.
Sent to an MFC-based or a COM-based DLL add-in when SOLIDWORKS is about to be destroyed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_DestroyNotifyEventHandler() As System.Integer
```

```

Dim instance As New DSldWorksEvents_DestroyNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_DestroyNotifyEventHandler()
```

```

public delegate System.int DSldWorksEvents_DestroyNotifyEventHandler();
```

Remarks

This is a pre-notification. Add-ins should not perform any cleanup inside this event.

Use [ISwAddin::DisconnectFromSw](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~DisconnectFromSW.md) to perform any cleanup of COM-based DLL add-ins.

If developing a C++ application, use [swAppDestroyNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_DestroyNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DestroyNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
