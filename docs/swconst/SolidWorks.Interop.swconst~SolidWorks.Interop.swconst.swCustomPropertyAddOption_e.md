# swCustomPropertyAddOption_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomPropertyAddOption_e`

Options when adding custom properties.
Options when adding custom properties.

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

<System.Runtime.InteropServices.GuidAttribute("87DCBCCD-950A-41AB-BAEC-649248ACE1EA")>
Public Enum swCustomPropertyAddOption_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCustomPropertyAddOption_e
```

```

[System.Runtime.InteropServices.Guid("87DCBCCD-950A-41AB-BAEC-649248ACE1EA")]
public enum swCustomPropertyAddOption_e : System.Enum 
```

```

public enum swCustomPropertyAddOption_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("87DCBCCD-950A-41AB-BAEC-649248ACE1EA")
public enum swCustomPropertyAddOption_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("87DCBCCD-950A-41AB-BAEC-649248ACE1EA")]
__value public enum swCustomPropertyAddOption_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("87DCBCCD-950A-41AB-BAEC-649248ACE1EA")]
public enum class swCustomPropertyAddOption_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCustomPropertyDeleteAndAdd** | 1 = Delete an existing custom property having the same name and add the new custom property |
| **swCustomPropertyOnlyIfNew** | 0 = Add the custom property only if it is new |
| **swCustomPropertyReplaceValue** | 2 = Replace the value of an existing custom property having the same name |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCustomPropertyAddOption\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
