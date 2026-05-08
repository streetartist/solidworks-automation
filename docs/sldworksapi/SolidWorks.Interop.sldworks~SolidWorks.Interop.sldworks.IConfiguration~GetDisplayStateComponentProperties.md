# GetDisplayStateComponentProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentProperties`

Gets the components and their material properties in the specified display state.
Gets the components and their material properties in the specified display state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayStateComponentProperties( _
   ByVal DisplayStateName As System.String, _
   ByRef Components As System.Object _
) As System.Object
```

```

Dim instance As IConfiguration
Dim DisplayStateName As System.String
Dim Components As System.Object
Dim value As System.Object
 
value = instance.GetDisplayStateComponentProperties(DisplayStateName, Components)
```

```

System.object GetDisplayStateComponentProperties( 
   System.string DisplayStateName,
   out System.object Components
)
```

```

System.Object^ GetDisplayStateComponentProperties( 
   System.String^ DisplayStateName,
   [Out] System.Object^ Components
) 
```

#### Parameters

*DisplayStateName*
:   Name of the display state

*Components*
:   Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)s

#### Return Value

Array of component properties (see **Remarks**)

Remarks

The material values returned include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid values are from 0 to 1 for all variables.

If the return value is all -1 values, then material property values are not assigned to the feature.

The format of the return value is an array of doubles as follows:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::GetDisplayStateBodyProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateBodyProperties.md)  
[IConfiguration::GetDisplayStateComponentVisibility Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentVisibility.md)  
[IConfiguration::GetDisplayStateFaceProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFaceProperties.md)  
[IConfiguration::GetDisplayStateFeatureProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFeatureProperties.md)  
[IConfiguration::GetDisplayStateProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateProperties.md)  
[IConfiguration::GetDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.md)  
[IConfiguration::GetDisplayStatesCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.md)
