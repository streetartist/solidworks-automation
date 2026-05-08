# InsertVariablePitchHelix Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVariablePitchHelix`

Starts a variable-pitch helix using the selected sketch containing an arc.
Starts a variable-pitch helix using the selected sketch containing an arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertVariablePitchHelix( _
   ByVal Reversed As System.Boolean, _
   ByVal Clockwise As System.Boolean, _
   ByVal Helixdef As System.Integer, _
   ByVal Startangle As System.Double _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim Reversed As System.Boolean
Dim Clockwise As System.Boolean
Dim Helixdef As System.Integer
Dim Startangle As System.Double
Dim value As System.Boolean
 
value = instance.InsertVariablePitchHelix(Reversed, Clockwise, Helixdef, Startangle)
```

```

System.bool InsertVariablePitchHelix( 
   System.bool Reversed,
   System.bool Clockwise,
   System.int Helixdef,
   System.double Startangle
)
```

```

System.bool InsertVariablePitchHelix( 
   System.bool Reversed,
   System.bool Clockwise,
   System.int Helixdef,
   System.double Startangle
) 
```

#### Parameters

*Reversed*
:   True to reverse the variable-pitch helix, false to not

*Clockwise*
:   True to create the variable-pitch helix in a clockwise direction, false to create in a counter-clockwise direction

*Helixdef*
:   Definition of variable-pitch helix as defined in [swHelixDefinedBy\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHelixDefinedBy_e.html); valid enumerators are:

    - swHelixDefinedByPitchAndRevolution
    - swHelixDefinedByHeightandRevolution
    - swHelixDefinedByHeightAndPitch

*Startangle*
:   Angle at which to start the variable-pitch helix

#### Return Value

True if the variable-pitch helix is started, false if not

Remarks

To create and insert a variable-pitch helix, call:

1. IFeatureManager::InsertVariablePitchHelix to create it.
2. [IFeatureManager::AddVariablePitchHelixFirstPitchAndDiamenter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddVariablePitchHelixFirstPitchAndDiameter.md) to add the first segment.
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
