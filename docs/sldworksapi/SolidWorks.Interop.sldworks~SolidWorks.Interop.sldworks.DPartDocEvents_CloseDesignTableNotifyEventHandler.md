# DPartDocEvents_CloseDesignTableNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_CloseDesignTableNotifyEventHandler`

Pre-notifies your application that a design table that was opened for editing is about to be closed.
Pre-notifies your application that a design table that was opened for editing is about to be closed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_CloseDesignTableNotifyEventHandler( _
   ByVal DesignTable As System.Object _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_CloseDesignTableNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_CloseDesignTableNotifyEventHandler( 
   System.object DesignTable
)
```

```

public delegate System.int DPartDocEvents_CloseDesignTableNotifyEventHandler( 
   System.Object^ DesignTable
)
```

#### Parameters

*DesignTable*
:   [Design table](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)

Remarks

The IPartDoc event [OpenDesignTableNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_OpenDesignTableNotifyEventHandler.md) post-notifies when a design table has been opened for editing.

If developing a C++ application, use [swPartOpenDesignTableNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_CloseDesignTableNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_CloseDesignTableNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
