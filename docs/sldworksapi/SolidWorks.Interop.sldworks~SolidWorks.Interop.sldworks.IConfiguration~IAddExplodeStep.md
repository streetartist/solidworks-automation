# IAddExplodeStep Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IAddExplodeStep`

Adds a new explode step to the configuration.
Adds a new explode step to the configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddExplodeStep( _
   ByVal ExplDist As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal RigidSubassembly As System.Boolean, _
   ByVal ExplodeRelated As System.Boolean _
) As ExplodeStep
```

```

Dim instance As IConfiguration
Dim ExplDist As System.Double
Dim ReverseDir As System.Boolean
Dim RigidSubassembly As System.Boolean
Dim ExplodeRelated As System.Boolean
Dim value As ExplodeStep
 
value = instance.IAddExplodeStep(ExplDist, ReverseDir, RigidSubassembly, ExplodeRelated)
```

```

ExplodeStep IAddExplodeStep( 
   System.double ExplDist,
   System.bool ReverseDir,
   System.bool RigidSubassembly,
   System.bool ExplodeRelated
)
```

```

ExplodeStep^ IAddExplodeStep( 
   System.double ExplDist,
   System.bool ReverseDir,
   System.bool RigidSubassembly,
   System.bool ExplodeRelated
) 
```

#### Parameters

*ExplDist*
:   Explode distance

*ReverseDir*
:   True to reverse the direction of the explode step, false to not

*RigidSubassembly*
:   True to explode entire sub assembly, false to explode just the selected component

*ExplodeRelated*
:   True to explode related components together, false to not

#### Return Value

Pointer to a newly created [explode step](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)

Remarks

Before calling this method, you must select by mark both an edge direction to explode along and a component to move. For example:

boolstatus = Model.Extension.SelectByID2('', 'EDGE', -0.011, 0.06, 0.084, True, 1, Nothing)

boolstatus = Model.Extension.SelectByID2('squarebolt1-1@Assem1', 'COMPONENT', 0, 0, 0, True, 2, Nothing, swSelectOptionDefault)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::AddExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep.md)  
[IConfiguration::DeleteExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.md)  
[IConfiguration::GetExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExplodeStep.md)  
[IConfiguration::GetNumberOfExplodeSteps Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfExplodeSteps.md)  
[IConfiguration::IGetExplodeStep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetExplodeStep.md)
