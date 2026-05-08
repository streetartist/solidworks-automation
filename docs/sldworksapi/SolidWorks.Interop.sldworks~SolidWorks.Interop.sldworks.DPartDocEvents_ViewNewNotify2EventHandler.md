# DPartDocEvents_ViewNewNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ViewNewNotify2EventHandler`

Post-notifies the user program when a new model view window is created. For example, this event is sent for each new model view created by the window split bar.
Post-notifies the user program when a new model view window is created. For example, this event is sent for each new model view created by the window split bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_ViewNewNotify2EventHandler( _
   ByVal viewBeingAdded As System.Object _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_ViewNewNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_ViewNewNotify2EventHandler( 
   System.object viewBeingAdded
)
```

```

public delegate System.int DPartDocEvents_ViewNewNotify2EventHandler( 
   System.Object^ viewBeingAdded
)
```

#### Parameters

*viewBeingAdded*
:   New window view

Remarks

SOLIDWORKS generates this notification when the user selects Window, New Window, or uses the splitter and clicks in the new view.

SOLIDWORKS passes a Dispatch pointer to the new view, which you can use to register for [IModelView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md) events or to run IModelView functions, such as [IModelView::GetViewHWnd](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewHWnd.md).

Since the SOLIDWORKS events [FileOpenNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.md) and [FileNewNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewNotify2EventHandler.md) are post-notifications, SOLIDWORKS has already constructed the views and has already generated this event by the time your application receives FileOpenNotify2 or FileNewNotify2. Therefore, within your functions that handle FileOpenNotify2 and FileNewNotify2, you should programmatically traverse each view in the newly opened or created document ([IEnumModelViews::Next](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews~Next.md) or [IModelDoc2::GetFirstModelView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.md) or [IModelDoc2::IGetFirstModelView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.md) or [IModelView::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetNext.md) or [IModelView::IGetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetNext.md)), and register each view for IModelView events.

The difference between [ViewNewNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ViewNewNotifyEventHandler.md) and ViewNewNotify2 is that ViewNewNotify is sent only when the view is activated for the first time. With ViewNewNotify2, the notification is sent whenever a new view is initialized and available for use by the third-party application. The view does not need to be activated by the user for the event to be sent.

If developing a C++ application, use [swPartViewNewNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_ViewNewNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ViewNewNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
