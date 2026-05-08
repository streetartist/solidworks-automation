# Parameter Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Parameter`

Gets value in the parameter space of the curve underlying the spline handle.
Gets value in the parameter space of the curve underlying the spline handle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Parameter As System.Double
```

```

Dim instance As ISplineHandle
Dim value As System.Double
 
value = instance.Parameter
```

```

System.double Parameter {get;}
```

```

property System.double Parameter {
   System.double get();
}
```

#### Property Value

Value in the parameter space of the curve underlying the spline handle

Remarks

There is no user-interface equivalent for this property as it is typically only useful for API client  code.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md)  
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.md)
