# GetLicenseType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetLicenseType`

Gets the type of SOLIDWORKS license used when the model was created.
Gets the type of SOLIDWORKS license used when the model was created.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLicenseType() As System.Integer
```

```

Dim instance As IModelDocExtension
Dim value As System.Integer
 
value = instance.GetLicenseType()
```

```

System.int GetLicenseType()
```

```

System.int GetLicenseType(); 
```

#### Return Value

Type of SOLIDWORKS license as defined in [swLicenseType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLicenseType_e.html)

Remarks

This method always returns 0 (swLicenseType\_e.swLicenseType\_Full) for files saved under any commercial SOLIDWORKS license.

To get the license type of this SOLIDWORKS installation, use [ISldWorks::GetCurrentLicenseType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentLicenseType.md).

Example

[Get License Type of SOLIDWORKS (C#)](Get_License_Types_of_SOLIDWORKS_Example_CSharp.htm)  
[Get License Type of SOLIDWORKS (VB.NET)](Get_License_Types_of_SOLIDWORKS_Example_VBNET.htm)  
[Get License Type of SOLIDWORKS (VBA)](Get_License_Types_of_SOLIDWORKS_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
