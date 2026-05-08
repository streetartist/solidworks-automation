# AddSpeedPak Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddSpeedPak`

Obsolete. Superseded by IConfigurationManager::AddSpeedPak2.
Obsolete. Superseded by [IConfigurationManager::AddSpeedPak2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddSpeedPak2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSpeedPak( _
   ByVal Type As System.Integer, _
   ByVal PartThreshold As System.Double, _
   ByVal FaceThreshold As System.Double _
) As System.Object
```

```

Dim instance As IConfigurationManager
Dim Type As System.Integer
Dim PartThreshold As System.Double
Dim FaceThreshold As System.Double
Dim value As System.Object
 
value = instance.AddSpeedPak(Type, PartThreshold, FaceThreshold)
```

```

System.object AddSpeedPak( 
   System.int Type,
   System.double PartThreshold,
   System.double FaceThreshold
)
```

```

System.Object^ AddSpeedPak( 
   System.int Type,
   System.double PartThreshold,
   System.double FaceThreshold
) 
```

#### Parameters

*Type*
:   - 1 = Geometry
    - 2 = Graphics

*PartThreshold*

*FaceThreshold*
:   See **Remarks**

#### Return Value

SpeedPak [configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)

Remarks

The SOLIDWORKS user-interface control corresponding to the FaceThreshhold parameter was removed from SOLIDWORKS 2013 and later. Regardless of the value that you specify for the FaceThreshhold parameter, the value 0 is passed, which results in no faces being included for SpeedPak by a call to this method.

This method was revised as described so that existing applications that call this method will not fail.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)  
[IConfiguration::IsSpeedPak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsSpeedPak.md)  
[IConfiguration::UpdateSpeedPak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UpdateSpeedPak.md)
