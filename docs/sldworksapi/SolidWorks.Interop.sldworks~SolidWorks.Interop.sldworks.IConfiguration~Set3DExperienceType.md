# Set3DExperienceType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Set3DExperienceType`

Converts this configuration in SOLIDWORKS Connected.
Converts this configuration in [SOLIDWORKS Connected](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Set3DExperienceType( _
   ByVal IsPhysicalProduct As System.Boolean, _
   ByVal RepresentationParentName As System.String _
) As System.Boolean
```

```

Dim instance As IConfiguration
Dim IsPhysicalProduct As System.Boolean
Dim RepresentationParentName As System.String
Dim value As System.Boolean
 
value = instance.Set3DExperienceType(IsPhysicalProduct, RepresentationParentName)
```

```

System.bool Set3DExperienceType( 
   System.bool IsPhysicalProduct,
   System.string RepresentationParentName
)
```

```

System.bool Set3DExperienceType( 
   System.bool IsPhysicalProduct,
   System.String^ RepresentationParentName
) 
```

#### Parameters

*IsPhysicalProduct*
:   True to convert this configuration to a parent configuration (Physical Product/Family), false to convert it to a derived configuration (Representation)

*RepresentationParentName*
:   Parent Physical Product/Family name of derived configuration (Representation); valid only if IsPhysicalProduct is false

#### Return Value

True if configuration successfully converted, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::Get3DExperienceType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Get3DExperienceType.md)  
[IConfiguration::AddCADFamilyConfiguration Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddCADFamilyConfiguration.md)
