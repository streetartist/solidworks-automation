# GetDisplayStateComponentVisibility Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentVisibility`

Gets the components and their visibilities in the specified display state.
Gets the components and their visibilities in the specified display state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayStateComponentVisibility( _
   ByVal DisplayStateName As System.String, _
   ByVal Onlyhidden As System.Boolean, _
   ByVal ToplevelOnly As System.Boolean, _
   ByRef Components As System.Object _
) As System.Object
```

```

Dim instance As IConfiguration
Dim DisplayStateName As System.String
Dim Onlyhidden As System.Boolean
Dim ToplevelOnly As System.Boolean
Dim Components As System.Object
Dim value As System.Object
 
value = instance.GetDisplayStateComponentVisibility(DisplayStateName, Onlyhidden, ToplevelOnly, Components)
```

```

System.object GetDisplayStateComponentVisibility( 
   System.string DisplayStateName,
   System.bool Onlyhidden,
   System.bool ToplevelOnly,
   out System.object Components
)
```

```

System.Object^ GetDisplayStateComponentVisibility( 
   System.String^ DisplayStateName,
   System.bool Onlyhidden,
   System.bool ToplevelOnly,
   [Out] System.Object^ Components
) 
```

#### Parameters

*DisplayStateName*
:   Name of the display state

*Onlyhidden*
:   True to only return visibilities for hidden components, false to return visibilities for all components

*ToplevelOnly*
:   True to get the top-level components only, false to get all components

*Components*
:   Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)s

#### Return Value

Array of longs or integers indicating component visibilities; 1 if visible, 0 if hidden

Example

[Get Display States and Visibilities of Components (C#)](Get_Display_State_Names_and_Visibilites_of_Components_Example_CSharp.htm)  
[Get Display States and Visibilities of Components (VB.NET)](Get_Display_State_Names_and_Visibilites_of_Components_Example_VBNET.htm)  
[Get Display States and Visibilities of Components (VBA)](Get_Display_State_Names_and_Visibilites_of_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::GetDisplayStateBodyProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateBodyProperties.md)  
[IConfiguration::GetDisplayStateComponentProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentProperties.md)  
[IConfiguration::GetDisplayStateFaceProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFaceProperties.md)  
[IConfiguration::GetDisplayStateFeatureProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFeatureProperties.md)  
[IConfiguration::GetDisplayStateProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateProperties.md)  
[IConfiguration::GetDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.md)  
[IConfiguration::GetDisplayStatesCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.md)
