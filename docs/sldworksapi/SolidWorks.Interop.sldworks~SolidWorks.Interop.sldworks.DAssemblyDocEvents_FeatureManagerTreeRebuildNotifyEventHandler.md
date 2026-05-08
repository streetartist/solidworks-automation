# DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler`

Post-notifies the user program when the active document's FeatureManager design tree is being rebuilt.
Post-notifies the user program when the active document's FeatureManager design tree is being rebuilt.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler() As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler()
```

```

public delegate System.int DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAssemblyFeatureManagerTreeRebuildNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

This notification is only used by SOLIDWORKS Animator.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_FeatureManagerTreeRebuildNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
