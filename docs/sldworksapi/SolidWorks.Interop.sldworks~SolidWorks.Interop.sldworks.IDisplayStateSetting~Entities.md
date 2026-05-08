# Entities Property (IDisplayStateSetting)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Entities`

Gets and sets the entities for this display state setting.
Gets and sets the entities for this display state setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Entities As System.Object
```

```

Dim instance As IDisplayStateSetting
Dim value As System.Object
 
instance.Entities = value
 
value = instance.Entities
```

```

System.object Entities {get; set;}
```

```

property System.Object^ Entities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of entities

Remarks

After calling this method:

1. Call [IDisplayStateSetting::Names](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Names.md) to specify the display states.
2. Call [IDisplayStateSetting::Option](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Option.md) to specify the display state scope of the setting.
3. Get or set one or more of the following properties for the specified display states, entities, and scope:

   - [IModelDocExtension::DisplayMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayMode.md)
   - [IModelDocExtension::Transparency](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Transparency.md)
   - [IModelDocExtension::Visibility](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Visibility.md)
4. Call [IModelDocExtension::GetAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAppearanceSetting.md) to obtain an [IAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md) object.
5. Set the properties in the IAppearanceSetting object.
6. Get or set the material properties for the specified display states, entities, and scope using [IModelDocExtension::DisplayStateSpecMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.md).

Example

[Get Display State Settings (C#)](Get_Display_State_Settings_CSharp.htm)  
[Get Display State Settings (VB.NET)](Get_Display_State_Settings_VBNET.htm)  
[Get Display State Settings (VBA)](Get_Display_State_Settings_Example_VB.htm)  
[Change Color of Component in Specific Display State (C#)](Change_Color_of_Component_in_Specific_Display_State_Example_CSharp.htm)  
[Change Color of Component in Specific Display State (VB.NET)](Change_Color_of_Component_in_Specific_Display_State_Example_VBNET.htm)  
[Change Color of Component in Specific Display State (VBA)](Change_Color_of_Component_in_Specific_Display_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.md)  
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.md)  
[IDisplayStateSetting::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~IGetEntities.md)  
[IDisplayStateSetting::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetEntities.md)
