# swFeatureTreeFolderType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureTreeFolderType_e`

Ways to insert feature folders for selected features or components in the FeatureManager design tree.
Ways to insert feature folders for selected features or components in the FeatureManager design tree.

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

<System.Runtime.InteropServices.GuidAttribute("12E0CCC0-BDB9-4C0F-950C-2AA48D2C312D")>
Public Enum swFeatureTreeFolderType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFeatureTreeFolderType_e
```

```

[System.Runtime.InteropServices.Guid("12E0CCC0-BDB9-4C0F-950C-2AA48D2C312D")]
public enum swFeatureTreeFolderType_e : System.Enum 
```

```

public enum swFeatureTreeFolderType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("12E0CCC0-BDB9-4C0F-950C-2AA48D2C312D")
public enum swFeatureTreeFolderType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("12E0CCC0-BDB9-4C0F-950C-2AA48D2C312D")]
__value public enum swFeatureTreeFolderType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("12E0CCC0-BDB9-4C0F-950C-2AA48D2C312D")]
public enum class swFeatureTreeFolderType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFeatureTreeFolder\_Containing** | 2 = Create and insert a folder to contain the pre-selected features |
| **swFeatureTreeFolder\_EmptyBefore** | 1 = Create and insert an empty folder before the pre-selected features |
| **swFeatureTreeFolder\_Mold** | 3 = Create and insert a Surface Bodies folder containing three folders: Cavity Surface Bodies, Core Surface Bodies, and Parting Surface Bodies for a pre-selected surface feature |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFeatureTreeFolderType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
