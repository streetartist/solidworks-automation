# IGetFirstFacePair Method (IMidSurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~IGetFirstFacePair`

Obsolete. Superseded by IMidSurface2::IGetFirstFacePair.
Obsolete. Superseded by [IMidSurface2::IGetFirstFacePair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFacePair.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFirstFacePair( _
   ByRef Thickness As System.Double, _
   ByRef PartnerFaceDisp As Face _
) As Face
```

```

Dim instance As IMidSurface
Dim Thickness As System.Double
Dim PartnerFaceDisp As Face
Dim value As Face
 
value = instance.IGetFirstFacePair(Thickness, PartnerFaceDisp)
```

```

Face IGetFirstFacePair( 
   out System.double Thickness,
   out Face PartnerFaceDisp
)
```

```

Face^ IGetFirstFacePair( 
   [Out] System.double Thickness,
   [Out] Face^ PartnerFaceDisp
) 
```

#### Parameters

*Thickness*

*PartnerFaceDisp*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.md)  
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.md)
