# DisplayStateSpecMaterialPropertyValues Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues`

Gets and sets the appearance settings for the specified display state setting.
Gets and sets the appearance settings for the specified display state setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayStateSpecMaterialPropertyValues( _
   ByVal Setting As DisplayStateSetting _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Setting As DisplayStateSetting
Dim value As System.Object
 
instance.DisplayStateSpecMaterialPropertyValues(Setting) = value
 
value = instance.DisplayStateSpecMaterialPropertyValues(Setting)
```

```

System.object DisplayStateSpecMaterialPropertyValues( 
   DisplayStateSetting Setting
) {get; set;}
```

```

property System.Object^ DisplayStateSpecMaterialPropertyValues {
   System.Object^ get(DisplayStateSetting^ Setting);
   void set (DisplayStateSetting^ Setting, System.Object^ value);
}
```

#### Parameters

*Setting*
:   [IDisplayStateSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.md) (see **Remarks**)

#### Property Value

One-dimensional array of [IAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md)s (see **Remarks**)

Remarks

Before using this method to get or set appearance settings:

1. Call [IModelDocExtension::GetDisplayStateSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDisplayStateSetting.md) to obtain an [IDisplayStateSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.md) object.
2. Call [IDisplayStateSetting::Names](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Names.md) or [IDisplayStateSetting::ISetNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetNames.md) to specify the display states.
3. Call [IDisplayStateSetting::Entities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Entities.md) or [IDisplayStateSetting::ISetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetEntities.md) to specify the components.
4. Call [IDisplayStateSetting::Option](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Option.md) to specify the display state scope of the setting.
5. Specify the Setting parameter using the IDisplayStateSetting object.

Each [IAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md) in the array returned by this method maps to a component in a display state. The size of the returned array is ([IDisplayStateSetting::GetEntityCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~GetEntityCount.md) \* [IDisplayStateSetting::GetNameCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~GetNameCount.md)).

The returned array stores appearance settings (AS) for N components in M display states as follows:

> Component1 DisplayState1 AS, Component1 DisplayState2 AS, ..., Component1 DisplayStateM AS,
>
> Component2 DisplayState1 AS, Component2 DisplayState2 AS, ..., Component2 DisplayStateM AS,
>
> ...
>
> ComponentN DisplayState1 AS, ComponentN DisplayState2 AS, ..., ComponentN DisplayStateM AS

Before using this method to set appearance settings:

1. Perform steps1-5 as described above.
2. Call [IModelDocExtension::GetAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAppearanceSetting.md) to obtain an [IAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md) object.
3. Set the properties in the IAppearanceSetting object for the component in the display state.
4. Repeat steps 2 and 3 for each component in each display state.
5. Create an array of the IAppearanceSetting objects in the order described above.

Example

[Change Color of Component in Specific Display State (C#)](Change_Color_of_Component_in_Specific_Display_State_Example_CSharp.htm)  
[Change Color of Component in Specific Display State (VB.NET)](Change_Color_of_Component_in_Specific_Display_State_Example_VBNET.htm)  
[Change Color of Component in Specific Display State (VBA)](Change_Color_of_Component_in_Specific_Display_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::DisplayMode Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayMode.md)  
[IModelDocExtension::Transparency Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Transparency.md)  
[IModelDocExtension::Visibility Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Visibility.md)
