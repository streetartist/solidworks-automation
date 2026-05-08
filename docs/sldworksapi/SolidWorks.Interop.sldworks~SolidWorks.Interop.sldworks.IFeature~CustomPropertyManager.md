# CustomPropertyManager Property (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CustomPropertyManager`

Gets the custom property information for weldment and cut-list item features only.
Gets the custom property information for weldment and cut-list item features only.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CustomPropertyManager As CustomPropertyManager
```

```

Dim instance As IFeature
Dim value As CustomPropertyManager
 
value = instance.CustomPropertyManager
```

```

CustomPropertyManager CustomPropertyManager {get;}
```

```

property CustomPropertyManager^ CustomPropertyManager {
   CustomPropertyManager^ get();
}
```

#### Property Value

Pointer to the [ICustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md) object

Example

[Add and Get Custom Properties (VBA)](Add_and_Get_Custom_Properties_Example_VB.htm)  
[Get Custom Properties for Cut-list Item (VBA)](Get_Custom_Properties_for_Cut-list_Item_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IModelDocExtension::CustomPropertyManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CustomPropertyManager.md)  
[IConfiguration::CustomPropertyManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.md)
