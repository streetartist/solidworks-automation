# swInterfaceBrightnessColor_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInterfaceBrightnessColor_e`

Background colors.
Background colors.

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

<System.Runtime.InteropServices.GuidAttribute("5DFC6CFA-0201-4459-885C-908C20ABBD71")>
Public Enum swInterfaceBrightnessColor_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swInterfaceBrightnessColor_e
```

```

[System.Runtime.InteropServices.Guid("5DFC6CFA-0201-4459-885C-908C20ABBD71")]
public enum swInterfaceBrightnessColor_e : System.Enum 
```

```

public enum swInterfaceBrightnessColor_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("5DFC6CFA-0201-4459-885C-908C20ABBD71")
public enum swInterfaceBrightnessColor_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("5DFC6CFA-0201-4459-885C-908C20ABBD71")]
__value public enum swInterfaceBrightnessColor_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("5DFC6CFA-0201-4459-885C-908C20ABBD71")]
public enum class swInterfaceBrightnessColor_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swIBColor\_ActiveTabColor** | 3 = Color of a tab's fill area when the tab is active |
| **swIBColor\_ButtonFillCheckedAndHotColor** | 8 = Color of the CommandManager flat-style button's fill area |
| **swIBColor\_ButtonFillCheckedColor** | 6 = Color of the CommandManager flat-style button's fill area |
| **swIBColor\_ButtonFillHotColor** | 5 = Color of the CommandManager flat-style button's fill area |
| **swIBColor\_ButtonFillPressedColor** | 7 = Color of the CommandManager flat-style button's fill area when pressing and holding down the left button of the mouse |
| **swIBColor\_DisabledTextColor** | 2 = Color of text when text is disabled |
| **swIBColor\_EnabledTextColor** | 1 = Color of text when text is enabled |
| **swIBColor\_FeatureMgrBkgnd** | 0 = Background color is the same as the FeatureManager design tree's background color |
| **swIBColor\_InactiveTabColor** | 4 = Color of a tab's fill area when the tab is inactive |

Remarks

If you want your add-in to use the same colors for your buttons as used by the SOLIDWORKS CommandManager buttons, then you can query and use these values.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swInterfaceBrightnessColor\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
