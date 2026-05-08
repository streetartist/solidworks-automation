# DSldWorksEvents_FileOpenPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenPostNotifyEventHandler`

Post-notifies the user program when a file has been opened.
Post-notifies the user program when a file has been opened.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_FileOpenPostNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_FileOpenPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_FileOpenPostNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DSldWorksEvents_FileOpenPostNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Name of the opened file

Remarks

This is the last event fired before control returns to the user. This event indicates that methods that modify references, [reload documents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ReloadOrReplace.md), or close documents can be called.

If developing a C++ application, use [swAppFileOpenPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_FileOpenPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
