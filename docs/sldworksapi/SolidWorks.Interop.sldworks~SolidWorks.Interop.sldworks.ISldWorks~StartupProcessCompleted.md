# StartupProcessCompleted Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~StartupProcessCompleted`

Gets whether the SOLIDWORKS startup process, including loading all startup add-ins, has completed.
Gets whether the SOLIDWORKS startup process, including loading all startup add-ins, has completed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property StartupProcessCompleted As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
value = instance.StartupProcessCompleted
```

```

System.bool StartupProcessCompleted {get;}
```

```

property System.bool StartupProcessCompleted {
   System.bool get();
}
```

#### Property Value

True if the SOLIDWORKS startup process, including loading all startup add-ins, has completed, false if not (see **Remarks**)

Remarks

Use this property in out-of-process add-in applications to ensure that SOLIDWORKS, including loading all startup add-ins, is ready to receive additional API calls. For example, call this property before calling [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) in an out-of-process add-in application.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
