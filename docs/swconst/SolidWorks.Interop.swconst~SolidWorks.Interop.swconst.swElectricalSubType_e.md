# swElectricalSubType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swElectricalSubType_e`

Electrical route sub types for connection points.
Electrical route sub types for connection points.

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

<System.Runtime.InteropServices.GuidAttribute("53DA933F-DE09-429D-AD0D-ADC5A354F1FD")>
Public Enum swElectricalSubType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swElectricalSubType_e
```

```

[System.Runtime.InteropServices.Guid("53DA933F-DE09-429D-AD0D-ADC5A354F1FD")]
public enum swElectricalSubType_e : System.Enum 
```

```

public enum swElectricalSubType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("53DA933F-DE09-429D-AD0D-ADC5A354F1FD")
public enum swElectricalSubType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("53DA933F-DE09-429D-AD0D-ADC5A354F1FD")]
__value public enum swElectricalSubType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("53DA933F-DE09-429D-AD0D-ADC5A354F1FD")]
public enum class swElectricalSubType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swElectricalSubType\_ElectricalCableWire** | 1 = Cable wire |
| **swElectricalSubType\_ElectricalConduit** | 2 = Conduit |
| **swElectricalSubType\_ElectricalHarness** | 0 = Harness |
| **swElectricalSubType\_ElectricalRibbonCable** | 30 = Ribbon cable |
| **swElectricalSubType\_ElectricalStandardCable** | 3 = Standard cable |
| **swElectricalSubType\_NotElectrical** | 20 = Not electrical |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swElectricalSubType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
