# IsCustomPropertyEditable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IsCustomPropertyEditable`

Gets whether the specified custom property is editable in the specified configuration.
Gets whether the specified custom property is editable in the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsCustomPropertyEditable( _
   ByVal PropertyName As System.String, _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

```

Dim instance As ICustomPropertyManager
Dim PropertyName As System.String
Dim ConfigurationName As System.String
Dim value As System.Boolean
 
value = instance.IsCustomPropertyEditable(PropertyName, ConfigurationName)
```

```

System.bool IsCustomPropertyEditable( 
   System.string PropertyName,
   System.string ConfigurationName
)
```

```

System.bool IsCustomPropertyEditable( 
   System.String^ PropertyName,
   System.String^ ConfigurationName
) 
```

#### Parameters

*PropertyName*
:   Custom property name

*ConfigurationName*
:   Configuration name

#### Return Value

True if the custom property is editable, false if not

Remarks

Use [ICustomPropertyManager::GetNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetNames.md) to populate PropertyName.

Example

[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)  
[Get Custom Properties for Configuration (VB.NET)](Get_Custom_Properties_for_Configuration_Example_VBNET.htm)  
[Get Custom Properties for Configuration (C#)](Get_Custom_Properties_for_Configuration_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)
