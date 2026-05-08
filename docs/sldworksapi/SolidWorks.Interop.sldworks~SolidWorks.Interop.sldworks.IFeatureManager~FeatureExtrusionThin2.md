# FeatureExtrusionThin2 Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtrusionThin2`

Creates an extruded thin feature.
Creates an extruded thin feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureExtrusionThin2( _
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
   ByVal Thk1 As System.Double, _
   ByVal Thk2 As System.Double, _
   ByVal EndThk As System.Double, _
   ByVal RevThinDir As System.Integer, _
   ByVal CapEnds As System.Integer, _
   ByVal AddBends As System.Boolean, _
   ByVal BendRad As System.Double, _
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
Dim Thk1 As System.Double
Dim Thk2 As System.Double
Dim EndThk As System.Double
Dim RevThinDir As System.Integer
Dim CapEnds As System.Integer
Dim AddBends As System.Boolean
Dim BendRad As System.Double
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim T0 As System.Integer
Dim StartOffset As System.Double
Dim FlipStartOffset As System.Boolean
Dim value As Feature
 
value = instance.FeatureExtrusionThin2(Sd, Flip, Dir, T1, T2, D1, D2, Dchk1, Dchk2, Ddir1, Ddir2, Dang1, Dang2, OffsetReverse1, OffsetReverse2, TranslateSurface1, TranslateSurface2, Merge, Thk1, Thk2, EndThk, RevThinDir, CapEnds, AddBends, BendRad, UseFeatScope, UseAutoSelect, T0, StartOffset, FlipStartOffset)
```

```

Feature FeatureExtrusionThin2( 
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
   System.double Thk1,
   System.double Thk2,
   System.double EndThk,
   System.int RevThinDir,
   System.int CapEnds,
   System.bool AddBends,
   System.double BendRad,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.int T0,
   System.double StartOffset,
   System.bool FlipStartOffset
)
```

```

Feature^ FeatureExtrusionThin2( 
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
   System.double Thk1,
   System.double Thk2,
   System.double EndThk,
   System.int RevThinDir,
   System.int CapEnds,
   System.bool AddBends,
   System.double BendRad,
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
:   Not used

*Dir*
:   Reverse direction; True if you want Direction1 to be opposite the default direction (see **Remarks**)

*T1*
:   Termination type for first end as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

*T2*
:   Termination type for second end as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

*D1*
:   Depth of extrusion for first end in meters

*D2*
:   Depth of extrusion for second end in meters

*Dchk1*
:   True allows draft angle in first direction, false does not allow drafting

*Dchk2*
:   True allows draft angle in second direction, false does not allow drafting

*Ddir1*
:   True for first draft angle to be inward, false to be outward

*Ddir2*
:   True for second draft angle to be inward, false to be outward

*Dang1*
:   First draft angle

*Dang2*
:   Second draft angle

*OffsetReverse1*
:   If you chose to offset the first end condition from another face or plane, then True specifies offset in direction away from the sketch, false specifies offset from the face or plane in direction toward the sketch

*OffsetReverse2*
:   If you chose to offset the second end condition from another face or plane, then True specifies offset in direction away from the sketch, false specifies offset from the face or plane in direction toward the sketch

*TranslateSurface1*
:   When you choose swEndcondOffsetFromSurface as the termination type for the first end, then True specifies that the end of the extrusion is a translation of the reference surface, false specifies to use a true offset

*TranslateSurface2*
:   When you choose swEndcondOffsetFromSurface as the termination type for the second end, then True specifies that the end of the extrusion is a translation of the reference surface, false specifies to use a true offset

*Merge*
:   True to merge the resultant base or boss body into an existing body, false to create a distinct solid body

*Thk1*
:   Wall thickness 1 (Mid-plane type uses (Thk1)/2 for each direction)

*Thk2*
:   Wall thickness 2 (Only used when RevThinType =3 )

*EndThk*
:   End cap thickness (Only used when CapEnds = 1)

*RevThinDir*
:   Thin feature type:

    - 0 = One direction
    - 1 = One direction reverse
    - 2 = Mid-plane
    - 3 = Two direction

*CapEnds*
:   Cap the ends:

    - 0 = no cap
    - 1 = cap (base features only)

*AddBends*
:   True to add auto bends (open profile base features only), false to not

*BendRad*
:   Fillet radii if AddBends = True

*UseFeatScope*
:   True if the feature only affects selected bodies, false if the feature affects all bodies

*UseAutoSelect*
:   True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects (see Remarks)

*T0*
:   Start condition as defined in [swStartConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStartConditions_e.html)

*StartOffset*
:   If T0 set to swStartOffset, then specify offset value

*FlipStartOffset*
:   If T0 set to swStartOffset, then True to flip the direction or false to not

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

The default direction for cut operations is opposite the sketch normal. The default direction for boss operations is along the sketch normal. Setting the Dir argument to True reverses the default direction. For double-ended extrusions, Direction 2 is always opposite of Direction 1.

The default sketch normal is the same as the face or plane normal where the sketch was placed. To determine this normal vector, see [IFace2::Normal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Normal.md) and [IRefPlane::Transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~Transform.md), respectively.

When UseAutoSelect is false, the user must select the bodies that the feature will affect.

When using cut or cavity features that result in multiple bodies, you cannot select to keep all of the resulting bodies or one or more selected bodies.

Example

[Create Extruded Thin Feature (VBA)](Create_Extruded_Thin_Feature_Example_VB.htm)  
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)  
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IFeature::FeatureExtrusion2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureExtrusion2.md)  
[IFeature::FeatureCutThin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCutThin.md)
