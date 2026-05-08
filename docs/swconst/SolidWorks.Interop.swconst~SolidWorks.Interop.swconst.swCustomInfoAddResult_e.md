# swCustomInfoAddResult_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomInfoAddResult_e`

Result codes when adding custom properties.
Result codes when adding custom properties.

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

<System.Runtime.InteropServices.GuidAttribute("687CB334-1E07-4F3F-BDC2-25C56D9498E7")>
Public Enum swCustomInfoAddResult_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCustomInfoAddResult_e
```

```

[System.Runtime.InteropServices.Guid("687CB334-1E07-4F3F-BDC2-25C56D9498E7")]
public enum swCustomInfoAddResult_e : System.Enum 
```

```

public enum swCustomInfoAddResult_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("687CB334-1E07-4F3F-BDC2-25C56D9498E7")
public enum swCustomInfoAddResult_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("687CB334-1E07-4F3F-BDC2-25C56D9498E7")]
__value public enum swCustomInfoAddResult_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("687CB334-1E07-4F3F-BDC2-25C56D9498E7")]
public enum class swCustomInfoAddResult_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCustomInfoAddResult\_AddedOrChanged** | 0 = Success |
| **swCustomInfoAddResult\_GenericFail** | 1 = Failed to add the custom property |
| **swCustomInfoAddResult\_MismatchAgainstExistingType** | 2 = Existing custom property with the same name has a different type |
| **swCustomInfoAddResult\_MismatchAgainstLegacyTypes** | 4 = Cannot add the specified custom property to legacy architecture |
| **swCustomInfoAddResult\_MismatchAgainstSpecifiedType** | 3 = Specified value of the custom property does not match the specified type |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCustomInfoAddResult\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
