# GetFirstFacePair Method (IMidSurface3)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFacePair`

Gets the first pair of parallel faces in this midsurface feature and the thickness (in meters) between the two faces.
Gets the first pair of parallel faces in this midsurface feature and the thickness (in meters) between the two faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstFacePair( _
   ByRef Thickness As System.Double, _
   ByRef PartnerFaceDisp As System.Object _
) As System.Object
```

```

Dim instance As IMidSurface3
Dim Thickness As System.Double
Dim PartnerFaceDisp As System.Object
Dim value As System.Object
 
value = instance.GetFirstFacePair(Thickness, PartnerFaceDisp)
```

```

System.object GetFirstFacePair( 
   out System.double Thickness,
   out System.object PartnerFaceDisp
)
```

```

System.Object^ GetFirstFacePair( 
   [Out] System.double Thickness,
   [Out] System.Object^ PartnerFaceDisp
) 
```

#### Parameters

*Thickness*
:   Distance between these two parallel faces

*PartnerFaceDisp*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) on the original part body used in generating the neutral face

#### Return Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) on the original part body used in generating the neutral face

Remarks

The two faces returned by this method are the two parallel faces from the original part body that were used to generate the first neutral face in this midsurface feature.

This method is similar to [IMidSurface3::GetFirstFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFace.md), except this method does not return the neutral face.

Call [IMidSurface3::GetNextFacePair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextFacePair.md) to get the next pair of faces in this midsurface feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.md)  
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.md)  
[IMidSurface3::IGetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFacePair.md)  
[IMidSurface3::GetFacePairCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFacePairCount.md)  
[IMidSurface3::GetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFacePair.md)  
[IMidSurface3::IGetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFacePair.md)
