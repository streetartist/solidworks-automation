# CreateLoftBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftBody`

Obsolete. Superseded by IModeler::CreateLoftBody2.
Obsolete. Superseded by [IModeler::CreateLoftBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftBody2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateLoftBody( _
   ByVal PModDoc As ModelDoc2, _
   ByVal IsBlendClosed As System.Boolean, _
   ByVal KeepTangency As System.Boolean, _
   ByVal ForceNonRational As System.Boolean, _
   ByVal IsSolidBody As System.Boolean, _
   ByVal TessTolFactor As System.Double, _
   ByVal StartMatchingType As System.Short, _
   ByVal EndMatchingType As System.Short _
) As Body2
```

```

Dim instance As IModeler
Dim PModDoc As ModelDoc2
Dim IsBlendClosed As System.Boolean
Dim KeepTangency As System.Boolean
Dim ForceNonRational As System.Boolean
Dim IsSolidBody As System.Boolean
Dim TessTolFactor As System.Double
Dim StartMatchingType As System.Short
Dim EndMatchingType As System.Short
Dim value As Body2
 
value = instance.CreateLoftBody(PModDoc, IsBlendClosed, KeepTangency, ForceNonRational, IsSolidBody, TessTolFactor, StartMatchingType, EndMatchingType)
```

```

Body2 CreateLoftBody( 
   ModelDoc2 PModDoc,
   System.bool IsBlendClosed,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.bool IsSolidBody,
   System.double TessTolFactor,
   System.short StartMatchingType,
   System.short EndMatchingType
)
```

```

Body2^ CreateLoftBody( 
   ModelDoc2^ PModDoc,
   System.bool IsBlendClosed,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.bool IsSolidBody,
   System.double TessTolFactor,
   System.short StartMatchingType,
   System.short EndMatchingType
) 
```

#### Parameters

*PModDoc*
:   [Model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) in which to create the lofted body

*IsBlendClosed*
:   True for a closed, false for an open loft; if true and you selected less that three profiles; any selected guide curves must be closed curves

*KeepTangency*
:   If the section curves are tangent, then you have the option to specify whether the resulting faces are also tangent; specify true to maintain the tangency as seen in the section curves, false to not

    NOTE: When generating tangent surfaces, SOLIDWORKS maintains planar and cylindrical surface shapes if the section curves exhibit these characteristics.

*ForceNonRational*
:   True to force the resulting surface to be non-rational, false to not

*IsSolidBody*
:   True to return a solid body, false to return a surface body

*TessTolFactor*
:   Factor to control the number of intermediate sections used for loft with centerline; default value is 1.0; the greater the variable, the more intermediate sections created

*StartMatchingType*
:   Tangency type at the start profile (see Remarks)

*EndMatchingType*
:   Tangency type as the end profile (see Remarks)

#### Return Value

Newly created [loft](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

Selection of guide curves and centerline is optional. However, you must select the profiles in an order consistent with the desired direction of the loft. Because a solid is being created, the section profiles must be closed.

It is best to use guide curves, especially when you select profiles in the FeatureManager design tree.

You can use any number of profiles, However, if you select only one profile, then any selected guide curves must be closed curves.

Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the profiles and guide curves. Set the mark for:

- profile selections to 1
- any guide curve selection to 2
- centerline selection to 4
- start tangency vector selection to 8
- start tangency faces selection to 16 (not available)
- end tangency vector selection to 32
- end tangency faces selection to 64 (not available)

Linear edge, sketch line, axis, plane and planar faces are qualified for tangency vector sections.

The tangency types can be:

- 0 = none
- 1 = tangent to the normal of the profile
- 2 = tangent to the selected vector
- 3 = tangent to all adjacent faces sharing an edge with the start profile

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
