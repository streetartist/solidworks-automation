# AddCADFamilyConfiguration Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddCADFamilyConfiguration`

Adds the specified configuration to SOLIDWORKS Connected.
Adds the specified configuration to [SOLIDWORKS Connected](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCADFamilyConfiguration( _
   ByVal Name As System.String, _
   ByVal Description As System.String, _
   ByVal IsPhysicalProduct As System.Boolean, _
   ByVal RepresentationParentName As System.String, _
   ByVal ConfigOptions As System.Integer, _
   ByVal ChildCompDisplayOption As System.Integer, _
   ByVal Rebuild As System.Boolean _
) As System.Object
```

```

Dim instance As IConfigurationManager
Dim Name As System.String
Dim Description As System.String
Dim IsPhysicalProduct As System.Boolean
Dim RepresentationParentName As System.String
Dim ConfigOptions As System.Integer
Dim ChildCompDisplayOption As System.Integer
Dim Rebuild As System.Boolean
Dim value As System.Object
 
value = instance.AddCADFamilyConfiguration(Name, Description, IsPhysicalProduct, RepresentationParentName, ConfigOptions, ChildCompDisplayOption, Rebuild)
```

```

System.object AddCADFamilyConfiguration( 
   System.string Name,
   System.string Description,
   System.bool IsPhysicalProduct,
   System.string RepresentationParentName,
   System.int ConfigOptions,
   System.int ChildCompDisplayOption,
   System.bool Rebuild
)
```

```

System.Object^ AddCADFamilyConfiguration( 
   System.String^ Name,
   System.String^ Description,
   System.bool IsPhysicalProduct,
   System.String^ RepresentationParentName,
   System.int ConfigOptions,
   System.int ChildCompDisplayOption,
   System.bool Rebuild
) 
```

#### Parameters

*Name*
:   Name of the configuration to add

*Description*
:   Details about the configuration

*IsPhysicalProduct*
:   True to add a parent configuration (Physical Product), false to add a derived configuration (Representation)

*RepresentationParentName*
:   Parent Physical Product name of derived configuration (Representation); valid only if IsPhysicalProduct is false

*ConfigOptions*
:   Configuration options as defined by [swCADFamilyCfgOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCADFamilyCfgOptions_e.html)

*ChildCompDisplayOption*
:   Child component display option as defined in [swChildComponentInBOMOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChildComponentInBOMOption_e.html)

*Rebuild*
:   True to rebuild the model after adding this configuration, false to not

#### Return Value

[IConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)  
[IConfiguration::Get3DExperienceType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Get3DExperienceType.md)  
[IConfiguration::Set3DExperienceType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Set3DExperienceType.md)
