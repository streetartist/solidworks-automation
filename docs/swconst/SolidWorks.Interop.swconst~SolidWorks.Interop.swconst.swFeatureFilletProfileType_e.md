# swFeatureFilletProfileType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureFilletProfileType_e`

Fillet cross-sectional profile shapes.
Fillet cross-sectional profile shapes.

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

<System.Runtime.InteropServices.GuidAttribute("DA2158B3-C923-4657-93CE-063F1459E44E")>
Public Enum swFeatureFilletProfileType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFeatureFilletProfileType_e
```

```

[System.Runtime.InteropServices.Guid("DA2158B3-C923-4657-93CE-063F1459E44E")]
public enum swFeatureFilletProfileType_e : System.Enum 
```

```

public enum swFeatureFilletProfileType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("DA2158B3-C923-4657-93CE-063F1459E44E")
public enum swFeatureFilletProfileType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("DA2158B3-C923-4657-93CE-063F1459E44E")]
__value public enum swFeatureFilletProfileType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("DA2158B3-C923-4657-93CE-063F1459E44E")]
public enum class swFeatureFilletProfileType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFeatureFilletCircular** | 0 = Circular for symmetric fillets; elliptical for asymmetric fillets |
| **swFeatureFilletConicRadius** | 2 = Requires that you set the radius of curvature at the shoulder point along the fillet's cross section |
| **swFeatureFilletConicRho** | 1 = Requires that you set a ratio in the range [0.5, 0.95] which indicates the weight of the cross-section |
| **swFeatureFilletConicRhoZeroChamfer** | 3 = Chamfer cross section |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFeatureFilletProfileType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
