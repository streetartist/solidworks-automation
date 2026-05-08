# GetModelMaterialPropertyValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelMaterialPropertyValues`

Gets the material properties of this lightweight component in the specified configuration.
Gets the material properties of this lightweight component in the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetModelMaterialPropertyValues( _
   ByVal ConfigName As System.String _
) As System.Object
```

```

Dim instance As IComponent2
Dim ConfigName As System.String
Dim value As System.Object
 
value = instance.GetModelMaterialPropertyValues(ConfigName)
```

```

System.object GetModelMaterialPropertyValues( 
   System.string ConfigName
)
```

```

System.Object^ GetModelMaterialPropertyValues( 
   System.String^ ConfigName
) 
```

#### Parameters

*ConfigName*
:   Name of configuration

#### Return Value

An array of 9 doubles (see **Remarks**)

Remarks

The contents of the returned array:

[ R, G, B, Ambient, Diffuse, Specularity, Shininess, Transparency, Emission ]

Valid values are between 0.0 and 1.0, inclusive. Multiply the R, G, and B values by 255 to obtain the red, green, and blue component values. Multiply the other values in the array by 100 to obtain percentages. If all values in the array are -1, then material property values were not assigned to this component, and the component has the same default properties as the user interface.

Example

[Get Model Material Property Values (VBA)](Get_Model_Material_Property_Values_Example_VB.htm)  
[Get Model Material Property Values (VB.NET)](Get_Model_Material_Property_Values_Example_VBNET.htm)  
[Get Model Material Property Values (C#)](Get_Model_Material_Property_Values_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.md)  
[IComponent2::IGetModelMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetModelMaterialPropertyValues.md)  
[IComponent2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasMaterialPropertyValues.md)
