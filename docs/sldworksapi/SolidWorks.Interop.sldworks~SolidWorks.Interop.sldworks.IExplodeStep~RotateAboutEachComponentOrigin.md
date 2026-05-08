# RotateAboutEachComponentOrigin Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotateAboutEachComponentOrigin`

Gets or sets whether components rotate about their origins in this regular explode step.
Gets or sets whether components rotate about their origins in this regular explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RotateAboutEachComponentOrigin As System.Boolean
```

```

Dim instance As IExplodeStep
Dim value As System.Boolean
 
instance.RotateAboutEachComponentOrigin = value
 
value = instance.RotateAboutEachComponentOrigin
```

```

System.bool RotateAboutEachComponentOrigin {get; set;}
```

```

property System.bool RotateAboutEachComponentOrigin {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if components rotate about their origins, false if not

Remarks

If [IExplodeStep::AutoSpaceComponentsOnDrag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~AutoSpaceComponentsOnDrag.md) is set to true, then this property is automatically false.

This property is valid only if [IExplodeStep::ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.md) is set to [swAssemblyExplodeStepType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html).swAssemblyExplodeStepType\_Translate.

If this property is set to true, then the rotation axis is automatically populated.

Example

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)
