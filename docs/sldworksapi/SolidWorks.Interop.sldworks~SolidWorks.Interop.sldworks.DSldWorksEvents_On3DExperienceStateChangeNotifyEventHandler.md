# DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler`

Fired when 3DExperience changes state.
Fired when 3DExperience changes state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler( _
   ByVal newState As System.Integer _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler( 
   System.int newState
)
```

```

public delegate System.int DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler( 
   System.int newState
)
```

#### Parameters

*newState*
:   New state as defined by [sw3DExperienceState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DExperienceState_e.html)

Remarks

If developing a C++ application, use [swAppOn3DExperienceStateChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_On3DExperienceStateChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
