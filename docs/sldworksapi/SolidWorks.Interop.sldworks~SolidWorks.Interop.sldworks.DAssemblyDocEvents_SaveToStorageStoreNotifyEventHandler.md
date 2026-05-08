# DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler`

Fired when it is safe to save data to third-party IStorage storage.
Fired when it is safe to save data to third-party IStorage storage.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler() As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler()
```

```

public delegate System.int DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAssemblySaveToStorageStoreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Call [IModelDocExtension::IGet3rdPartyStorageStore](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGet3rdPartyStorageStore.md) after receiving this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_SaveToStorageStoreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
