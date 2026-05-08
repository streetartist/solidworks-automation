# RotationAngle Property (IExplodeStep)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotationAngle`

Gets or sets the angle of component rotation in this regular or radial explode step.
Gets or sets the angle of component rotation in this regular or radial explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RotationAngle As System.Double
```

```

Dim instance As IExplodeStep
Dim value As System.Double
 
instance.RotationAngle = value
 
value = instance.RotationAngle
```

```

System.double RotationAngle {get; set;}
```

```

property System.double RotationAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Angle in radians of component rotation

Remarks

If [IExplodeStep::AutoSpaceComponentsOnDrag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~AutoSpaceComponentsOnDrag.md) is set to true, then this property is automatically 0.0.

If [IExplodeStep::ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.md) is set to [swAssemblyExplodeStepType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html):

- swAssemblyExplodeStepType\_Radial, then this property sets the degree of rotation of components about their origins.
- swAssemblyExplodeStepType\_Translate, then this property sets the degree of rotation of components about the rotation axis.

Example

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)
