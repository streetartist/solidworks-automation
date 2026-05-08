# swMouseNotify_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMouseNotify_e`

Mouse notifications.
Mouse notifications.

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

<System.Runtime.InteropServices.GuidAttribute("CD51833C-74E3-46F7-8C7A-88C3180E2D18")>
Public Enum swMouseNotify_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swMouseNotify_e
```

```

[System.Runtime.InteropServices.Guid("CD51833C-74E3-46F7-8C7A-88C3180E2D18")]
public enum swMouseNotify_e : System.Enum 
```

```

public enum swMouseNotify_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("CD51833C-74E3-46F7-8C7A-88C3180E2D18")
public enum swMouseNotify_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("CD51833C-74E3-46F7-8C7A-88C3180E2D18")]
__value public enum swMouseNotify_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("CD51833C-74E3-46F7-8C7A-88C3180E2D18")]
public enum class swMouseNotify_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swMouseLBtnDblClkNotify** | 9 = [MouseLBtnDblClkNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DMouseEvents_MouseLBtnDblClkNotifyEventHandler.html) |
| **swMouseLBtnDownNotify** | 3 = [MouseLBtnDownNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DMouseEvents_MouseLBtnDownNotifyEventHandler.html) |
| **swMouseLBtnUpNotify** | 4 = [MouseLBtnUpNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DMouseEvents_MouseLBtnUpNotifyEventHandler.html) |
| **swMouseMBtnDblClkNotify** | 11 = [MouseMBtnDblClkNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DMouseEvents_MouseMBtnDblClkNotifyEventHandler.html) |
| **swMouseMBtnDownNotify** | 7 = [MouseMBtnDownNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DMouseEvents_MouseMBtnDownNotifyEventHandler.html) |
| **swMouseMBtnUpNotify** | 8 = [MouseMBtnUpNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DMouseEvents_MouseMBtnUpNotifyEventHandler.html) |
| **swMouseMoveNotify** | 2 = [MouseMoveNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DMouseEvents_MouseMoveNotifyEventHandler.html) |
| **swMouseNotify** | 1 = [MouseNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DMouseEvents_MouseNotifyEventHandler.html) |
| **swMouseRBtnDblClkNotify** | 10 = [MouseRBtnDblClkNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DMouseEvents_MouseRBtnDblClkNotifyEventHandler.html) |
| **swMouseRBtnDownNotify** | 5 = [MouseRBtnDownNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DMouseEvents_MouseRBtnDownNotifyEventHandler.html) |
| **swMouseRBtnUpNotify** | 6 = [MouseRBtnUpNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DMouseEvents_MouseRBtnUpNotifyEventHandler.html) |
| **swMouseSelectNotify** | 12 = [MouseSelectNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DMouseEvents_MouseSelectNotifyEventHandler.html) |

Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports mouse events (e.g., Mouse.h), include:

DECLARE\_REGISTRY\_RESOURCEID(IDR\_MOUSE)

BEGIN\_SINK\_MAP(CMouse)

SINK\_ENTRY\_EX(ID\_MOUSE\_EVENTS, DIID\_DMouseEvents, swMouseMoveNotify, MouseMoveNotify)

SINK\_ENTRY\_EX(ID\_MOUSE\_EVENTS, DIID\_DMouseEvents, swMouseSelectNotify, MouseSelectNotify)

SINK\_ENTRY\_EX(ID\_MOUSE\_EVENTS, DIID\_DMouseEvents, swMouseLBtnDownNotify, MouseLBtnDownNotify)

END\_SINK\_MAP()

If developing a C++ application, use these enumerators to [register for notifications](sldworksapiprogguide.chm::/overview/events.htm) for the [IMouse](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMouse.html) events.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swMouseNotify\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
