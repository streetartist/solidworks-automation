# DModelViewEvents_DestroyNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_DestroyNotify2EventHandler`

Pre-notifies the user program when a model view is about to be destroyed.
Pre-notifies the user program when a model view is about to be destroyed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_DestroyNotify2EventHandler( _
   ByVal DestroyType As System.Integer _
) As System.Integer
```

```

Dim instance As New DModelViewEvents_DestroyNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_DestroyNotify2EventHandler( 
   System.int DestroyType
)
```

```

public delegate System.int DModelViewEvents_DestroyNotify2EventHandler( 
   System.int DestroyType
)
```

#### Parameters

*DestroyType*
:   Value as defined by [swDestroyNotifyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDestroyNotifyType_e.html)

Remarks

This event is sent when a view is being destroyed and will no longer be available to the end-user. In this case, the destroyType value is swDestroyNotifyDestroy.

This event is also sent for each view of a model when the document is closed, yet the view is not destroyed. This can happen when the model is being used by an open assembly or drawing document. In this case, the destroyType value is swDestroyNotifyHidden. This indicates that the view is still available for use, but is not visible.

If the part is then reopened, a IPartDoc [ViewNewNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ViewNewNotify2EventHandler.md) event is again sent for all views in the part. At this point, you can recreate your link to these views, or if your application did not destroy the views, you can recognize that these views are no longer hidden. When the document and all referencing assemblies and drawings are finally closed, then the views are destroyed and this event is sent for each of the model views, with the destroyType = swDestroyNotifyDestroy.

If developing a C++ application, use [swViewDestroyNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_DestroyNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_DestroyNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
