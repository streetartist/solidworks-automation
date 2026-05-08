# DAssemblyDocEvents_CloseDesignTableNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_CloseDesignTableNotifyEventHandler`

Pre-notifies your application that a design table that was being edited is about to be closed.
Pre-notifies your application that a design table that was being edited is about to be closed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_CloseDesignTableNotifyEventHandler( _
   ByVal DesignTable As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_CloseDesignTableNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_CloseDesignTableNotifyEventHandler( 
   System.object DesignTable
)
```

```

public delegate System.int DAssemblyDocEvents_CloseDesignTableNotifyEventHandler( 
   System.Object^ DesignTable
)
```

#### Parameters

*DesignTable*
:   [Design table](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)

Remarks

The IAssemblyDoc event [OpenDesignTableNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_OpenDesignTableNotifyEventHandler.md) post-notifies your application that a design table has just been opened for editing.

If developing a C++ application, use [swAssemblyCloseDesignTableNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_CloseDesignTableNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_CloseDesignTableNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
