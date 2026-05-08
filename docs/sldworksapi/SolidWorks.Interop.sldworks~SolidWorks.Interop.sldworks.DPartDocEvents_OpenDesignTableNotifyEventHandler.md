# DPartDocEvents_OpenDesignTableNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_OpenDesignTableNotifyEventHandler`

Post-notifies your application that a design table has been opened for editing.
Post-notifies your application that a design table has been opened for editing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_OpenDesignTableNotifyEventHandler( _
   ByVal DesignTable As System.Object _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_OpenDesignTableNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_OpenDesignTableNotifyEventHandler( 
   System.object DesignTable
)
```

```

public delegate System.int DPartDocEvents_OpenDesignTableNotifyEventHandler( 
   System.Object^ DesignTable
)
```

#### Parameters

*DesignTable*
:   [Design table](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)

Remarks

The IPartDoc event [CloseDesignTableNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_CloseDesignTableNotifyEventHandler.md) pre-notifies your application that a design table that was opened for editing is about to be closed.

If developing a C++ application, use [swPartOpenDesignTableNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_OpenDesignTableNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_OpenDesignTableNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
