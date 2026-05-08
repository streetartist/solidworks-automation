# DAssemblyDocEvents_OpenDesignTableNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_OpenDesignTableNotifyEventHandler`

Post-notifies your application that a design table has been opened for editing.
Post-notifies your application that a design table has been opened for editing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_OpenDesignTableNotifyEventHandler( _
   ByVal DesignTable As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_OpenDesignTableNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_OpenDesignTableNotifyEventHandler( 
   System.object DesignTable
)
```

```

public delegate System.int DAssemblyDocEvents_OpenDesignTableNotifyEventHandler( 
   System.Object^ DesignTable
)
```

#### Parameters

*DesignTable*
:   [Design table](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)

Remarks

The IAssemblyDoc event [CloseDesignTableNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_CloseDesignTableNotifyEventHandler.md) pre-notifies your application that a design table that was being edited is about to be closed.

If developing a C++ application, use [swAssemblyOpenDesignTableNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_OpenDesignTableNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_OpenDesignTableNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
