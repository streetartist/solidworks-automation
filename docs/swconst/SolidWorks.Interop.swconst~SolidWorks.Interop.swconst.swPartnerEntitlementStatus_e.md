# swPartnerEntitlementStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPartnerEntitlementStatus_e`

Partner entitlement status.
Partner entitlement status.

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

<System.Runtime.InteropServices.GuidAttribute("4932330A-8338-4DC6-9AAC-53BF660CF914")>
Public Enum swPartnerEntitlementStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPartnerEntitlementStatus_e
```

```

[System.Runtime.InteropServices.Guid("4932330A-8338-4DC6-9AAC-53BF660CF914")]
public enum swPartnerEntitlementStatus_e : System.Enum 
```

```

public enum swPartnerEntitlementStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("4932330A-8338-4DC6-9AAC-53BF660CF914")
public enum swPartnerEntitlementStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("4932330A-8338-4DC6-9AAC-53BF660CF914")]
__value public enum swPartnerEntitlementStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("4932330A-8338-4DC6-9AAC-53BF660CF914")]
public enum class swPartnerEntitlementStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPEAddinGUIDMismatch** | 4 or 0x4 |
| **swPEAddinNameMismatch** | 2 or 0x2 |
| **swPEFail** | 1 or 0x1 |
| **swPELicenseError** | 64 or 0x40 |
| **swPELicenseExpired** | 16 or 0x10 |
| **swPESuccess** | 0 or 0x0 |
| **swPETierMismatch** | 32 or 0x20 |
| **swPEVersionMismatch** | 8 or 0x8 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPartnerEntitlementStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
