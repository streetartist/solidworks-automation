# IGetModelMaterialPropertyValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetModelMaterialPropertyValues`

Gets the material properties of this lightweight component in the specified configuration.
Gets the material properties of this lightweight component in the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetModelMaterialPropertyValues( _
   ByVal ConfigName As System.String _
) As System.Double
```

```

Dim instance As IComponent2
Dim ConfigName As System.String
Dim value As System.Double
 
value = instance.IGetModelMaterialPropertyValues(ConfigName)
```

```

System.double IGetModelMaterialPropertyValues( 
   System.string ConfigName
)
```

```

System.double IGetModelMaterialPropertyValues( 
   System.String^ ConfigName
) 
```

#### Parameters

*ConfigName*
:   Name of the configuration

#### Return Value

- in-process, unmanaged C++: Pointer to an array of 9 doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The contents of the returned array:

[ R, G, B, Ambient, Diffuse, Specularity, Shininess, Transparency, Emission ]

Valid values are between 0.0 and 1.0, inclusive. Multiply the R, G, and B values by 255 to obtain the red, green, and blue component values. Multiply the other values in the array by 100 to obtain percentages. If all values in the array are -1, then material property values were not assigned to this component, and the component has the same default properties as the user interface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetModelMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelMaterialPropertyValues.md)  
[IComponent2::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.md)
