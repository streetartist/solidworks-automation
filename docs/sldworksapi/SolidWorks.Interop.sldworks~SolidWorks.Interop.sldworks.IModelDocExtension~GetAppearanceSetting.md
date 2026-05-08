# GetAppearanceSetting Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAppearanceSetting`

Gets the appearance setting for this document.
Gets the appearance setting for this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAppearanceSetting() As AppearanceSetting
```

```

Dim instance As IModelDocExtension
Dim value As AppearanceSetting
 
value = instance.GetAppearanceSetting()
```

```

AppearanceSetting GetAppearanceSetting()
```

```

AppearanceSetting^ GetAppearanceSetting(); 
```

#### Return Value

[IAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md)

Remarks

After calling this method:

1. Set the properties in the [IAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md) object.
2. Call [IModelDocExtension::GetDisplayStateSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDisplayStateSetting.md) to obtain an [IDisplayStateSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.md) object.
3. Call [IDisplayStateSetting::Names](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Names.md) or [IDisplayStateSetting::ISetNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetNames.md) to specify the display states.
4. Call [IDisplayStateSetting::Entities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Entities.md) or [IDisplayStateSetting::ISetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetEntities.md) to specify the components.
5. Call [IDisplayStateSetting::Option](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Option.md) to specify the scope of the display state setting.
6. Get or set the material properties for the specified display states, components, and scope using [IModelDocExtension::DisplayStateSpecMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
