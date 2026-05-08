# Transparency Property (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Transparency`

Gets and sets the transparency states for the specified display state setting.
Gets and sets the transparency states for the specified display state setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Transparency( _
   ByVal Setting As DisplayStateSetting _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Setting As DisplayStateSetting
Dim value As System.Object
 
instance.Transparency(Setting) = value
 
value = instance.Transparency(Setting)
```

```

System.object Transparency( 
   DisplayStateSetting Setting
) {get; set;}
```

```

property System.Object^ Transparency {
   System.Object^ get(DisplayStateSetting^ Setting);
   void set (DisplayStateSetting^ Setting, System.Object^ value);
}
```

#### Parameters

*Setting*
:   [IDisplayStateSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.md)

#### Property Value

One-dimensional array of transparency states as defined in [swTransparencyState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTransparencyState_e.html) (see **Remarks**)

Remarks

Before calling this method:

1. Call [IModelDocExtension::GetDisplayStateSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDisplayStateSetting.md) to obtain an [IDisplayStateSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.md) object.
2. Call [IDisplayStateSetting::Names](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Names.md) or [IDisplayStateSetting::ISetNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetNames.md) to specify the display states.
3. Call [IDisplayStateSetting::Entities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Entities.md) or [IDisplayStateSetting::ISetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetEntities.md) to specify the components.
4. Call [IDisplayStateSetting::Option](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Option.md) to specify the display state scope of the setting.
5. Specify the Setting parameter using the IDisplayStateSetting object.

Each transparency state in the array returned by this method maps to a component in a display state. The size of the returned array is ([IDisplayStateSetting::GetEntityCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~GetEntityCount.md) X [IDisplayStateSetting::GetNameCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~GetNameCount.md)).

The returned array stores transparency states (TS) for N components in M display states as follows:

> Component1 DisplayState1 TS, Component1 DisplayState2 TS, ..., Component1 DisplayStateM TS,
>
> Component2 DisplayState1 TS, Component2 DisplayState2 TS, ..., Component2 DisplayStateM TS,
>
> ...,
>
> ComponentN DisplayState1 TS, ComponentN DisplayState2 TS, ..., ComponentN DisplayStateM TS

Example

[Get Display State Settings (C#)](Get_Display_State_Settings_CSharp.htm)  
[Get Display State Settings (VB.NET)](Get_Display_State_Settings_VBNET.htm)  
[Get Display State Settings (VBA)](Get_Display_State_Settings_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::DisplayMode Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayMode.md)  
[IModelDocExtension::DisplayStateSpecMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.md)  
[IModelDocExtension::Visibility Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Visibility.md)
