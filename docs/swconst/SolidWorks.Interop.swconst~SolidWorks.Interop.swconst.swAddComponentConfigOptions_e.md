# swAddComponentConfigOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddComponentConfigOptions_e`

Options for adding components to an assembly.
Options for adding components to an assembly.

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

<System.Runtime.InteropServices.GuidAttribute("F6CD5E03-2756-4A0F-BC99-9A2872F01E0D")>
Public Enum swAddComponentConfigOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAddComponentConfigOptions_e
```

```

[System.Runtime.InteropServices.Guid("F6CD5E03-2756-4A0F-BC99-9A2872F01E0D")]
public enum swAddComponentConfigOptions_e : System.Enum 
```

```

public enum swAddComponentConfigOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F6CD5E03-2756-4A0F-BC99-9A2872F01E0D")
public enum swAddComponentConfigOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F6CD5E03-2756-4A0F-BC99-9A2872F01E0D")]
__value public enum swAddComponentConfigOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F6CD5E03-2756-4A0F-BC99-9A2872F01E0D")]
public enum class swAddComponentConfigOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAddComponentConfigOptions\_CurrentSelectedConfig** | 0 = Add a part or assembly in its last saved configuration.  (See [IAssemblyDoc::AddComponent5](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddComponent5.html)) |
| **swAddComponentConfigOptions\_NewConfigWithAllReferenceModels** | 1 = Add an assembly with all of its components resolved.  (See IAssemblyDoc::AddComponent5) |
| **swAddComponentConfigOptions\_NewConfigWithAsmStructure** | 2 = Add an assembly with all of its components suppressed.  (See IAssemblyDoc::AddComponent5) |

Example

[Add Component and Mate (VBA)](ms-help://SolidWorks.Interop.sldworks/SolidWorks/Add_Component_and_Mate_Example_VB.htm)  
[Add Component and Mate (VB.NET)](ms-help://SolidWorks.Interop.sldworks/SolidWorks/Add_Component_and_Mate_Example_VBNET.htm)  
[Add Component and Mate (C#)](ms-help://SolidWorks.Interop.sldworks/SolidWorks/Add_Component_and_Mate_Example_CSharp.htm)

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAddComponentConfigOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
