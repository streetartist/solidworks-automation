# VariableType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~VariableType`

Gets the type of specific hole callout variable.
Gets the type of specific hole callout variable.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property VariableType As System.Integer
```

```

Dim instance As ICalloutVariable
Dim value As System.Integer
 
value = instance.VariableType
```

```

System.int VariableType {get;}
```

```

property System.int VariableType {
   System.int get();
}
```

#### Property Value

Type of specific hole callout variable as defined in [swCalloutVariable\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCalloutVariable_e.html)

Remarks

Call [ICalloutVariable::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~Type.md) to get the type of general hole callout variable.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.md)  
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.md)
