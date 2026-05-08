# IGetFirstFacePair Method (IMidSurface2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFacePair`

Obsolete. Superseded by IMidSurface3::IGetFirstFacePair.
Obsolete. Superseded by [IMidSurface3::IGetFirstFacePair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstFacePair.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFirstFacePair( _
   ByRef Thickness As System.Double, _
   ByRef PartnerFaceDisp As Face2 _
) As Face2
```

```

Dim instance As IMidSurface2
Dim Thickness As System.Double
Dim PartnerFaceDisp As Face2
Dim value As Face2
 
value = instance.IGetFirstFacePair(Thickness, PartnerFaceDisp)
```

```

Face2 IGetFirstFacePair( 
   out System.double Thickness,
   out Face2 PartnerFaceDisp
)
```

```

Face2^ IGetFirstFacePair( 
   [Out] System.double Thickness,
   [Out] Face2^ PartnerFaceDisp
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

This method is similar to [IMidSurface2::IGetFirstFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFace.md), except this method does not return the neutral face.

Call [IMidSurface2::IGetNextFacePair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFacePair.md) to get the next pair of faces in this midsurface feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.md)  
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.md)  
[IMidSurface2::GetFacePairCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFacePairCount.md)  
[IMidSurface2::GetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstFacePair.md)  
[IMidSurface2::GetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFacePair.md)
