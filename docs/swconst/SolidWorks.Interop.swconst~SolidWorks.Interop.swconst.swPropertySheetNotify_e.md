# swPropertySheetNotify_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropertySheetNotify_e`

Property sheet notifications.
Property sheet notifications.

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

<System.Runtime.InteropServices.GuidAttribute("9660B905-402C-4448-9C3B-1938F1110A87")>
Public Enum swPropertySheetNotify_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPropertySheetNotify_e
```

```

[System.Runtime.InteropServices.Guid("9660B905-402C-4448-9C3B-1938F1110A87")]
public enum swPropertySheetNotify_e : System.Enum 
```

```

public enum swPropertySheetNotify_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("9660B905-402C-4448-9C3B-1938F1110A87")
public enum swPropertySheetNotify_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("9660B905-402C-4448-9C3B-1938F1110A87")]
__value public enum swPropertySheetNotify_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("9660B905-402C-4448-9C3B-1938F1110A87")]
public enum class swPropertySheetNotify_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPropertySheetCreateControlNotify** | 5 = [CreateControlNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSWPropertySheetEvents_CreateControlNotifyEventHandler.html) |
| **swPropertySheetDestroyNotify** | 1 = [DestroyNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSWPropertySheetEvents_DestroyNotifyEventHandler.html) |
| **swPropertySheetHelpNotify** | 2 = [HelpNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSWPropertySheetEvents_HelpNotifyEventHandler.html) |
| **swPropertySheetOnCancelNotify** | 4 = [OnCancelNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSWPropertySheetEvents_OnCancelNotifyEventHandler.html) |
| **swPropertySheetOnOKNotify** | 3 = [OnOKNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSWPropertySheetEvents_OnOKNotifyEventHandler.html) |

Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports property sheet events ( e.g., SwPropertySheet.h), include:

BEGIN\_SINK\_MAP(CSwPropertySheet)

SINK\_ENTRY\_EX(ID\_SWPROPERTYSHEET\_EVENTS, DIID\_DSwPropertySheetEvents, swPropertySheetCreateControlNotify, CreateControlNotify)

SINK\_ENTRY\_EX(ID\_SWPROPERTYSHEET\_EVENTS, DIID\_DSwPropertySheetEvents, swPropertySheetDestroyNotify, DestroyNotify)

END\_SINK\_MAP()

If developing a C++ application, use these enumerators to [register for notifications](sldworksapiprogguide.chm::/overview/events.htm) for [ISWPropertySheet](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet.html) events.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPropertySheetNotify\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
