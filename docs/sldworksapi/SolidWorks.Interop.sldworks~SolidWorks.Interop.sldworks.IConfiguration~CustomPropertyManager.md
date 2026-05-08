# CustomPropertyManager Property (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager`

Gets the custom property information for this configuration.
Gets the custom property information for this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CustomPropertyManager As CustomPropertyManager
```

```

Dim instance As IConfiguration
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

Pointer to [ICustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md) object

Example

[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IFeature::CustomPropertyManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CustomPropertyManager.md)  
[IModelDocExtension::CustomPropertyManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CustomPropertyManager.md)
