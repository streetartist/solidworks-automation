# swFeatureChamferOption_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureChamferOption_e`

Chamfer feature options. Bitmask.
Chamfer feature options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("068E9088-2039-4C30-B005-E26E93096FCC")>
Public Enum swFeatureChamferOption_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFeatureChamferOption_e
```

```

[System.Runtime.InteropServices.Guid("068E9088-2039-4C30-B005-E26E93096FCC")]
public enum swFeatureChamferOption_e : System.Enum 
```

```

public enum swFeatureChamferOption_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("068E9088-2039-4C30-B005-E26E93096FCC")
public enum swFeatureChamferOption_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("068E9088-2039-4C30-B005-E26E93096FCC")]
__value public enum swFeatureChamferOption_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("068E9088-2039-4C30-B005-E26E93096FCC")]
public enum class swFeatureChamferOption_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFeatureChamferFlipDirection** | 1 or 0x1 |
| **swFeatureChamferKeepFeature** | 2 or 0x2 |
| **swFeatureChamferPropagateFeatToParts** | 8 or 0x8 |
| **swFeatureChamferTangentPropagation** | 4 or 0x4 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFeatureChamferOption\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
