# DDrawingDocEvents_LoadFromStorageStoreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_LoadFromStorageStoreNotifyEventHandler`

Fired when it is safe to load data from third-party IStorage storage.
Fired when it is safe to load data from third-party IStorage storage.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_LoadFromStorageStoreNotifyEventHandler() As System.Integer
```

```

Dim instance As New DDrawingDocEvents_LoadFromStorageStoreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_LoadFromStorageStoreNotifyEventHandler()
```

```

public delegate System.int DDrawingDocEvents_LoadFromStorageStoreNotifyEventHandler();
```

Remarks

Call [IModelDocExtension::IGet3rdPartyStorageStore](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGet3rdPartyStorageStore.md) after receiving this notification. This notification is sent even when the third-party storage node is empty.

If developing a C++ application, use [swDrawingLoadFromStorageStoreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_LoadFromStorageStoreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_LoadFromStorageStoreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
