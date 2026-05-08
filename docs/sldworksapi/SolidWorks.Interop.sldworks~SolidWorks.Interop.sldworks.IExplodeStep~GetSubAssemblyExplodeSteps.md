# GetSubAssemblyExplodeSteps Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetSubAssemblyExplodeSteps`

Gets the explode steps of this subassembly explode step.
Gets the explode steps of this subassembly explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSubAssemblyExplodeSteps() As System.Object
```

```

Dim instance As IExplodeStep
Dim value As System.Object
 
value = instance.GetSubAssemblyExplodeSteps()
```

```

System.object GetSubAssemblyExplodeSteps()
```

```

System.Object^ GetSubAssemblyExplodeSteps(); 
```

#### Return Value

Array of [IExplodeSteps](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) in the subassembly explode view

Remarks

A subassembly explode step is created when you click **Reuse Subassembly Explode** on the Explode PropertyManager. This method retrieves the nested explode steps of the subassembly.

This method is valid only if [IExplodeStep::ExplodeStepType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~ExplodeStepType.md) returns [swAssemblyExplodeStepType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyExplodeStepType.html).swAssemblyExplodeStepType\_SubAssembly.

Example

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)
