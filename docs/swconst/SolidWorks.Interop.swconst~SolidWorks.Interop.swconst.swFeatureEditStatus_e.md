# swFeatureEditStatus_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureEditStatus_e`

Editing status of feature. Bitmask.
Editing status of feature. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("3D91DCB2-718B-4B7A-8C94-26962C0DB210")>
Public Enum swFeatureEditStatus_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFeatureEditStatus_e
```

```

[System.Runtime.InteropServices.Guid("3D91DCB2-718B-4B7A-8C94-26962C0DB210")]
public enum swFeatureEditStatus_e : System.Enum 
```

```

public enum swFeatureEditStatus_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("3D91DCB2-718B-4B7A-8C94-26962C0DB210")
public enum swFeatureEditStatus_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("3D91DCB2-718B-4B7A-8C94-26962C0DB210")]
__value public enum swFeatureEditStatus_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("3D91DCB2-718B-4B7A-8C94-26962C0DB210")]
public enum class swFeatureEditStatus_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFeature\_Editable** | 0 or 0x0; Feature can be edited |
| **swFeature\_NonEditable** | 1 or 0x1; Feature cannot be edited |
| **swFeature\_UnderEditing** | 2 or 0x2; If the feature is a sketch, then the sketch is already being edited |

Remarks

Although swFeatureEditStatus\_e is a bitmask, you currently cannot combine its mutually exclusive enumerators.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFeatureEditStatus\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
