# ReverseRotationDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ReverseRotationDirection`

Gets or sets whether to reverse the direction of rotation of components in this regular explode step.
Gets or sets whether to reverse the direction of rotation of components in this regular explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReverseRotationDirection As System.Boolean
```

```

Dim instance As IExplodeStep
Dim value As System.Boolean
 
instance.ReverseRotationDirection = value
 
value = instance.ReverseRotationDirection
```

```

System.bool ReverseRotationDirection {get; set;}
```

```

property System.bool ReverseRotationDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the direction of rotation of components, false to not

Remarks

This property is valid only if [IExplodeStep::ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.md) is set to [swAssemblyExplodeStepType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html).swAssemblyExplodeStepType\_Translate.

Example

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)
