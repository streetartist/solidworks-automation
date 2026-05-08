# SetExpanded Method (IConfigurationManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetExpanded`

Sets whether to display and expand all of the configuration nodes in the specified pane of the ConfigurationManager.
Sets whether to display and expand all of the configuration nodes in the specified pane of the ConfigurationManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetExpanded( _
   ByVal WhichPane As System.Integer, _
   ByVal Expand As System.Boolean _
) 
```

```

Dim instance As IConfigurationManager
Dim WhichPane As System.Integer
Dim Expand As System.Boolean
 
instance.SetExpanded(WhichPane, Expand)
```

```

void SetExpanded( 
   System.int WhichPane,
   System.bool Expand
)
```

```

void SetExpanded( 
   System.int WhichPane,
   System.bool Expand
) 
```

#### Parameters

*WhichPane*
:   Display pane as defined in [swFeatMgrPane\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatMgrPane_e.html):

    - swFeatMgrPaneTop
    - swFeatMgrPaneBottom

*Expand*
:   True to expand all of the nodes, false to collapse them

Example

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)  
[IConfiguration::SetExpanded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetExpanded.md)
