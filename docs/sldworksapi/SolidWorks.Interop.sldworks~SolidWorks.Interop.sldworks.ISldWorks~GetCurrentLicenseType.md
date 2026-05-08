# GetCurrentLicenseType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentLicenseType`

Gets the type of license for the current SOLIDWORKS session.
Gets the type of license for the current SOLIDWORKS session.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurrentLicenseType() As System.Integer
```

```

Dim instance As ISldWorks
Dim value As System.Integer
 
value = instance.GetCurrentLicenseType()
```

```

System.int GetCurrentLicenseType()
```

```

System.int GetCurrentLicenseType(); 
```

#### Return Value

Type of SOLIDWORKS license as defined in [swLicenseType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLicenseType_e.html)

Example

[Get License Types of SOLIDWORKS (C#)](Get_License_Types_of_SOLIDWORKS_Example_CSharp.htm)  
[Get License Types of SOLIDWORKS (VB.NET)](Get_License_Types_of_SOLIDWORKS_Example_VBNET.htm)  
[Get License Types of SOLIDWORKS (VBA)](Get_License_Types_of_SOLIDWORKS_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[IModelDocExtension::GetLicenseType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetLicenseType.md)
