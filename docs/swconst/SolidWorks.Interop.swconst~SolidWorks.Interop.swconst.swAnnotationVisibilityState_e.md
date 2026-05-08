# swAnnotationVisibilityState_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAnnotationVisibilityState_e`

Annotation visibility states.
Annotation visibility states.

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

<System.Runtime.InteropServices.GuidAttribute("8179D388-1B75-4DF2-A370-4825F025F92C")>
Public Enum swAnnotationVisibilityState_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAnnotationVisibilityState_e
```

```

[System.Runtime.InteropServices.Guid("8179D388-1B75-4DF2-A370-4825F025F92C")]
public enum swAnnotationVisibilityState_e : System.Enum 
```

```

public enum swAnnotationVisibilityState_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("8179D388-1B75-4DF2-A370-4825F025F92C")
public enum swAnnotationVisibilityState_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("8179D388-1B75-4DF2-A370-4825F025F92C")]
__value public enum swAnnotationVisibilityState_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("8179D388-1B75-4DF2-A370-4825F025F92C")]
public enum class swAnnotationVisibilityState_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAnnotationHalfHidden** | 2 = Annotation is half-hidden (grayed out) or hidden depending on the interactive user's actions. For example, if the annotation's visibility is set to swAnnotationHalfHidden by [IAnnotation::Visible](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Visible.html), then that annotation is in a half-hidden state, which is not a permanent state. During a Hide/Show Annotations operation in a drawing, a half-hidden annotation is displayed in gray if the interactive user selects to show all annotations. Any annotation set to swAnnotationHalfHidden is hidden when the interactive user finishes using Hide/Show Annotations. |
| **swAnnotationHidden** | 3 = Annotation is hidden |
| **swAnnotationVisibilityUnknown** | 0 = Annotation visibility is not known |
| **swAnnotationVisible** | 1 = Annotation is visible |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAnnotationVisibilityState\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
