# AddVariablePitchHelixSegment Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddVariablePitchHelixSegment`

Adds a segment to a variable-pitch helix.
Adds a segment to a variable-pitch helix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddVariablePitchHelixSegment( _
   ByVal Height As System.Double, _
   ByVal Diameter As System.Double, _
   ByVal Pitch As System.Double _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim Height As System.Double
Dim Diameter As System.Double
Dim Pitch As System.Double
Dim value As System.Boolean
 
value = instance.AddVariablePitchHelixSegment(Height, Diameter, Pitch)
```

```

System.bool AddVariablePitchHelixSegment( 
   System.double Height,
   System.double Diameter,
   System.double Pitch
)
```

```

System.bool AddVariablePitchHelixSegment( 
   System.double Height,
   System.double Diameter,
   System.double Pitch
) 
```

#### Parameters

*Height*
:   Helix segment revolution; 1.0 = 360 degrees

*Diameter*
:   Diameter, which determines how far the variable-pitch helix segment extends

*Pitch*
:   Pitch, which determines the width of one complete helix turn, measured parallel to the axis of the helix

#### Return Value

True if the variable-pitch helix segment is added, false if not

Remarks

To create and insert a variable-pitch helix, call:

1. [IFeatureManager::InsertVariablePitchHelix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVariablePitchHelix.md) to create it.
2. [IFeatureManager::AddVariablePitchHelixFirstPitchAndDiameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddVariablePitchHelixFirstPitchAndDiameter.md) to add the first segment.
3. IFeatureManager::AddVariablePitchHelixSegment one or more times to add the remaining segments.
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
