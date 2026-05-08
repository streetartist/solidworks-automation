# FeatureExtrusion3 Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtrusion3`

Creates an extruded feature.
Creates an extruded feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureExtrusion3( _
   ByVal Sd As System.Boolean, _
   ByVal Flip As System.Boolean, _
   ByVal Dir As System.Boolean, _
   ByVal T1 As System.Integer, _
   ByVal T2 As System.Integer, _
   ByVal D1 As System.Double, _
   ByVal D2 As System.Double, _
   ByVal Dchk1 As System.Boolean, _
   ByVal Dchk2 As System.Boolean, _
   ByVal Ddir1 As System.Boolean, _
   ByVal Ddir2 As System.Boolean, _
   ByVal Dang1 As System.Double, _
   ByVal Dang2 As System.Double, _
   ByVal OffsetReverse1 As System.Boolean, _
   ByVal OffsetReverse2 As System.Boolean, _
   ByVal TranslateSurface1 As System.Boolean, _
   ByVal TranslateSurface2 As System.Boolean, _
   ByVal Merge As System.Boolean, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean, _
   ByVal T0 As System.Integer, _
   ByVal StartOffset As System.Double, _
   ByVal FlipStartOffset As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Sd As System.Boolean
Dim Flip As System.Boolean
Dim Dir As System.Boolean
Dim T1 As System.Integer
Dim T2 As System.Integer
Dim D1 As System.Double
Dim D2 As System.Double
Dim Dchk1 As System.Boolean
Dim Dchk2 As System.Boolean
Dim Ddir1 As System.Boolean
Dim Ddir2 As System.Boolean
Dim Dang1 As System.Double
Dim Dang2 As System.Double
Dim OffsetReverse1 As System.Boolean
Dim OffsetReverse2 As System.Boolean
Dim TranslateSurface1 As System.Boolean
Dim TranslateSurface2 As System.Boolean
Dim Merge As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim T0 As System.Integer
Dim StartOffset As System.Double
Dim FlipStartOffset As System.Boolean
Dim value As Feature
 
value = instance.FeatureExtrusion3(Sd, Flip, Dir, T1, T2, D1, D2, Dchk1, Dchk2, Ddir1, Ddir2, Dang1, Dang2, OffsetReverse1, OffsetReverse2, TranslateSurface1, TranslateSurface2, Merge, UseFeatScope, UseAutoSelect, T0, StartOffset, FlipStartOffset)
```

```

Feature FeatureExtrusion3( 
   System.bool Sd,
   System.bool Flip,
   System.bool Dir,
   System.int T1,
   System.int T2,
   System.double D1,
   System.double D2,
   System.bool Dchk1,
   System.bool Dchk2,
   System.bool Ddir1,
   System.bool Ddir2,
   System.double Dang1,
   System.double Dang2,
   System.bool OffsetReverse1,
   System.bool OffsetReverse2,
   System.bool TranslateSurface1,
   System.bool TranslateSurface2,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.int T0,
   System.double StartOffset,
   System.bool FlipStartOffset
)
```

```

Feature^ FeatureExtrusion3( 
   System.bool Sd,
   System.bool Flip,
   System.bool Dir,
   System.int T1,
   System.int T2,
   System.double D1,
   System.double D2,
   System.bool Dchk1,
   System.bool Dchk2,
   System.bool Ddir1,
   System.bool Ddir2,
   System.double Dang1,
   System.double Dang2,
   System.bool OffsetReverse1,
   System.bool OffsetReverse2,
   System.bool TranslateSurface1,
   System.bool TranslateSurface2,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.int T0,
   System.double StartOffset,
   System.bool FlipStartOffset
) 
```

#### Parameters

*Sd*
:   True for single ended, false for double ended

*Flip*
:   True to flip the side to cut

*Dir*
:   True to flip the direction of extrusion

*T1*
:   Termination type for first end of the extrusion as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

*T2*
:   Termination type for second end of the extrusion as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

*D1*
:   Depth of extrusion for first end in meters; offset, if T1 is set to [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html).swEndCondOffsetFromSurface

*D2*
:   Depth of extrusion for second end in meters; offset, if T2 is set to [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html).swEndCondOffsetFromSurface

*Dchk1*
:   True to allow drafting in the first direction, false to not

*Dchk2*
:   True to allow drafting in the second direction, false to not

*Ddir1*
:   True for first draft angle to be inward, false to be outward; valid only if Dchk1 is true

*Ddir2*
:   True for second draft angle to be inward, false to be outward; valid only if Dchk2 is true

*Dang1*
:   Draft angle for first end; valid only if Dchk1 is true

*Dang2*
:   Draft angle for second end; valid only if Dchk2 is true

*OffsetReverse1*
:   True to offset the first end from another face or plane in a direction away from the sketch, false to offset in a direction toward the sketch; valid only if T1 is set to [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html).swEndCondOffsetFromSurface

*OffsetReverse2*
:   True to offset the second end from another face or plane in a direction away from the sketch, false to offset in a direction toward the sketch; valid only if T2 is set to [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html).swEndCondOffsetFromSurface

*TranslateSurface1*
:   True if the first end of the extrusion is a translation of the reference surface, false if it has a true offset; valid only if T1 is set to [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html).swEndCondOffsetFromSurface

*TranslateSurface2*
:   True if the second end of the extrusion is a translation of the reference surface, false if it has a true offset; valid only if T2 is set to [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html).swEndCondOffsetFromSurface

*Merge*
:   True to merge the results in a multibody part, false to not

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies (see **Remarks**)

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies that the feature affects (see **Remarks**)

*T0*
:   Start condition as defined in [swStartConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStartConditions_e.html)

*StartOffset*
:   Distance from the sketch plane to start the extrude; valid only if T0 is set to [swStartConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStartConditions_e.html).swStartOffset

*FlipStartOffset*
:   True to flip the direction of the start offset, false to not; valid only if T0 is set to [swStartConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStartConditions_e.html).swStartOffset

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

The difference between this method and the now obsolete IFeatureManager::FeatureExtrusion2 is that this method supports the selection of surface, face, and plane references for start and end conditions.

Before calling this method to extrude a 3D sketch:

| Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select... | With selection mark... |
| --- | --- |
| 3D sketch | 0 |
| Extrusion direction edge | 16 |
| Start condition reference entity | 32 |
| End condition reference entity | 1 |

The default direction for cut operations is opposite the sketch normal. The default direction for boss operations is along the sketch normal. Setting the Dir argument to True reverses the default direction. For double-ended extrusions, Direction 2 is always opposite to Direction 1.

The default sketch normal is the same as the face or plane normal where the sketch was placed. To determine this normal vector, see [IFace2::Normal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Normal.md) and [IRefPlane::Transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~Transform.md), respectively.

When UseAutoSelect is false, the user must select the bodies that the feature affects. Use a selection mark of 8 for each selected body.

When using cut or cavity features that result in multiple bodies, you cannot select to keep all of the resulting bodies or one or more selected bodies.

Example

[Create Extrusion Feature (VBA)](Insert_Feature_Extrusion_Example_VB.htm)  
[Create Extrusion Feature (VB.NET)](Insert_Feature_Extrusion_Example_VBNET.htm)  
[Create Extrusion Feature (C#)](Insert_Feature_Extrusion_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IFeatureManager::FeatureExtrusionThin2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtrusionThin2.md)  
[IFeatureManager::FeatureCut3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCut3.md)
