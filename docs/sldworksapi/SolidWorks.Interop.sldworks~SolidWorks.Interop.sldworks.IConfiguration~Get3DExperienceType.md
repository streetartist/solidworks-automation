# Get3DExperienceType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Get3DExperienceType`

Gets how this configuration is viewed in SOLIDWORKS Connected.
Gets how this configuration is viewed in [SOLIDWORKS Connected](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Get3DExperienceType() As System.Integer
```

```

Dim instance As IConfiguration
Dim value As System.Integer
 
value = instance.Get3DExperienceType()
```

```

System.int Get3DExperienceType()
```

```

System.int Get3DExperienceType(); 
```

#### Return Value

Type of 3DEXPERIENCE configuration as defined in [sw3DExperienceCfgType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DExperienceCfgType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::GetRepresentationParent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRepresentationParent.md)  
[IConfiguration::Set3DExperienceType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Set3DExperienceType.md)  
[IConfigurationManager::AddCADFamilyConfiguration Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddCADFamilyConfiguration.md)
