# PostTrimSurface Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostTrimSurface`

Sets whether to sew the resulting trimmed surfaces.
Sets whether to sew the resulting trimmed surfaces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PostTrimSurface( _
   ByVal BSewSurfaceIn As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim BSewSurfaceIn As System.Boolean
Dim value As Feature
 
value = instance.PostTrimSurface(BSewSurfaceIn)
```

```

Feature PostTrimSurface( 
   System.bool BSewSurfaceIn
)
```

```

Feature^ PostTrimSurface( 
   System.bool BSewSurfaceIn
) 
```

#### Parameters

*BSewSurfaceIn*
:   True to sew the resulting trimmed surfaces, false to not

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method:

1. Call [IFeatureManager::PreTrimSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreTrimSurface.md).
2. Select the trimming surfaces or trim tool.
3. Optionally, call [IFeatureManager::SolidForTrim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SolidForTrim.md).

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
