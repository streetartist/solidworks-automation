# DPartDocEvents_SaveToStorageStoreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SaveToStorageStoreNotifyEventHandler`

Fired when it is safe to save data to third-party IStorage storage.
Fired when it is safe to save data to third-party IStorage storage.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_SaveToStorageStoreNotifyEventHandler() As System.Integer
```

```

Dim instance As New DPartDocEvents_SaveToStorageStoreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_SaveToStorageStoreNotifyEventHandler()
```

```

public delegate System.int DPartDocEvents_SaveToStorageStoreNotifyEventHandler();
```

Remarks

Call [IModelDocExtension::IGet3rdPartyStorageStore](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGet3rdPartyStorageStore.md) after receiving this notification.

If developing a C++ application, use [swPartSaveToStorageStoreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_SaveToStorageStoreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SaveToStorageStoreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
