# DivergeFromAxis Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeFromAxis`

Gets or sets whether to move components at an angle from the explode direction of this radial explode step.
Gets or sets whether to move components at an angle from the explode direction of this radial explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DivergeFromAxis As System.Boolean
```

```

Dim instance As IExplodeStep
Dim value As System.Boolean
 
instance.DivergeFromAxis = value
 
value = instance.DivergeFromAxis
```

```

System.bool DivergeFromAxis {get; set;}
```

```

property System.bool DivergeFromAxis {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to move components at an angle from the explode direction, false to not (see **Remarks**)

Remarks

This property is valid only if [IExplodeStep::ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.md) is set to [swAssemblyExplodeStepType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html).swAssemblyExplodeStepType\_Radial.

If you set this property to false, then [IExplodeStep::DivergeDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeDirection.md) is automatically set to nothing or null.

If you want to set this property to true, then you must first set IExplodeStep::DivergeDirection to a valid diverge direction entity.

Example

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)
