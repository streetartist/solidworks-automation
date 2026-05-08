# DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler`

Post-notifies the user program when the active document's FeatureManager design tree is being rebuilt.
Post-notifies the user program when the active document's FeatureManager design tree is being rebuilt.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler() As System.Integer
```

```

Dim instance As New DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler()
```

```

public delegate System.int DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler();
```

Remarks

This notification is only used by SOLIDWORKS Animator.

If developing a C++ application, use [swDrawingFeatureManagerTreeRebuildNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_FeatureManagerTreeRebuildNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
