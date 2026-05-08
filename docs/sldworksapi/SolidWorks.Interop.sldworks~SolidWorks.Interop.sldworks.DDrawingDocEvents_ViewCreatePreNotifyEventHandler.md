# DDrawingDocEvents_ViewCreatePreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ViewCreatePreNotifyEventHandler`

Pre-notifies the user application when a drawing view is about to be created.
Pre-notifies the user application when a drawing view is about to be created.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_ViewCreatePreNotifyEventHandler( _
   ByVal modelDocBeingAdded As System.Object _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_ViewCreatePreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_ViewCreatePreNotifyEventHandler( 
   System.object modelDocBeingAdded
)
```

```

public delegate System.int DDrawingDocEvents_ViewCreatePreNotifyEventHandler( 
   System.Object^ modelDocBeingAdded
)
```

#### Parameters

*modelDocBeingAdded*
:   [Model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) used to create the drawing view

Remarks

This notification occurs just before the drawing view is added as a feature to the drawing document. Use [IModelDoc2::GetPathName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) and [IConfigurationManager::ActiveConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md) to get the model document's path, filename, and configuration to use to create the drawing view.

This notification also gets fired for empty drawing views. Because empty drawing views do not have a model document, the argument ModelDocBeingAdded is NULL or Nothing. Use the event handler to check ModelDocBeingAdded for NULL or Nothing before using this notification.

If developing a C++ application, then use [swDrawingViewCreatePreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_ViewCreatePreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ViewCreatePreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
