# Select Method (ISplineHandle)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Select`

Selects a spline handle.
Selects a spline handle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select( _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISplineHandle
Dim AppendFlag As System.Boolean
Dim value As System.Boolean
 
value = instance.Select(AppendFlag)
```

```

System.bool Select( 
   System.bool AppendFlag
)
```

```

System.bool Select( 
   System.bool AppendFlag
) 
```

#### Parameters

*AppendFlag*
:   True appends the spline handle to the selection list, false replaces the selection list with the spline handle

#### Return Value

True if the spline handle is selected, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md)  
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.md)
