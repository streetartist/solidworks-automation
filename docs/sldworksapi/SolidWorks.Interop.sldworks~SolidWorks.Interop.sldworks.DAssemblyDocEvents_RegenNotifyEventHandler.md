# DAssemblyDocEvents_RegenNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenNotifyEventHandler`

Pre-notifies the user program when an assembly document is about to be rebuilt.
Pre-notifies the user program when an assembly document is about to be rebuilt.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_RegenNotifyEventHandler() As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_RegenNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_RegenNotifyEventHandler()
```

```

public delegate System.int DAssemblyDocEvents_RegenNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAssemblyRegenNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Use [DAssemblyDocEvents RegenPostNotify2EventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenPostNotify2EventHandler.md) to fire an event after the assembly is rebuilt.

You can also use [IModelDoc2::GetUpdateStamp](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUpdateStamp.md) to determine when changes take place in this document.

Example

[Fire Assembly Rebuild Events (C#)](Regen_Post_Notify2_Event_Handler_Example_CSharp.htm)  
[Fire Assembly Rebuild Events (VB.NET)](Regen_Post_Notify2_Event_Handler_Example_VBNET.htm)  
[Fire Assembly Rebuild Events (VBA)](Regen_Post_Notify2_Event_Handler_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_RegenNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
