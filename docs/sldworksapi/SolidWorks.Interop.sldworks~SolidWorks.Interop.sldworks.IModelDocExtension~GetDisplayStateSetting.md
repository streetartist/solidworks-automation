# GetDisplayStateSetting Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDisplayStateSetting`

Gets the display state setting for the specified scope.
Gets the display state setting for the specified scope.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayStateSetting( _
   ByVal Option As System.Integer _
) As DisplayStateSetting
```

```

Dim instance As IModelDocExtension
Dim Option As System.Integer
Dim value As DisplayStateSetting
 
value = instance.GetDisplayStateSetting(Option)
```

```

DisplayStateSetting GetDisplayStateSetting( 
   System.int Option
)
```

```

DisplayStateSetting^ GetDisplayStateSetting( 
   System.int Option
) 
```

#### Parameters

*Option*
:   Scope of the display state setting as defined in [swDisplayStateOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayStateOpts_e.html)

#### Return Value

[IDisplayStateSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.md)

Remarks

After calling this method:

1. Call [IDisplayStateSetting::Names](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Names.md) or [IDisplayStateSetting::ISetNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetNames.md) to specify the display states.
2. Call [IDisplayStateSetting::Entities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Entities.md) or [IDisplayStateSetting::ISetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetEntities.md) to specify the components.
3. Get or set one or more of the following properties for the specified display states, components, and scope:

   - [IModelDocExtension::DisplayMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayMode.md)
   - [IModelDocExtension::Transparency](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Transparency.md)
   - [IModelDocExtension::Visibility](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Visibility.md)
4. Call [IModelDocExtension::GetAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAppearanceSetting.md) to obtain the [IAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md) object.
5. Set the properties in the IAppearanceSetting object.
6. Get or set the material properties for the specified display states, components, and scope using [IModelDocExtension::DisplayStateSpecMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.md).

Example

[Get Display State Settings (VBA)](Get_Display_State_Settings_Example_VB.htm)  
[Get Display State Settings (VB.NET)](Get_Display_State_Settings_VBNET.htm)  
[Get Display State Settings (C#)](Get_Display_State_Settings_CSharp.htm)  
[Change Color of Component in Specific Display State (C#)](Change_Color_of_Component_in_Specific_Display_State_Example_CSharp.htm)  
[Change Color of Component in Specific Display State (VB.NET)](Change_Color_of_Component_in_Specific_Display_State_Example_VBNET.htm)  
[Change Color of Component in Specific Display State (VBA)](Change_Color_of_Component_in_Specific_Display_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
