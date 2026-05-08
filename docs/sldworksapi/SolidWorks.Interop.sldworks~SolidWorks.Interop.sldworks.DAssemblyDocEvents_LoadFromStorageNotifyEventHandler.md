# DAssemblyDocEvents_LoadFromStorageNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LoadFromStorageNotifyEventHandler`

Fired when it is safe to load data from third-party IStream storage.
Fired when it is safe to load data from third-party IStream storage.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_LoadFromStorageNotifyEventHandler() As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_LoadFromStorageNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_LoadFromStorageNotifyEventHandler()
```

```

public delegate System.int DAssemblyDocEvents_LoadFromStorageNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAssemblyLoadFromStorageNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Call [IModelDoc2::IGet3rdPartyStorage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.md) after receiving this notification. This notification is sent even when the third-party storage node is empty.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_LoadFromStorageNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LoadFromStorageNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
