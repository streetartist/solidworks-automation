# AddSpeedPak2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddSpeedPak2`

Creates a SpeedPak configuration that includes all faces and the specified threshold of parts or bodies for the active assembly configuration.
Creates a SpeedPak configuration that includes all faces and the specified threshold of parts or bodies for the active assembly configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSpeedPak2( _
   ByVal Type As System.Integer, _
   ByVal PartThreshold As System.Double _
) As System.Object
```

```

Dim instance As IConfigurationManager
Dim Type As System.Integer
Dim PartThreshold As System.Double
Dim value As System.Object
 
value = instance.AddSpeedPak2(Type, PartThreshold)
```

```

System.object AddSpeedPak2( 
   System.int Type,
   System.double PartThreshold
)
```

```

System.Object^ AddSpeedPak2( 
   System.int Type,
   System.double PartThreshold
) 
```

#### Parameters

*Type*
:   Selection type:

    - 1 = Geometry
    - 2 = Graphics

*PartThreshold*
:   1.0 >= Double value for part or body selection threshold >= 0.0; 1.0 selects nothing, and 0.0 selects all (see **Remarks**)

#### Return Value

SpeedPak [configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)

Remarks

PartThreshold corresponds to the value of the **Bodies to Include** slider on the SpeedPak PropertyManager page.

This method includes all faces in the SpeedPak configuration.

Example

[Create a SpeedPak Configuration (VBA)](Create_SpeedPak_Example_VB.htm)  
[Create a Speedpak Configuration (VB.NET)](Create_SpeedPak_Example_VBNET.htm)  
[Create a Speedpak Configuration (C#)](Create_Speedpak_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)  
[IConfiguration::IsSpeedPak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsSpeedPak.md)  
[IConfiguration::UpdateSpeedPak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UpdateSpeedPak.md)  
[IAssemblyDoc::CreateSpeedPak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSpeedPak.md)
