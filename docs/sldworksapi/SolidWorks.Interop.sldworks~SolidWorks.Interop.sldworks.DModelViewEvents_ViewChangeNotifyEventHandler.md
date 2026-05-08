# DModelViewEvents_ViewChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_ViewChangeNotifyEventHandler`

Post-notifies the user program when a view is altered and returns the new transform matrix of the view.
Post-notifies the user program when a view is altered and returns the new transform matrix of the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_ViewChangeNotifyEventHandler( _
   ByVal View As System.Object _
) As System.Integer
```

```

Dim instance As New DModelViewEvents_ViewChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_ViewChangeNotifyEventHandler( 
   System.object View
)
```

```

public delegate System.int DModelViewEvents_ViewChangeNotifyEventHandler( 
   System.Object^ View
)
```

#### Parameters

*View*
:   See **Remarks**

Remarks

In Visual Basic for Applications (VBA), the view argument is a VARIANT of type SafeArray of 16 doubles:

|  |  |
| --- | --- |
| **Elements** | **Values** |
| First 9 | Standard 3x3 rotation matrix |
| Next 3 | Define translation |
| Next 1 | For scaling |
| Last 3 | Not used |

Your application is responsible for destroying the SafeArray when you are finished with it.

If developing a C++ application, use [swViewChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_ViewChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_ViewChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
