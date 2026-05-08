# SetExpanded Method (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetExpanded`

Sets whether to expand this configuration's node in the specified pane of the ConfigurationManager.
Sets whether to expand this configuration's node in the specified pane of the ConfigurationManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetExpanded( _
   ByVal WhichPane As System.Integer, _
   ByVal Expanded As System.Boolean _
) 
```

```

Dim instance As IConfiguration
Dim WhichPane As System.Integer
Dim Expanded As System.Boolean
 
instance.SetExpanded(WhichPane, Expanded)
```

```

void SetExpanded( 
   System.int WhichPane,
   System.bool Expanded
)
```

```

void SetExpanded( 
   System.int WhichPane,
   System.bool Expanded
) 
```

#### Parameters

*WhichPane*
:   Display pane as defined in [swFeatMgrPane\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatMgrPane_e.html):

    - swFeatMgrPaneTop
    - swFeatMgrPaneBottom

*Expanded*
:   True to expand the node, false to collapse it

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::GetExpanded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExpanded.md)  
[IConfigurationManager::SetExpanded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetExpanded.md)
