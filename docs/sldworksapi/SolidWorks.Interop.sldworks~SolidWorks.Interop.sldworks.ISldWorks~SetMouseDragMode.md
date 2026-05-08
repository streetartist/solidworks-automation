# SetMouseDragMode Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMouseDragMode`

Sets the command-mouse mode.
Sets the command-mouse mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetMouseDragMode( _
   ByVal Command As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Command As System.Integer
Dim value As System.Boolean
 
value = instance.SetMouseDragMode(Command)
```

```

System.bool SetMouseDragMode( 
   System.int Command
)
```

```

System.bool SetMouseDragMode( 
   System.int Command
) 
```

#### Parameters

*Command*
:   Command mode that you want to check as defined in [swMouseDragMode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseDragMode_e.html)

#### Return Value

True if the specified command mode was set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetMouseDragMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMouseDragMode.md)
