# AddComponentConfiguration Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponentConfiguration`

Adds a new configuration for the last selected assembly component.
Adds a new configuration for the last selected assembly component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddComponentConfiguration( _
   ByVal Name As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal Options As System.Integer _
) As Configuration
```

```

Dim instance As IAssemblyDoc
Dim Name As System.String
Dim Comment As System.String
Dim AlternateName As System.String
Dim Options As System.Integer
Dim value As Configuration
 
value = instance.AddComponentConfiguration(Name, Comment, AlternateName, Options)
```

```

Configuration AddComponentConfiguration( 
   System.string Name,
   System.string Comment,
   System.string AlternateName,
   System.int Options
)
```

```

Configuration^ AddComponentConfiguration( 
   System.String^ Name,
   System.String^ Comment,
   System.String^ AlternateName,
   System.int Options
) 
```

#### Parameters

*Name*
:   Name of new configuration

*Comment*
:   Comment displayed in Configuration Properties

*AlternateName*
:   Alternate configuration name; used if swConfigOption\_UseAlternateName is set to true (see **Remarks**)

*Options*
:   Combination of one or more BOOLEAN configuration options as defined in [swConfigurationOptions2\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationOptions2_e.html) (see Remarks)

#### Return Value

[IConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)

Remarks

The Options argument can be a combination of any of the following values:

- swConfigOption\_SuppressByDefault True if you want to suppress newly added features and mates in this configuration, false if not
- swConfigOption\_HideByDefault - True if you want newly added components to be hidden, false if not
- swConfigOption\_MinFeatureManager True if you want newly added components to only display their component name in the FeatureManager design tree, false if you want newly added components to display their name and each of their features in the FeatureManager design tree
- swConfigOption\_DontActivate - True if you do not want the new configuration activated, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
