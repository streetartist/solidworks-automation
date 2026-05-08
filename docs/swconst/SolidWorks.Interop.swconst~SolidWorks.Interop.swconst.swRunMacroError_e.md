# swRunMacroError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRunMacroError_e`

VBA macro error codes.
VBA macro error codes.

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

<System.Runtime.InteropServices.GuidAttribute("250DDB99-84A9-4D95-B9BE-55CBDF60B627")>
Public Enum swRunMacroError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRunMacroError_e
```

```

[System.Runtime.InteropServices.Guid("250DDB99-84A9-4D95-B9BE-55CBDF60B627")]
public enum swRunMacroError_e : System.Enum 
```

```

public enum swRunMacroError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("250DDB99-84A9-4D95-B9BE-55CBDF60B627")
public enum swRunMacroError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("250DDB99-84A9-4D95-B9BE-55CBDF60B627")]
__value public enum swRunMacroError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("250DDB99-84A9-4D95-B9BE-55CBDF60B627")]
public enum class swRunMacroError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swRunMacroError\_BadParmCount** | 9 |
| **swRunMacroError\_BadVarType** | 10 |
| **swRunMacroError\_Busy** | 17 |
| **swRunMacroError\_CallFailed** | 20 |
| **swRunMacroError\_CallRejected** | 19 |
| **swRunMacroError\_CantSave** | 27 |
| **swRunMacroError\_ConnectionTerminated** | 18 |
| **swRunMacroError\_DiskError** | 26 |
| **swRunMacroError\_Exception** | 12 |
| **swRunMacroError\_InvalidArg** | 1 |
| **swRunMacroError\_Invalidindex** | 22 |
| **swRunMacroError\_InvalidProcname** | 6 |
| **swRunMacroError\_InvalidPropertyType** | 7 |
| **swRunMacroError\_MacrosAreDisabled** | 2 |
| **swRunMacroError\_NoPermission** | 23 |
| **swRunMacroError\_NotInDesignMode** | 3 |
| **swRunMacroError\_OnlyCodeModules** | 4 |
| **swRunMacroError\_OpenFileFailed** | 28 |
| **swRunMacroError\_OutOfMemory** | 5 |
| **swRunMacroError\_Overflow** | 13 |
| **swRunMacroError\_ParmNotOptional** | 15 |
| **swRunMacroError\_Reverted** | 24 |
| **swRunMacroError\_SuborfuncExpected** | 8 |
| **swRunMacroError\_TooManyOpenFiles** | 25 |
| **swRunMacroError\_TypeMismatch** | 14 |
| **swRunMacroError\_UnknownLcid** | 16 |
| **swRunMacroError\_UserInterrupt** | 11 |
| **swRunMacroError\_Zombied** | 21 |

Remarks

VSTA error codes not yet implementd.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRunMacroError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
