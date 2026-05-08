# IGetExplodeStep Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetExplodeStep`

Gets a pointer to the specified explode step in the configuration explode step sequence.
Gets a pointer to the specified explode step in the configuration explode step sequence.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetExplodeStep( _
   ByVal ExplodeStepIndex As System.Integer _
) As ExplodeStep
```

```

Dim instance As IConfiguration
Dim ExplodeStepIndex As System.Integer
Dim value As ExplodeStep
 
value = instance.IGetExplodeStep(ExplodeStepIndex)
```

```

ExplodeStep IGetExplodeStep( 
   System.int ExplodeStepIndex
)
```

```

ExplodeStep^ IGetExplodeStep( 
   System.int ExplodeStepIndex
) 
```

#### Parameters

*ExplodeStepIndex*
:   Index number of the explode step in the explode step sequence

#### Return Value

Pointer to the [explode step](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)

Remarks

Before calling this method, call [IConfiguration::GetNumberOfExplodeSteps](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfExplodeSteps.md) to get the number of explode steps in the sequence.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::AddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep.md)  
[IConfiguration::DeleteExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.md)  
[IConfiguration::GetExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExplodeStep.md)  
[IConfiguration::IAddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IAddExplodeStep.md)
