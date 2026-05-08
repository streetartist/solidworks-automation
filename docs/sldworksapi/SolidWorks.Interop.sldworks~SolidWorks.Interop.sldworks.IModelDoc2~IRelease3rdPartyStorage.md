# IRelease3rdPartyStorage Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IRelease3rdPartyStorage`

Releases the specified third-party stream.
Releases the specified third-party stream.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IRelease3rdPartyStorage( _
   ByVal StringIn As System.String _
) 
```

```

Dim instance As IModelDoc2
Dim StringIn As System.String
 
instance.IRelease3rdPartyStorage(StringIn)
```

```

void IRelease3rdPartyStorage( 
   System.string StringIn
)
```

```

void IRelease3rdPartyStorage( 
   System.String^ StringIn
) 
```

#### Parameters

*StringIn*
:   Name of the stream to release

Remarks

You can use this method with [IModelDoc2::IGet3rdPartyStorage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.md). You must use it if you are not using the LoadFromStorageNotify event. You must call this method when the call to IModelDoc2::IGet3rdPartyStorage returns a NULL stream.

NOTE: If you are using serialization, then be careful with the standard MFC macros; otherwise, you can get messages like Unexpected File Format after your application is unloaded. One way of using IMPLEMENT\_SERIAL is:

IMPLEMENT\_SERIAL( CCustomAttr, CObject, VERSIONABLE\_SCHEMA|0 )

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[DAssemblyDocEvents\_LoadFromStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LoadFromStorageNotifyEventHandler.md)  
[DAssemblyDocEvents\_SaveToStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SaveToStorageNotifyEventHandler.md)  
[DDrawingDocEvents\_LoadFromStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_LoadFromStorageNotifyEventHandler.md)  
[DDrawingDocEvents\_SaveToStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_SaveToStorageNotifyEventHandler.md)  
[DPartDocEvents\_LoadFromStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_LoadFromStorageNotifyEventHandler.md)  
[DPartDocEvents\_SaveToStorageNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SaveToStorageNotifyEventHandler.md)
