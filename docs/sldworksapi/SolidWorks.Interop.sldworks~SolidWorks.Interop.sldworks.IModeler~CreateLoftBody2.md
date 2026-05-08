# CreateLoftBody2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftBody2`

Creates a loft body using the specified profiles, guide curves, and centerline.
Creates a loft body using the specified profiles, guide curves, and centerline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateLoftBody2( _
   ByVal PModDoc As ModelDoc2, _
   ByVal Profile As System.Object, _
   ByVal GuideCurve As System.Object, _
   ByVal Centerline As System.Object, _
   ByVal IsThinBody As System.Boolean, _
   ByVal ThinType As System.Integer, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal FeatureScope As System.Boolean, _
   ByVal IsBlendClosed As System.Boolean, _
   ByVal KeepTangency As System.Boolean, _
   ByVal ForceNonRational As System.Boolean, _
   ByVal IsSolidBody As System.Boolean, _
   ByVal TessTolFactor As System.Double, _
   ByVal StartTangentLength As System.Double, _
   ByVal EndTangentLength As System.Double, _
   ByVal StartTangentDir As System.Boolean, _
   ByVal EndTangentDir As System.Boolean, _
   ByVal StartMatchingType As System.Integer, _
   ByVal EndMatchingType As System.Integer, _
   ByVal Merge As System.Boolean _
) As Body2
```

```

Dim instance As IModeler
Dim PModDoc As ModelDoc2
Dim Profile As System.Object
Dim GuideCurve As System.Object
Dim Centerline As System.Object
Dim IsThinBody As System.Boolean
Dim ThinType As System.Integer
Dim Thickness1 As System.Double
Dim Thickness2 As System.Double
Dim FeatureScope As System.Boolean
Dim IsBlendClosed As System.Boolean
Dim KeepTangency As System.Boolean
Dim ForceNonRational As System.Boolean
Dim IsSolidBody As System.Boolean
Dim TessTolFactor As System.Double
Dim StartTangentLength As System.Double
Dim EndTangentLength As System.Double
Dim StartTangentDir As System.Boolean
Dim EndTangentDir As System.Boolean
Dim StartMatchingType As System.Integer
Dim EndMatchingType As System.Integer
Dim Merge As System.Boolean
Dim value As Body2
 
value = instance.CreateLoftBody2(PModDoc, Profile, GuideCurve, Centerline, IsThinBody, ThinType, Thickness1, Thickness2, FeatureScope, IsBlendClosed, KeepTangency, ForceNonRational, IsSolidBody, TessTolFactor, StartTangentLength, EndTangentLength, StartTangentDir, EndTangentDir, StartMatchingType, EndMatchingType, Merge)
```

```

Body2 CreateLoftBody2( 
   ModelDoc2 PModDoc,
   System.object Profile,
   System.object GuideCurve,
   System.object Centerline,
   System.bool IsThinBody,
   System.int ThinType,
   System.double Thickness1,
   System.double Thickness2,
   System.bool FeatureScope,
   System.bool IsBlendClosed,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.bool IsSolidBody,
   System.double TessTolFactor,
   System.double StartTangentLength,
   System.double EndTangentLength,
   System.bool StartTangentDir,
   System.bool EndTangentDir,
   System.int StartMatchingType,
   System.int EndMatchingType,
   System.bool Merge
)
```

```

Body2^ CreateLoftBody2( 
   ModelDoc2^ PModDoc,
   System.Object^ Profile,
   System.Object^ GuideCurve,
   System.Object^ Centerline,
   System.bool IsThinBody,
   System.int ThinType,
   System.double Thickness1,
   System.double Thickness2,
   System.bool FeatureScope,
   System.bool IsBlendClosed,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.bool IsSolidBody,
   System.double TessTolFactor,
   System.double StartTangentLength,
   System.double EndTangentLength,
   System.bool StartTangentDir,
   System.bool EndTangentDir,
   System.int StartMatchingType,
   System.int EndMatchingType,
   System.bool Merge
) 
```

#### Parameters

*PModDoc*
:   [Model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) in which to create the loft body

*Profile*
:   Array of sketches representing the profiles of the loft body

*GuideCurve*
:   Array of sketches representing the guide curves of the loft body

*Centerline*
:   Sketch representing a centerline of the loft body

*IsThinBody*
:   True if the loft body is to be a thin body, false if not

*ThinType*
:   - 0 = One direction
    - 1 = One direction reverse
    - 2 = Midplane
    - 3 = Two direction

*Thickness1*
:   Value for thickness for first direction if a thin body

*Thickness2*
:   Value for thickness for second direction if a thin body

*FeatureScope*
:   True if the loft body only affects selected bodies, false if the loft body affects all bodies

*IsBlendClosed*
:   True for a closed loft, false for an open loft; if true and you selected less that three profiles, then any selected guide curves must be closed curves

*KeepTangency*
:   If the section curves are tangent, then you have the option to specify whether the resulting faces are also tangent; specify true to maintain the tangency as seen in the section curves, false to not

    NOTE: When generating tangent surfaces, SOLIDWORKS maintains planar and cylindrical surface shapes if the section curves exhibit these characteristics.

*ForceNonRational*
:   True to force the resulting surface to be non-rational, false to not

*IsSolidBody*
:   True to return a solid loft body, false to return a surface loft body

*TessTolFactor*
:   Factor to control the number of intermediate sections used for loft with centerline; default value is 1.0; the greater the variable, the more intermediate sections created

*StartTangentLength*
:   Start tangent length

*EndTangentLength*
:   End tangent length

*StartTangentDir*
:   True is one direction, false is the opposite direction

*EndTangentDir*
:   True is one direction, false is the opposite direction

*StartMatchingType*
:   Tangency type at the start profile:

    - 0 = none
    - 1 = tangent to the normal of the profile
    - 2 = tangent to the selected vector
    - 3 = tangent to all adjacent faces sharing an edge with the start profile

*EndMatchingType*
:   Tangency type as the end profile:

    - 0 = none
    - 1 = tangent to the normal of the profile
    - 2 = tangent to the selected vector
    - 3 = tangent to all adjacent faces sharing an edge with the start profile

*Merge*
:   True merges the results in a multibody part, false does not

#### Return Value

Loft [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

Specifying guide curves and a centerline are optional. It is best to use guide curves, especially when you select profiles in the FeatureManager design tree.

You must specify the profiles in an order consistent with the desired direction of the loft. If creating a solid loft body, then the profiles must be closed. You can use any number of profiles. However, if you specify only one profile, then any specified guide curves must be closed curves.

Linear edge, sketch line, axis, plane and planar faces are qualified for tangency vector sections.

Example

[Create Loft Surface Body and Change Into Feature (VBA)](Create_Loft_Surface_Body_and_Change_Into_Feature_Example_VB.htm)  
[Create Loft Body (VB.NET)](Create_Loft_Body_Example_VBNET.htm)  
[Create Loft Body (VBA)](Create_Loft_Body_Example_VB.htm)  
[Create Loft Body (C#)](Create_Loft_Body_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IFeatureManager::InsertCutBlend Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutBlend.md)  
[IFeatureManager::InsertProtrusionBlend Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertProtrusionBlend.md)  
[IModelDoc2::InsertLoftRefSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertLoftRefSurface2.md)  
[IModeler::CreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftSurface.md)  
[IModeler::ICreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLoftSurface.md)
