# DeleteExplodeStep Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep`

Deletes the specified explode step.
Deletes the specified explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteExplodeStep( _
   ByVal ExplodeStepName As System.String _
) As System.Boolean
```

```

Dim instance As IConfiguration
Dim ExplodeStepName As System.String
Dim value As System.Boolean
 
value = instance.DeleteExplodeStep(ExplodeStepName)
```

```

System.bool DeleteExplodeStep( 
   System.string ExplodeStepName
)
```

```

System.bool DeleteExplodeStep( 
   System.String^ ExplodeStepName
) 
```

#### Parameters

*ExplodeStepName*
:   Name of the explode step to delete

#### Return Value

True if the explode step was deleted successfully, false if not

Remarks

This method is valid only for the active configuration.

Example

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::AddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep.md)  
[IConfiguration::IAddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IAddExplodeStep.md)  
[IConfiguration::GetExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExplodeStep.md)  
[IConfiguration::GetNumberOfExplodeSteps Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfExplodeSteps.md)  
[IConfiguration::IGetExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetExplodeStep.md)  
[IConfiguration::AddRadialExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRadialExplodeStep.md)  
[IConfiguration::AddPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddPartExplodeStep.md)  
[IConfiguration::GetPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetPartExplodeStep.md)
