# CreateLoftSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftSurface`

Creates a loft surface.
Creates a loft surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateLoftSurface( _
   ByVal CurveArray As System.Object, _
   ByVal BBlendClosed As System.Boolean, _
   ByVal BForceCubic As System.Boolean, _
   ByVal GuideCrvArray As System.Object, _
   ByVal StartMatchingType As System.Integer, _
   ByVal EndMatchingType As System.Integer, _
   ByVal NormalAtStartSection As System.Object, _
   ByVal NormalAtEndSection As System.Object, _
   ByVal StartMatchingFaceList As System.Object, _
   ByVal EndMatchingFaceList As System.Object, _
   ByVal DegeneratedStart As System.Boolean, _
   ByVal DegeneratedEnd As System.Boolean, _
   ByVal StartPointOfStartSection As System.Object, _
   ByVal StartPointOfEndSection As System.Object, _
   ByVal SectionIndexStart As System.Integer, _
   ByVal SectionIndexEnd As System.Integer, _
   ByVal GuideIndexStart As System.Integer, _
   ByVal GuideIndexEnd As System.Integer _
) As System.Object
```

```

Dim instance As IModeler
Dim CurveArray As System.Object
Dim BBlendClosed As System.Boolean
Dim BForceCubic As System.Boolean
Dim GuideCrvArray As System.Object
Dim StartMatchingType As System.Integer
Dim EndMatchingType As System.Integer
Dim NormalAtStartSection As System.Object
Dim NormalAtEndSection As System.Object
Dim StartMatchingFaceList As System.Object
Dim EndMatchingFaceList As System.Object
Dim DegeneratedStart As System.Boolean
Dim DegeneratedEnd As System.Boolean
Dim StartPointOfStartSection As System.Object
Dim StartPointOfEndSection As System.Object
Dim SectionIndexStart As System.Integer
Dim SectionIndexEnd As System.Integer
Dim GuideIndexStart As System.Integer
Dim GuideIndexEnd As System.Integer
Dim value As System.Object
 
value = instance.CreateLoftSurface(CurveArray, BBlendClosed, BForceCubic, GuideCrvArray, StartMatchingType, EndMatchingType, NormalAtStartSection, NormalAtEndSection, StartMatchingFaceList, EndMatchingFaceList, DegeneratedStart, DegeneratedEnd, StartPointOfStartSection, StartPointOfEndSection, SectionIndexStart, SectionIndexEnd, GuideIndexStart, GuideIndexEnd)
```

```

System.object CreateLoftSurface( 
   System.object CurveArray,
   System.bool BBlendClosed,
   System.bool BForceCubic,
   System.object GuideCrvArray,
   System.int StartMatchingType,
   System.int EndMatchingType,
   System.object NormalAtStartSection,
   System.object NormalAtEndSection,
   System.object StartMatchingFaceList,
   System.object EndMatchingFaceList,
   System.bool DegeneratedStart,
   System.bool DegeneratedEnd,
   System.object StartPointOfStartSection,
   System.object StartPointOfEndSection,
   System.int SectionIndexStart,
   System.int SectionIndexEnd,
   System.int GuideIndexStart,
   System.int GuideIndexEnd
)
```

```

System.Object^ CreateLoftSurface( 
   System.Object^ CurveArray,
   System.bool BBlendClosed,
   System.bool BForceCubic,
   System.Object^ GuideCrvArray,
   System.int StartMatchingType,
   System.int EndMatchingType,
   System.Object^ NormalAtStartSection,
   System.Object^ NormalAtEndSection,
   System.Object^ StartMatchingFaceList,
   System.Object^ EndMatchingFaceList,
   System.bool DegeneratedStart,
   System.bool DegeneratedEnd,
   System.Object^ StartPointOfStartSection,
   System.Object^ StartPointOfEndSection,
   System.int SectionIndexStart,
   System.int SectionIndexEnd,
   System.int GuideIndexStart,
   System.int GuideIndexEnd
) 
```

#### Parameters

*CurveArray*
:   Array of b-spline [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*BBlendClosed*
:   True if blend closed, false if not

*BForceCubic*
:   True if force surface is cubic, false if not

*GuideCrvArray*
:   Array of guide [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*StartMatchingType*
:   Start matching type:

    - 0 = MATCH\_NONE (default)
    - 1 = MATCH\_NORMAL
    - 2 = MATCH\_VECTOR
    - 3 = MATCH\_ALL\_FACES or MATCH\_FACE\_G1
    - 4 = MATCH\_FACE\_G2

*EndMatchingType*
:   End matching type:

    - 0 = MATCH\_NONE (default)
    - 1 = MATCH\_NORMAL
    - 2 = MATCH\_VECTOR
    - 3 = MATCH\_ALL\_FACES or MATCH\_FACE\_G1
    - 4 = MATCH\_FACE\_G2

*NormalAtStartSection*
:   [Normal at start section](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) when StartMatchingType is MATCH\_NORMAL or MATCH\_VECTOR; otherwise, can be Nothing

*NormalAtEndSection*
:   [Normal at start section](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) when EndMatchingType is MATCH\_NORMAL or MATCH\_VECTOR; otherwise, can be Nothing

*StartMatchingFaceList*
:   Array of matching [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) at start section when startMatchingType is MATCH\_ALL\_FACES, MATCH\_FACE\_G1, or MATCH\_FACE\_G2; otherwise, can be Nothing

*EndMatchingFaceList*
:   Array of matching [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) at end section when startMatchingType is MATCH\_ALL\_FACES, MATCH\_FACE\_G1, or MATCH\_FACE\_G2; otherwise, can be Nothing

*DegeneratedStart*
:   True to degenerate at start, false to not

*DegeneratedEnd*
:   True to degenerate at end, false to not

*StartPointOfStartSection*
:   [Start point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) of start section

*StartPointOfEndSection*
:   [Start point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) of end section

*SectionIndexStart*
:   Index of start section; default is -1

*SectionIndexEnd*
:   Index of end section; default is -1

*GuideIndexStart*
:   Index of start guide curve; default is -1

*GuideIndexEnd*
:   Index of end guide curve; default is -1

#### Return Value

Newly created loft [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineSurface.md)  
[IModeler::CreateCoonsBSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCoonsBSurface.md)  
[IModeler::CreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.md)  
[IModeler::CreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrusionSurface.md)  
[IModeler::CreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftSurface.md)  
[IModeler::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateOffsetSurface.md)  
[IModeler::CreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.md)  
[IModeler:::CreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.md)  
[IModeler::CreateSphericalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface2.md)  
[IModeler::CreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptSurface.md)  
[IModeler::CreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateToroidalSurface.md)  
[IModeler::ICreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineSurface.md)  
[IModeler::ICreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateConicalSurface2.md)  
[IModeler::ICreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.md)  
[IModeler::ICreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateExtrusionSurface.md)  
[IModeler::ICreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLoftSurface.md)  
[IModeler::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateOffsetSurface.md)  
[IModeler::ICreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface2.md)  
[IModeler::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurface.md)  
[IModeler::ICreateSphericalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSphericalSurface2.md)  
[IModeler::ICreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSweptSurface.md)  
[IModeler::ICreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateToroidalSurface.md)
