# GetExplodeStep Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExplodeStep`

Gets the specified explode step in this configuration's explode step sequence.
Gets the specified explode step in this configuration's explode step sequence.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExplodeStep( _
   ByVal ExplodeStepIndex As System.Integer _
) As System.Object
```

```

Dim instance As IConfiguration
Dim ExplodeStepIndex As System.Integer
Dim value As System.Object
 
value = instance.GetExplodeStep(ExplodeStepIndex)
```

```

System.object GetExplodeStep( 
   System.int ExplodeStepIndex
)
```

```

System.Object^ GetExplodeStep( 
   System.int ExplodeStepIndex
) 
```

#### Parameters

*ExplodeStepIndex*
:   Index of the explode step in the explode step sequence

#### Return Value

[Explode step](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)

Remarks

Before calling this method, call [IConfiguration::GetNumberOfExplodeSteps](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfExplodeSteps.md) to get the number of explode steps in the explode step sequence.

Example

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) examples.

Example

[Get Explode Step (C#)](Get_Explode_Step_Example_CSharp.htm)  
[Get Explode Step (VB.NET)](Get_Explode_Step_Example_VBNET.htm)  
[Get Explode Step (VBA)](Get_Explode_Step_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::AddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep.md)  
[IConfiguration::DeleteExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.md)  
[IConfiguration::IGetExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetExplodeStep.md)  
[IConfiguration::IAddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IAddExplodeStep.md)  
[IConfiguration::AddRadialExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRadialExplodeStep.md)
