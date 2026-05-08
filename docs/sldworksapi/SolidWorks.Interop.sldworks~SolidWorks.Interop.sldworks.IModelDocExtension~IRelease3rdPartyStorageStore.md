# IRelease3rdPartyStorageStore Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IRelease3rdPartyStorageStore`

Releases the specified third-party storage in this document.
Releases the specified third-party storage in this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IRelease3rdPartyStorageStore( _
   ByVal SubStorageName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim SubStorageName As System.String
Dim value As System.Boolean
 
value = instance.IRelease3rdPartyStorageStore(SubStorageName)
```

```

System.bool IRelease3rdPartyStorageStore( 
   System.string SubStorageName
)
```

```

System.bool IRelease3rdPartyStorageStore( 
   System.String^ SubStorageName
) 
```

#### Parameters

*SubStorageName*
:   Name of the third-party storage

#### Return Value

True if the data is released, false if not

Remarks

You can use this method with [IModelDocExtension::IGet3rdPartyStorageStore](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGet3rdPartyStorageStore.md). You must use it if you are not using the LoadFromStorageStoreNotify event. You must call this method when the call to IModelDocExtension::IGet3rdPartyStorageStore returns a NULL stream.

NOTE: If you are using serialization, then be careful with the standard MFC macros; otherwise, you can get messages like "Unexpected File Format" after your application is unloaded. One way of using IMPLEMENT\_SERIAL is:

IMPLEMENT\_SERIAL( CCustomAttr, CObject, VERSIONABLE\_SCHEMA|0 )

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[DAssemblyDocEvents LoadFromStorageNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LoadFromStorageNotifyEventHandler.md)  
[DDrawingDocEvents LoadFromStorageNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_LoadFromStorageNotifyEventHandler.md)  
[DPartDocEvents LoadFromStorageNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_LoadFromStorageNotifyEventHandler.md)
