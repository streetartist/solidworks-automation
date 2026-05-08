# DPartDocEvents_CommandManagerTabActivatedPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_CommandManagerTabActivatedPreNotifyEventHandler`

Pre-notifies you that a SOLIDWORKS CommandManager tab is about to be activated.
Pre-notifies you that a SOLIDWORKS CommandManager tab is about to be activated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_CommandManagerTabActivatedPreNotifyEventHandler( _
   ByVal CommandTabIndex As System.Integer, _
   ByVal CommandTabName As System.String _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_CommandManagerTabActivatedPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_CommandManagerTabActivatedPreNotifyEventHandler( 
   System.int CommandTabIndex,
   System.string CommandTabName
)
```

```

public delegate System.int DPartDocEvents_CommandManagerTabActivatedPreNotifyEventHandler( 
   System.int CommandTabIndex,
   System.String^ CommandTabName
)
```

#### Parameters

*CommandTabIndex*
:   Index of the tab that is about to be activated

*CommandTabName*
:   Name of the tab

Remarks

If developing a C++ application, use [swPartCommandManagerTabActivatedPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_CommandManagerTabActivatedPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_CommandManagerTabActivatedPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
