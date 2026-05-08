# AddVariablePitchHelixFirstPitchAndDiameter Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddVariablePitchHelixFirstPitchAndDiameter`

Adds the first segment to a variable-pitch helix.
Adds the first segment to a variable-pitch helix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddVariablePitchHelixFirstPitchAndDiameter( _
   ByVal FirstPitch As System.Double, _
   ByVal FirstDiameter As System.Double _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim FirstPitch As System.Double
Dim FirstDiameter As System.Double
Dim value As System.Boolean
 
value = instance.AddVariablePitchHelixFirstPitchAndDiameter(FirstPitch, FirstDiameter)
```

```

System.bool AddVariablePitchHelixFirstPitchAndDiameter( 
   System.double FirstPitch,
   System.double FirstDiameter
)
```

```

System.bool AddVariablePitchHelixFirstPitchAndDiameter( 
   System.double FirstPitch,
   System.double FirstDiameter
) 
```

#### Parameters

*FirstPitch*
:   Pitch, which determines the width of one complete helix turn, measured parallel to the axis of the helix

*FirstDiameter*
:   Diameter, which determines how far the variable-pitch helix segment extends

#### Return Value

True if the first segment of the helix is added, false if not

Remarks

To create and insert a variable-pitch helix, call:

1. [IFeatureManager::InsertVariablePitchHelix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVariablePitchHelix.md) to create it.
2. IFeatureManager::AddVariablePitchHelixFirstPitchAndDiamenter to add the first segment.
3. [IFeatureManager::AddVariablePitchHelixSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddVariablePitchHelixSegment.md) one or more times to add the remaining segments.
4. [IFeatureManager::EndVariablePitchHelix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EndVariablePitchHelix.md) to insert it.

Example

[Create Variable-pitch Helix (C#)](Create_Variable_Pitch_Helix_Example_CSharp.htm)  
[Create Variable-pitch Helix (VB.NET)](Create_Variable_Pitch_Helix_Example_VBNET.htm)  
[Create Variable-pitch Helix (VBA)](Create_Variable_Pitch_Helix_Example_VB.htm)  
[Create and Modify Variable-pitch Helix (C#)](Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm)  
[Create and Modify Variable-pitch Helix (VB.NET)](Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm)  
[Create and Modify Variable-pitch Helix (VBA)](Create_and_Modify_Variable-pitch_Helix_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md)
