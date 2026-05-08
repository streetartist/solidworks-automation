# DPartDocEvents_AutoSaveNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AutoSaveNotifyEventHandler`

Fired when the part document is automatically saved.
Fired when the part document is automatically saved.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_AutoSaveNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_AutoSaveNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_AutoSaveNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DPartDocEvents_AutoSaveNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   File name to which to save the part document

Remarks

If developing a C++ application, use [swPartAutoSaveNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_AutoSaveNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AutoSaveNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
