# DAssemblyDocEvents_ViewNewNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ViewNewNotify2EventHandler`

Post-notifies the user program when a new view model window has been created.
Post-notifies the user program when a new view model window has been created.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ViewNewNotify2EventHandler( _
   ByVal viewBeingAdded As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ViewNewNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ViewNewNotify2EventHandler( 
   System.object viewBeingAdded
)
```

```

public delegate System.int DAssemblyDocEvents_ViewNewNotify2EventHandler( 
   System.Object^ viewBeingAdded
)
```

#### Parameters

*viewBeingAdded*
:   New [view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) window

Remarks

If developing a C++ application, use [swAssemblyViewNewNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

This event is sent for each new model view created by the window splitter bar. It is also sent for each new model view created in a document when Window, New Window is selected. A Dispatch pointer to the new model view is passed, which can be used to register for [IModelView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md) events or to run the various ModelView APIs such as [IModelView::GetViewHWnd](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewHWnd.md).

Because [FileOpenNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.md) and [FileNewNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewNotify2EventHandler.md) are post-notifications, SOLIDWORKS has already constructed the model views and has already fired this event by the time your application receives FileOpenNotify2 or FileNewNotify2. Therefore, within your functions that handle FileOpenNotify2 and FileNewNotify2, you should programmatically traverse each model view in the newly opened or created document ([IModelDoc2::EnumModelViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EnumModelViews.md) or [IModelDoc2::GetFirstModelView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.md) or [IModelDoc2::IGetFirstModelView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.md) and [IModelView::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetNext.md) or [IModelView::IGetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetNext.md)), and register each view for ModelView events.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_ViewNewNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ViewNewNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
