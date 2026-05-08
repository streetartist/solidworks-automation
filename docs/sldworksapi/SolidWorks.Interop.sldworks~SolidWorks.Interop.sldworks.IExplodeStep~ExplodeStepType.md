# ExplodeStepType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType`

Gets the type of this explode step.
Gets the type of this explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ExplodeStepType As System.Integer
```

```

Dim instance As IExplodeStep
Dim value As System.Integer
 
value = instance.ExplodeStepType
```

```

System.int ExplodeStepType {get;}
```

```

property System.int ExplodeStepType {
   System.int get();
}
```

#### Property Value

Explode step type as defined in [swAssemblyExplodeStepType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html)

Example

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)  
[IExplodeStep::DivergeDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeDirection.md)  
[IExplodeStep::DivergeFromAxis Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~DivergeFromAxis.md)  
[IExplodeStep::ReverseRotationDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ReverseRotationDirection.md)  
[IExplodeStep::ReverseTranslationDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ReverseTranslationDirection.md)  
[IExplodeStep::RotateAboutEachComponentOrigin Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotateAboutEachComponentOrigin.md)  
[IExplodeStep::RotationAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotationAngle.md)
