# GetNumberOfPartExplodeSteps Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetNumberOfPartExplodeSteps`

Gets the number of explode steps in the explode view of a multibody part.
Gets the number of explode steps in the explode view of a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNumberOfPartExplodeSteps() As System.Integer
```

```

Dim instance As IConfiguration
Dim value As System.Integer
 
value = instance.GetNumberOfPartExplodeSteps()
```

```

System.int GetNumberOfPartExplodeSteps()
```

```

System.int GetNumberOfPartExplodeSteps(); 
```

#### Return Value

Number of explode steps

Remarks

This method is valid only for the active configuration.

Before calling this method, call [IPartDoc::ShowExploded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.md) to activate the explode view of interest.

Call this method before calling [IConfiguration::GetPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetPartExplodeStep.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::AddPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddPartExplodeStep.md)  
[IConfiguration::GetCurrentPartExplodeViewName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCurrentPartExplodeViewName.md)
