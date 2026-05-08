# ISetEntities Method (IDisplayStateSetting)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetEntities`

Sets the entities for this display state setting.
Sets the entities for this display state setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetEntities( _
   ByVal EntityCount As System.Integer, _
   ByRef Entities As System.Object _
) 
```

```

Dim instance As IDisplayStateSetting
Dim EntityCount As System.Integer
Dim Entities As System.Object
 
instance.ISetEntities(EntityCount, Entities)
```

```

void ISetEntities( 
   System.int EntityCount,
   ref System.object Entities
)
```

```

void ISetEntities( 
   System.int EntityCount,
   System.Object^% Entities
) 
```

#### Parameters

*EntityCount*
:   Number of entities in the Entities array

*Entities*
:   - in-process, unmanaged C++: Pointer to an array of entities
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

After calling this method:

1. Call [IDisplayStateSetting::ISetNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetNames.md) to specify the display states.
2. Call [IDisplayStateSetting::Option](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Option.md) to specify the display state scope of the setting.
3. Get or set one or more of the following properties for the specified display states, components, and scope:

   - [IModelDocExtension::DisplayMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayMode.md)
   - [IModelDocExtension::Transparency](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Transparency.md)
   - [IModelDocExtension::Visibility](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Visibility.md)
4. Call [IModelDocExtension::GetAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAppearanceSetting.md) to obtain an [IAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md) object.
5. Set the properties in the IAppearanceSetting object.
6. Get or set the material properties for the specified display states, components, and scope:

   - [IModelDocExtension::DisplayStateSpecMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.md)  
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.md)  
[IDisplayStateSetting::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Entities.md)  
[IDisplayStateSetting::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~IGetEntities.md)
