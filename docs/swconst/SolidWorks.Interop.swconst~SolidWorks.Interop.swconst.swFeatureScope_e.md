# swFeatureScope_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureScope_e`

Feature scope options.
Feature scope options.

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

<System.Runtime.InteropServices.GuidAttribute("9A862944-510B-4433-A0DB-7AA29EE5CA57")>
Public Enum swFeatureScope_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFeatureScope_e
```

```

[System.Runtime.InteropServices.Guid("9A862944-510B-4433-A0DB-7AA29EE5CA57")]
public enum swFeatureScope_e : System.Enum 
```

```

public enum swFeatureScope_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("9A862944-510B-4433-A0DB-7AA29EE5CA57")
public enum swFeatureScope_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("9A862944-510B-4433-A0DB-7AA29EE5CA57")]
__value public enum swFeatureScope_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("9A862944-510B-4433-A0DB-7AA29EE5CA57")]
public enum class swFeatureScope_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFeatureScope\_AllBodies** | 0 = All of the bodies in the multibody part are affected by the Mirror feature. |
| **swFeatureScope\_SelectedBodiesWithAutoSelect** | 1 = Only the specified bodies in the multibody part are affected by the Mirror feature when AutoSelect is true. |
| **swFeatureScope\_SelectedBodiesWithOutAutoSelect** | 2 = Only the specified bodies in the multibody part are affected by the Mirror feature when AutoSelect is false. |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFeatureScope\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
