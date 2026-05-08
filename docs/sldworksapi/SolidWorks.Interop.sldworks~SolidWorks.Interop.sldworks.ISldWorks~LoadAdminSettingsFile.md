# LoadAdminSettingsFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAdminSettingsFile`

Loads the specified *.sldsettings file into SOLIDWORKS Connected.
Loads the specified **\*.sldsettings** file into [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LoadAdminSettingsFile( _
   ByVal FilePath As System.String _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim FilePath As System.String
Dim value As System.Integer
 
value = instance.LoadAdminSettingsFile(FilePath)
```

```

System.int LoadAdminSettingsFile( 
   System.string FilePath
)
```

```

System.int LoadAdminSettingsFile( 
   System.String^ FilePath
) 
```

#### Parameters

*FilePath*
:   Full local path name of the **\*.sldsettings** file to load

#### Return Value

True if settings successfully applied, false if not

Remarks

The 3DEXPERIENCE platform Admin authors the **\*.sldsettings** platform file with settings appropriate for SOLIDWORKS Connected. At launch, SOLIDWORKS Connected reads a local copy. This method is used primarily by the 3DEXPERIENCE Add-in.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::RestoreSettings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RestoreSettings.md)  
[ISldWorks::SaveSettings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SaveSettings.md)
