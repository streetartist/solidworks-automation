# GetPartExplodeStep Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetPartExplodeStep`

Gets the specified explode step of an explode view of a multibody part.
Gets the specified explode step of an explode view of a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPartExplodeStep( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IConfiguration
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetPartExplodeStep(Index)
```

```

System.object GetPartExplodeStep( 
   System.int Index
)
```

```

System.Object^ GetPartExplodeStep( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the explode step (see **Remarks**)

#### Return Value

[IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md)

Remarks

This method is valid only for the active configuration.

Before calling this method, call [IPartDoc::ShowExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.md) to activate the explode view of interest.

To specify Index, call [IConfiguration::GetNumberOfPartExplodeSteps](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfPartExplodeSteps.md) to get the number of explode steps in the explode view.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::AddPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddPartExplodeStep.md)  
[IConfiguration::DeleteExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteExplodeStep.md)  
[IConfiguration::GetCurrentPartExplodeViewName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCurrentPartExplodeViewName.md)
