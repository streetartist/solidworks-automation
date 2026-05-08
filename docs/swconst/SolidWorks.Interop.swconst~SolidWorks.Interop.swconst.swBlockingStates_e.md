# swBlockingStates_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBlockingStates_e`

Blocking states.
Blocking states.

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

<System.Runtime.InteropServices.GuidAttribute("0E920426-39BA-4286-B318-285268F09313")>
Public Enum swBlockingStates_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBlockingStates_e
```

```

[System.Runtime.InteropServices.Guid("0E920426-39BA-4286-B318-285268F09313")]
public enum swBlockingStates_e : System.Enum 
```

```

public enum swBlockingStates_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("0E920426-39BA-4286-B318-285268F09313")
public enum swBlockingStates_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("0E920426-39BA-4286-B318-285268F09313")]
__value public enum swBlockingStates_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("0E920426-39BA-4286-B318-285268F09313")]
public enum class swBlockingStates_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swEditorBlock** | 4 = A valid return value for [IModelDoc2::GetBlockingState](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetBlockingState.html), but it is not a valid input for [IModelDoc2::SetBlockingState](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetBlockingState.html); editing or inserting blocks are blocked |
| **swEditSketchAllowExitBlock** | 8 = Block model changes but allow sketching and exiting sketch edit mode |
| **swEditSketchBlock** | 5 = A block is being edited in the drawing |
| **swFullBlock** | 1 = Most actions are blocked; you cannot edit features, add features, change views (rotate, pan, and so on), exit the SOLIDWORKS software, or change a document; however, you can open a document |
| **swModifyBlock** | 2 = Similar to swFullBlock except that view-related (rotate, pan, and so on) operations are not blocked |
| **swNoBlock** | 0 = No actions are blocked |
| **swPartialModifyBlock** | 3 = Similar to swModifyBlock except that you can change documents |
| **swSystemBlock** | 6 = Similar to swFullBlock except that you cannot open a document |
| **swViewOnlyBlock** | 7 = A valid return value for [IModelDoc2::GetBlockingState](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetBlockingState.html) when a document is open in View only/Selective open mode; not a valid input for [IModelDoc2::SetBlockingState](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetBlockingState.html) |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBlockingStates\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
