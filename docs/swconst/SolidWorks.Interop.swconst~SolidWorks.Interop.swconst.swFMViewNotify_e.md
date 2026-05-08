# swFMViewNotify_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFMViewNotify_e`

FeatureManager design tree notifications.
FeatureManager design tree notifications.

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

<System.Runtime.InteropServices.GuidAttribute("D10B86A9-4E9A-4643-883E-26C64F9B826B")>
Public Enum swFMViewNotify_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFMViewNotify_e
```

```

[System.Runtime.InteropServices.Guid("D10B86A9-4E9A-4643-883E-26C64F9B826B")]
public enum swFMViewNotify_e : System.Enum 
```

```

public enum swFMViewNotify_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D10B86A9-4E9A-4643-883E-26C64F9B826B")
public enum swFMViewNotify_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D10B86A9-4E9A-4643-883E-26C64F9B826B")]
__value public enum swFMViewNotify_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D10B86A9-4E9A-4643-883E-26C64F9B826B")]
public enum class swFMViewNotify_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFMViewActivateNotify** | 1 = [ActivateNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DFeatMgrViewEvents_ActivateNotifyEventHandler.html) |
| **swFMViewDeactivateNotify** | 2 = [DeactivateNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DFeatMgrViewEvents_DeactivateNotifyEventHandler.html) |
| **swFMViewDestroyNotify** | 3 = [DestroyNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DFeatMgrViewEvents_DestroyNotifyEventHandler.html) |

Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports FeatureManager design tree events (e.g., FeatMgrView.h), include:

DECLARE\_REGISTRY\_RESOURCEID(IDR\_FeatMgrView)

BEGIN\_SINK\_MAP(CFeatMgrView)

SINK\_ENTRY\_EX(ID\_FEATMGRVIEW\_EVENTS, DIID\_DFeatMgrViewEvents, swFMViewDestroyNotify , DestroyNotify)

SINK\_ENTRY\_EX(ID\_FEATMGRVIEW\_EVENTS, DIID\_DFeatMgrViewEvents, swFMViewActivateNotify, ActivateNotify)

SINK\_ENTRY\_EX(ID\_FEATMGRVIEW\_EVENTS, DIID\_DFeatMgrViewEvents, swFMViewDeactivateNotify , DeActivateNotify)

END\_SINK\_MAP()

If developing a C++ application, use these enumerators to [register for notifications](sldworksapiprogguide.chm::/overview/events.htm) for [IFeatMgrView](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView.html) events.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFMViewNotify\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
