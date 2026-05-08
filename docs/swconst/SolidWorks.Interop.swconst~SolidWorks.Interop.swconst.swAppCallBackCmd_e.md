# swAppCallBackCmd_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppCallBackCmd_e`

Types of application callback functions.
Types of application callback functions.

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

<System.Runtime.InteropServices.GuidAttribute("1DD0F701-D1D2-4EA4-85BE-C50A3AE7CBB5")>
Public Enum swAppCallBackCmd_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAppCallBackCmd_e
```

```

[System.Runtime.InteropServices.Guid("1DD0F701-D1D2-4EA4-85BE-C50A3AE7CBB5")]
public enum swAppCallBackCmd_e : System.Enum 
```

```

public enum swAppCallBackCmd_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("1DD0F701-D1D2-4EA4-85BE-C50A3AE7CBB5")
public enum swAppCallBackCmd_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("1DD0F701-D1D2-4EA4-85BE-C50A3AE7CBB5")]
__value public enum swAppCallBackCmd_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("1DD0F701-D1D2-4EA4-85BE-C50A3AE7CBB5")]
public enum class swAppCallBackCmd_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAppHelpContext** | 3 = Not used |
| **swAppIsCmdEnabled** | 4 = CommandGroup item is enabled |
| **swAppIsNewCmd** | 1 = True if data is new, false if not |
| **swAppPostNotifyEvent** | 5 = Your application is posting a callback to the SOLIDWORKS message queue that will be invoked when the callback is processed in the SOLIDWORKS message queue |
| **swAppWhatsNewDescription** | 2 = Interactive What's New |

Remarks

Use with [ISldWorks::AddCallback](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddCallback.html).

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAppCallBackCmd\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
