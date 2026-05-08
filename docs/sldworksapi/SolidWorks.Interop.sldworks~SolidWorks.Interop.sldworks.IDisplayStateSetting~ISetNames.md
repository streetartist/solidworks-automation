# ISetNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetNames`

Sets the display state names for this display state setting.
Sets the display state names for this display state setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetNames( _
   ByVal DsNameCount As System.Integer, _
   ByRef DSNames As System.String _
) 
```

```

Dim instance As IDisplayStateSetting
Dim DsNameCount As System.Integer
Dim DSNames As System.String
 
instance.ISetNames(DsNameCount, DSNames)
```

```

void ISetNames( 
   System.int DsNameCount,
   ref System.string DSNames
)
```

```

void ISetNames( 
   System.int DsNameCount,
   System.String^% DSNames
) 
```

#### Parameters

*DsNameCount*
:   Number of names in the DSNames array

*DSNames*
:   - in-process, unmanaged C++: Pointer to an array display state names
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

After calling this method:

1. Call [IDisplayStateSetting::ISetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetEntities.md) to specify the entities.
2. Call [IDisplayStateSetting::Option](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Option.md) to specify the display state scope of the setting.
3. Get or set one or more of the following properties for the specified display states, entities, and scope:
   - [IModelDocExtension::DisplayMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayMode.md)
   - [IModelDocExtension::Transparency](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Transparency.md)
   - [IModelDocExtension::Visibility](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Visibility.md)
4. Call [IModelDocExtension::GetAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAppearanceSetting.md) to obtain an [IAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.md) object.
5. Set the properties in the IAppearanceSetting object.
6. Get or set the material properties for the specified display states, entities, and scope:

   - [IModelDocExtension::DisplayStateSpecMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.md)  
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.md)  
[IDisplayStateSetting::Names Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Names.md)  
[IDisplayStateSetting::IGetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~IGetNames.md)
