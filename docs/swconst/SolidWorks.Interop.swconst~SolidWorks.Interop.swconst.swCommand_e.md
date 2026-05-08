# swCommand_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCommand_e`

Dialog or file to display.
Dialog or file to display.

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

<System.Runtime.InteropServices.GuidAttribute("E20CC132-C933-4765-A9FD-80E987D43E0D")>
Public Enum swCommand_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCommand_e
```

```

[System.Runtime.InteropServices.Guid("E20CC132-C933-4765-A9FD-80E987D43E0D")]
public enum swCommand_e : System.Enum 
```

```

public enum swCommand_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("E20CC132-C933-4765-A9FD-80E987D43E0D")
public enum swCommand_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("E20CC132-C933-4765-A9FD-80E987D43E0D")]
__value public enum swCommand_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("E20CC132-C933-4765-A9FD-80E987D43E0D")]
public enum class swCommand_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCurrentTipOfDayString** | 8 |
| **swFileNew** | 1 = Display the File, New dialog |
| **swFileOpen** | 0 = Display the File, Open dialog |
| **swFontSize** | 10 = Reserved; not in use |
| **swInterfaceBrightnessTheme** | 11 = Get current user-interface brightness theme |
| **swNextTipOfDayString** | 7 |
| **swOpenHTMLHelp** | 3 = Given the path and compiled HTML filename (has **.chm** file name extension), this option opens the HTML Help file in a new window; if no path is given, the current language folder below the folder in which **sldworks.exe** exists is used |
| **swOpenRecentFile** | 2 = Given a number between ID\_FILE\_MRU\_FILE1 and ID\_FILE\_MRU\_FILE1 + 9, this option opens the matching file from the list of most recently used files |
| **swPrevTipOfDayString** | 9 |
| **swReserved** | 4 = Reserved; not in use |
| **swUserExperienceLevel** | 6 = User experience level: new user, existing user to this revision, or existing user but new to this revision |
| **swVerticalMkt** | 5 = Current vertical market user-interface sett |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCommand\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
