# PreTrimSurface Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreTrimSurface`

Sets the trimming options before trimming a surface.
Sets the trimming options before trimming a surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PreTrimSurface( _
   ByVal BMutualTrimIn As System.Boolean, _
   ByVal BSplitSystemIn As System.Boolean, _
   ByVal BSplitLinearIn As System.Boolean, _
   ByVal BRemovePickedIn As System.Boolean _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim BMutualTrimIn As System.Boolean
Dim BSplitSystemIn As System.Boolean
Dim BSplitLinearIn As System.Boolean
Dim BRemovePickedIn As System.Boolean
Dim value As System.Boolean
 
value = instance.PreTrimSurface(BMutualTrimIn, BSplitSystemIn, BSplitLinearIn, BRemovePickedIn)
```

```

System.bool PreTrimSurface( 
   System.bool BMutualTrimIn,
   System.bool BSplitSystemIn,
   System.bool BSplitLinearIn,
   System.bool BRemovePickedIn
)
```

```

System.bool PreTrimSurface( 
   System.bool BMutualTrimIn,
   System.bool BSplitSystemIn,
   System.bool BSplitLinearIn,
   System.bool BRemovePickedIn
) 
```

#### Parameters

*BMutualTrimIn*
:   True to use the selected intersecting surfaces as the trimming surfaces (mutual), false to use the selected surface, plane, or sketch as the trim tool (standard)

*BSplitSystemIn*
:   True to let the SOLIDWORKS application determine which surfaces to trim, false to trim all possible surfaces

*BSplitLinearIn*
:   False to naturally extend any trims along the intersecting surfaces, true to extend any trims linearly along the intersecting surfaces

*BRemovePickedIn*
:   True to remove the selected surfaces, false to keep the selected surfaces

#### Return Value

True if successful, false if not

Remarks

After calling this method:

1. Select the trimming surfaces or trim tool.
2. Optionally, call [IFeatureManager::SolidForTrim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SolidForTrim.md).
3. Call [IFeatureManager::PostTrimSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostTrimSurface.md).

Example

[Create Trimmed Surface Feature (C#)](Create_Trimmed_Surface_Feature_Example_CSharp.htm)  
[Create Trimmed Surface Feature (VB.NET)](Create_Trimmed_Surface_Feature_Example_VBNET.htm)  
[Create Trimmed Surface Feature (VBA)](Create_Trimmed_Surface_Feature_Example_VB.htm)  
[Create Solid Body Surface Trim Feature (C#)](Create_Solid_Body_Surface_Trim_Feature_Example_CSharp.htm)  
[Create Solid Body Surface Trim Feature (VB.NET)](Create_Solid_Body_Surface_Trim_Feature_Example_VBNET.htm)  
[Create Solid Body Surface Trim Feature (VBA)](Create_Solid_Body_Surface_Trim_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.md)
