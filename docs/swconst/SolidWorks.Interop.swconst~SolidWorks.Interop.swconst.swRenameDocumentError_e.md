# swRenameDocumentError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRenameDocumentError_e`

Rename components errors.
Rename components errors.

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

<System.Runtime.InteropServices.GuidAttribute("3D3BBCD3-4864-4ADD-ACD2-6BE8D9C91BEC")>
Public Enum swRenameDocumentError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRenameDocumentError_e
```

```

[System.Runtime.InteropServices.Guid("3D3BBCD3-4864-4ADD-ACD2-6BE8D9C91BEC")]
public enum swRenameDocumentError_e : System.Enum 
```

```

public enum swRenameDocumentError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("3D3BBCD3-4864-4ADD-ACD2-6BE8D9C91BEC")
public enum swRenameDocumentError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("3D3BBCD3-4864-4ADD-ACD2-6BE8D9C91BEC")]
__value public enum swRenameDocumentError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("3D3BBCD3-4864-4ADD-ACD2-6BE8D9C91BEC")]
public enum class swRenameDocumentError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swRenameDocumentError\_ComponentNotResolved** | 5 = You must resolve the component before attempting to rename it |
| **swRenameDocumentError\_DocumentNameInUse** | 12 = You cannot rename the component to the specified name because a document with that name is open |
| **swRenameDocumentError\_DocumentNotSaved** | 15 = You cannot rename the document, and the document was not saved |
| **swRenameDocumentError\_FileAlreadyExists** | 8 = You cannot rename the component to the specified name because a file with that name exists on disk |
| **swRenameDocumentError\_InvalidCharactersInName** | 9 = You specified an invalid component name; the name is either too long or contains invalid characters |
| **swRenameDocumentError\_InvalidForDrawings** | 3 = You cannot rename drawing documents |
| **swRenameDocumentError\_InvalidSelection** | 2 = You must select a valid component; your selection is invalid for renaming |
| **swRenameDocumentError\_InvalidVirtualComponent** | 10 = You cannot rename virtual components |
| **swRenameDocumentError\_LightWeightComponent** | 6 = You cannot rename the child component whose parent component is lightweight |
| **swRenameDocumentError\_NameTooLong** | 11 = You cannot rename the component to the specified name because that name is too long |
| **swRenameDocumentError\_NoModelLoaded** | 4 = You cannot rename the component because a model is not loaded in memory |
| **swRenameDocumentError\_None** | 0 = Success |
| **swRenameDocumentError\_NotAllowedWithPDM** | 17 = You cannot rename the component because the SOLIDWORKS Professional PDM add-in is not loaded |
| **swRenameDocumentError\_PatternedComponent** | 19 = You cannot rename patterned components |
| **swRenameDocumentError\_PendingNameAlreadyInUse** | 13 = You cannot rename the component to the specified name because a document with the same name has been temporarily renamed but not yet saved |
| **swRenameDocumentError\_ReadOnlyDocument** | 14 = You cannot rename read-only documents or documents referenced by read-only documents |
| **swRenameDocumentError\_RoutingComponent** | 7 = You cannot rename routing components |
| **swRenameDocumentError\_ToolboxComponent** | 18 = You cannot rename Toolbox components |
| **swRenameDocumentError\_UnspecifiedInternalError** | 1 = You cannot rename the component due to an internal error |
| **swRenameDocumentError\_VirtualComponent** | 16 = You cannot rename virtual components |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRenameDocumentError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
