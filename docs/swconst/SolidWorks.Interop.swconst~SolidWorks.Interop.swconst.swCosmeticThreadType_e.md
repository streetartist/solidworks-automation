# swCosmeticThreadType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCosmeticThreadType_e`

Cosmetic thread types.
Cosmetic thread types.

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

<System.Runtime.InteropServices.GuidAttribute("2BB47770-EB08-4530-A72E-2A620AF93E95")>
Public Enum swCosmeticThreadType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCosmeticThreadType_e
```

```

[System.Runtime.InteropServices.Guid("2BB47770-EB08-4530-A72E-2A620AF93E95")]
public enum swCosmeticThreadType_e : System.Enum 
```

```

public enum swCosmeticThreadType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2BB47770-EB08-4530-A72E-2A620AF93E95")
public enum swCosmeticThreadType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2BB47770-EB08-4530-A72E-2A620AF93E95")]
__value public enum swCosmeticThreadType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2BB47770-EB08-4530-A72E-2A620AF93E95")]
public enum class swCosmeticThreadType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swApplyCosmeticThread\_Blind** | 0 = Runs the thread for a specified distance |
| **swApplyCosmeticThread\_ThroughFeature** | 2 = Runs the thread through the object |
| **swApplyCosmeticThread\_UpToNext** | 1 = Runs the thread to the next face |

Remarks

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCosmeticThreadType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
