# Command Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Command`

Opens the specified dialog or file.
Opens the specified dialog or file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Command( _
   ByVal Command As System.Integer, _
   ByVal Args As System.Object _
) As System.Object
```

```

Dim instance As ISldWorks
Dim Command As System.Integer
Dim Args As System.Object
Dim value As System.Object
 
value = instance.Command(Command, Args)
```

```

System.object Command( 
   System.int Command,
   System.object Args
)
```

```

System.Object^ Command( 
   System.int Command,
   System.Object^ Args
) 
```

#### Parameters

*Command*
:   Command as defined by [swCommand\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommand_e.html)

*Args*
:   See Remarks

Remarks

|  |  |
| --- | --- |
| **If command specified is...** | **Then pass...** |
| swOpenHTMLHelp | Path and filename for the compiled HTML file (has .chm filename extension) |
| - swFileOpen - swFileNew - swOpenRecentFile | Empty VARIANT; for example:   VARIANT args;   V\_VT(&args) = VT\_EMPTY;   // Call Command API and open the File, Open dialog   swApp->Command(0, args, &retval); |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
