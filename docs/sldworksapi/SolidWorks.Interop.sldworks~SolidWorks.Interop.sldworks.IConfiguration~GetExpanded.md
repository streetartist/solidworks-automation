# GetExpanded Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetExpanded`

Gets whether this configuration's node is expanded in the specified pane of the ConfigurationManager.
Gets whether this configuration's node is expanded in the specified pane of the ConfigurationManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExpanded( _
   ByVal WhichPane As System.Integer _
) As System.Boolean
```

```

Dim instance As IConfiguration
Dim WhichPane As System.Integer
Dim value As System.Boolean
 
value = instance.GetExpanded(WhichPane)
```

```

System.bool GetExpanded( 
   System.int WhichPane
)
```

```

System.bool GetExpanded( 
   System.int WhichPane
) 
```

#### Parameters

*WhichPane*
:   Valid options in [swFeatMgrPane\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatMgrPane_e.html):

    - swFeatMgrPaneTop
    - swFeatMgrPaneBottom

#### Return Value

True if node is expanded, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::SetExpanded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetExpanded.md)
