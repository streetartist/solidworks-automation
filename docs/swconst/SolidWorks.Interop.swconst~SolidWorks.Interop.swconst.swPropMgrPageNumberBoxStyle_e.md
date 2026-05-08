# swPropMgrPageNumberBoxStyle_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropMgrPageNumberBoxStyle_e`

PropertyManager page number box styles. Bitmask.
PropertyManager page number box styles. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("74CEAB56-41EE-41A1-A2A7-63AAB2CEBA02")>
Public Enum swPropMgrPageNumberBoxStyle_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPropMgrPageNumberBoxStyle_e
```

```

[System.Runtime.InteropServices.Guid("74CEAB56-41EE-41A1-A2A7-63AAB2CEBA02")]
public enum swPropMgrPageNumberBoxStyle_e : System.Enum 
```

```

public enum swPropMgrPageNumberBoxStyle_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("74CEAB56-41EE-41A1-A2A7-63AAB2CEBA02")
public enum swPropMgrPageNumberBoxStyle_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("74CEAB56-41EE-41A1-A2A7-63AAB2CEBA02")]
__value public enum swPropMgrPageNumberBoxStyle_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("74CEAB56-41EE-41A1-A2A7-63AAB2CEBA02")]
public enum class swPropMgrPageNumberBoxStyle_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPropMgrPageNumberBoxStyle\_AvoidSelectionText** | 4 or 0x4; The item the user selects in the attached drop-down list does not appear in the number box. Instead, the user's selection causes the add-in to get a callback via [IPropertyManagerPage2Handler9::OnComboboxSelectionChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnComboboxSelectionChanged.md); the Id argument will be the number box; the add-in is expected to respond by setting the value for the number box using [IPropertyManagerPageNumberbox::Value](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageNumberbox~Value.html). |
| **swPropMgrPageNumberBoxStyle\_ComboEditBox** | 1 or 0x1; Enables the attached drop-down list for the number box; user can type a value or select a value from the attached drop-down list for the number box |
| **swPropMgrPageNumberBoxStyle\_EditBoxReadOnly** | 2 or 0x2; User can only select a value from the attached drop-down list for the number box  **NOTE:** You can set swPropMgrPageNumberBoxStyle\_EditBoxReadOnly either before or after the PropertyManager page is displayed. If set after the PropertyManager page is displayed and the number box contains editable text, then that text cannot be edited by the user |
| **swPropMgrPageNumberBoxStyle\_NoScrollArrows** | 8 or 0x8; Do not show the up and down arrows in the number box, thus, disallowing incrementing or decrementing the value in the number box |
| **swPropMgrPageNumberBoxStyle\_Slider** | 16 or 0x10; Slider |
| **swPropMgrPageNumberBoxStyle\_SuppressNotifyWhileTracking** | 64 or 0x40; Suppress sending multiple notifications when a user is dragging or spinning the slider of a number box on a PropertyManager page; instead, send only one notification; see [IPropertyManagerPage2Handler9::OnNumberboxChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnNumberboxChanged.md) for details |
| **swPropMgrPageNumberBoxStyle\_Thumbwheel** | 32 or 0x20; Thumbwheel |

Remarks

When the user selects an item in the attached drop-down list, SOLIDWORKS attempts to use that item as a value in the number box. Thus, the items in the attached drop-down list should be numeric values and optionally include their units. The add-in then gets a callback via IPropertyManagerPage2Handler9::OnNumberboxChanged as if the user had typed a value in the number box or clicked the up-arrow or down-arrow buttons to increment or decrement the value.

If you do not want your add-in to directly use items in the attached drop-down list in the number box, but instead want it to react to the user selecting a computed or linked value in the number box, then use swPropMgrPageNumberBoxStyle\_AvoidSelectionText.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPropMgrPageNumberBoxStyle\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
