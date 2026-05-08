# DPartDocEvents_DestroyNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DestroyNotify2EventHandler`

Pre-notifies the user program when a part document is about to be destroyed.
Pre-notifies the user program when a part document is about to be destroyed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_DestroyNotify2EventHandler( _
   ByVal DestroyType As System.Integer _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_DestroyNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_DestroyNotify2EventHandler( 
   System.int DestroyType
)
```

```

public delegate System.int DPartDocEvents_DestroyNotify2EventHandler( 
   System.int DestroyType
)
```

#### Parameters

*DestroyType*
:   Value as defined by [swDestroyNotifyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDestroyNotifyType_e.html)

Remarks

The DestroyType argument indicates whether the part is being removed from memory (swDestroyNotifyDestroy) or if it remains open due to an outside reference (swDestroyNotifyHidden).

If developing a C++ application, use [swPartDestroyNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_DestroyNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DestroyNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
