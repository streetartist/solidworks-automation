# swViewNotify_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swViewNotify_e`

Model view notifications.
Model view notifications.

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("A7316ED7-77C7-44A6-8F66-3E1FAE523FFE")>
Public Enum swViewNotify_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swViewNotify_e
```

```

[System.Runtime.InteropServices.Guid("A7316ED7-77C7-44A6-8F66-3E1FAE523FFE")]
public enum swViewNotify_e : System.Enum 
```

```

public enum swViewNotify_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("A7316ED7-77C7-44A6-8F66-3E1FAE523FFE")
public enum swViewNotify_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("A7316ED7-77C7-44A6-8F66-3E1FAE523FFE")]
__value public enum swViewNotify_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("A7316ED7-77C7-44A6-8F66-3E1FAE523FFE")]
public enum class swViewNotify_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swViewBufferSwapNotify** | 5 = [BufferSwapNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_BufferSwapNotifyEventHandler.html) |
| **swViewChangeNotify** | 2 = [ViewChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_ViewChangeNotifyEventHandler.html) |
| **swViewDestroyNotify** | Obsolete |
| **swViewDestroyNotify2** | 6 = [DestroyNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_DestroyNotify2EventHandler.html) |
| **swViewDisplayModeChangePostNotify** | 13 = [DisplayModeChangePostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_DisplayModeChangePostNotifyEventHandler.html) |
| **swViewDisplayModeChangePreNotify** | 12 = [DisplayModeChangePreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_DisplayModeChangePreNotifyEventHandler.html) |
| **swViewGraphicsRenderPostNotify** | 11 = [GraphicsRenderPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_GraphicsRenderPostNotifyEventHandler.html) |
| **swViewPerspectiveViewNotify** | 7 = [PerspectiveViewNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_PerspectiveViewNotifyEventHandler.html) |
| **swViewPrintNotify** | Obsolete |
| **swViewPrintNotify2** | 14 = [PrintNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_PrintNotify2EventHandler.html) |
| **swViewRenderLayer0Notify** | 8 = [RenderLayerNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_RenderLayer0NotifyEventHandler.html) |
| **swViewRepaintNotify** | 1 = [RepaintNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_RepaintNotifyEventHandler.html) |
| **swViewRepaintPostNotify** | 4 = [RepaintPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_RepaintPostNotifyEventHandler.html) |
| **swViewUserClearSelectionsNotify** | 9 = [UserClearSelectionsNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_UserClearSelectionsNotifyEventHandler.html) |

Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports model view events (e.g., DocView.h), include:

BEGIN\_SINK\_MAP(CDocView)

SINK\_ENTRY\_EX(ID\_MODELVIEW\_EVENTS, DIID\_DModelViewEvents, swViewDestroyNotify, DestroyNotify)

SINK\_ENTRY\_EX(ID\_MODELVIEW\_EVENTS, DIID\_DModelViewEvents, swViewRepaintNotify, RepaintNotify)

END\_SINK\_MAP()

If developing a C++ application, use these enumerators to [register for notifications](sldworksapiprogguide.chm::/overview/events.htm) for the [IModelView](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) events.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swViewNotify\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
