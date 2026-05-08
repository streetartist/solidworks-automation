# DModelViewEvents_PrintNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_PrintNotifyEventHandler`

Obsolete. Superseded by DModelViewEvents_PrintNotify2EventHandler.
Obsolete. Superseded by [DModelViewEvents\_PrintNotify2EventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_PrintNotify2EventHandler.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_PrintNotifyEventHandler( _
   ByVal pDC As System.Long _
) As System.Integer
```

```

Dim instance As New DModelViewEvents_PrintNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_PrintNotifyEventHandler( 
   System.long pDC
)
```

```

public delegate System.int DModelViewEvents_PrintNotifyEventHandler( 
   System.int64 pDC
)
```

#### Parameters

*pDC*
:   HDC of the printer device context used to print the document

Remarks

Always return S\_OK in the swViewPrintNotify event handler.

If developing a C++ application, use [swViewPrintNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_PrintNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_PrintNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
