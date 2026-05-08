# swFeatureSuppressionAction_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureSuppressionAction_e`

Feature suppression actions.
Feature suppression actions.

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

<System.Runtime.InteropServices.GuidAttribute("20867024-8F23-466F-BEC3-F2879D5B8BEF")>
Public Enum swFeatureSuppressionAction_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFeatureSuppressionAction_e
```

```

[System.Runtime.InteropServices.Guid("20867024-8F23-466F-BEC3-F2879D5B8BEF")]
public enum swFeatureSuppressionAction_e : System.Enum 
```

```

public enum swFeatureSuppressionAction_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("20867024-8F23-466F-BEC3-F2879D5B8BEF")
public enum swFeatureSuppressionAction_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("20867024-8F23-466F-BEC3-F2879D5B8BEF")]
__value public enum swFeatureSuppressionAction_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("20867024-8F23-466F-BEC3-F2879D5B8BEF")]
public enum class swFeatureSuppressionAction_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSuppressFeature** | 0 = Suppress the feature |
| **swUnSuppressDependent** | 2 = Unsuppress the children of the feature |
| **swUnSuppressFeature** | 1 = Unsuppress the feature |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFeatureSuppressionAction\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
