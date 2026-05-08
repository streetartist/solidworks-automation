# swTaskPaneNotify_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTaskPaneNotify_e`

Task Pane notifications.
Task Pane notifications.

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

<System.Runtime.InteropServices.GuidAttribute("0A275BEB-A561-4352-82A0-4A9BBE3BB4DB")>
Public Enum swTaskPaneNotify_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swTaskPaneNotify_e
```

```

[System.Runtime.InteropServices.Guid("0A275BEB-A561-4352-82A0-4A9BBE3BB4DB")]
public enum swTaskPaneNotify_e : System.Enum 
```

```

public enum swTaskPaneNotify_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("0A275BEB-A561-4352-82A0-4A9BBE3BB4DB")
public enum swTaskPaneNotify_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("0A275BEB-A561-4352-82A0-4A9BBE3BB4DB")]
__value public enum swTaskPaneNotify_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("0A275BEB-A561-4352-82A0-4A9BBE3BB4DB")]
public enum class swTaskPaneNotify_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAppTaskPaneActivateNotify** | 1 = [ActivateNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler.html) |
| **swAppTaskPaneDeactivateNotify** | 2 = [DeactivateNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler.html) |
| **swAppTaskPaneDestroyNotify** | 3 = [DestroyNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DTaskpaneViewEvents_TaskPaneDestroyNotifyEventHandler.html) |
| **swAppTaskPaneToolbarButtonClicked** | 4 = [ToolbarButtonClicked](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler.html) |

Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports Task Pane events (e.g., Taskpane.h, include:

DECLARE\_REGISTRY\_RESOURCEID(IDR\_TaskPane)

BEGIN\_SINK\_MAP(CTaskPane)

SINK\_ENTRY\_EX(ID\_TASKPANE\_EVENTS, DIID\_DTaskpaneViewEvents, swAppTaskPaneDestroyNotify, DestroyNotify)

SINK\_ENTRY\_EX(ID\_TASKPANE\_EVENTS, DIID\_DTaskpaneViewEvents, swAppTaskPaneActivateNotify, ActivateNotify)

SINK\_ENTRY\_EX(ID\_TASKPANE\_EVENTS, DIID\_DTaskpaneViewEvents, swAppTaskPaneDeactivateNotify, DeActivateNotify)

END\_SINK\_MAP()

If developing a C++ application, use these enumerators to [register for notifications](sldworksapiprogguide.chm::/overview/events.htm) for the [ITaskpaneView](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITaskpaneView.html) events.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swTaskPaneNotify\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
