# swAppearanceTargetType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppearanceTargetType_e`

Types of targets to which to apply a copied appearance.
Types of targets to which to apply a copied appearance.

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

<System.Runtime.InteropServices.GuidAttribute("7C113CE3-DC6E-4BF4-9DF6-86C0F1A9C138")>
Public Enum swAppearanceTargetType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAppearanceTargetType_e
```

```

[System.Runtime.InteropServices.Guid("7C113CE3-DC6E-4BF4-9DF6-86C0F1A9C138")]
public enum swAppearanceTargetType_e : System.Enum 
```

```

public enum swAppearanceTargetType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("7C113CE3-DC6E-4BF4-9DF6-86C0F1A9C138")
public enum swAppearanceTargetType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("7C113CE3-DC6E-4BF4-9DF6-86C0F1A9C138")]
__value public enum swAppearanceTargetType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("7C113CE3-DC6E-4BF4-9DF6-86C0F1A9C138")]
public enum class swAppearanceTargetType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAppearanceTargetAppearanceFilter** | 5 = All appearances in the model that match the appearance of the selected face are applied the copied appearance |
| **swAppearanceTargetBody** | 2 = The body of the selected face is applied the copied appearance |
| **swAppearanceTargetComponent** | 4 = The component of the selected face is applied the copied appearance |
| **swAppearanceTargetFace** | 0 = The selected face is applied the copied appearance |
| **swAppearanceTargetFeature** | 1 = The feature of the selected face is applied the copied appearance |
| **swAppearanceTargetPart** | 3 = The part of the selected face is applied the copied appearance |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAppearanceTargetType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
