# IGetEnvironment Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetEnvironment`

Gets the IEnvironment object.
Gets the [IEnvironment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md) object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEnvironment() As Environment
```

```

Dim instance As ISldWorks
Dim value As Environment
 
value = instance.IGetEnvironment()
```

```

Environment IGetEnvironment()
```

```

Environment^ IGetEnvironment(); 
```

#### Return Value

[IEnvironment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md) object

Remarks

All numeric values returned from the IEnvironment object are relative to a unit text height of 1.0; i.e., if a symbol has a text height of 0.15, then you the numeric values returned by 0.15.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetEnvironment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetEnvironment.md)
