# swPropSheetType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropSheetType_e`

Property sheet types.
Property sheet types.

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

<System.Runtime.InteropServices.GuidAttribute("56908F53-A82D-4229-B7C5-40C8332C707F")>
Public Enum swPropSheetType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPropSheetType_e
```

```

[System.Runtime.InteropServices.Guid("56908F53-A82D-4229-B7C5-40C8332C707F")]
public enum swPropSheetType_e : System.Enum 
```

```

public enum swPropSheetType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("56908F53-A82D-4229-B7C5-40C8332C707F")
public enum swPropSheetType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("56908F53-A82D-4229-B7C5-40C8332C707F")]
__value public enum swPropSheetType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("56908F53-A82D-4229-B7C5-40C8332C707F")]
public enum class swPropSheetType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPropSheetAmbientLight** | 3 = Property sheet ambient light |
| **swPropSheetDirectionalLight** | 4 = Property sheet directional light |
| **swPropSheetLighting** | 1 = Property sheet lighting |
| **swPropSheetNotValid** | 0 = Invalid property sheet |
| **swPropSheetPositionLight** | 5 = Property sheet position light |
| **swPropSheetSpotLight** | 6 = Property sheet spot light |
| **swPropSheetToolsOptions** | 2 = Property sheet tools options |

Remarks

This enumerator specifies possible values for the types of [ISWPropertySheet](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet.html)s exported by the SOLIDWORKS software when a SldWorks notification of type [swAppPropertySheetCreateNotify](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppNotify_e.md) is sent.

An example of a property sheet is the dialog that is displayed when you click Tools, Options. This dialog consists of a base property sheet and property pages stacked on top of it. To display a specific property page, click its tab.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPropSheetType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
