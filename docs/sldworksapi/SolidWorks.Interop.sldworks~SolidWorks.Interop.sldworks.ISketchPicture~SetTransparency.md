# SetTransparency Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~SetTransparency`

Sets the transparency parameters of this picture on the sketch.
Sets the transparency parameters of this picture on the sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTransparency( _
   ByVal Style As System.Integer, _
   ByVal Transparency As System.Double, _
   ByVal MatchingColor As System.Integer, _
   ByVal MatchingTolerance As System.Double _
) As System.Boolean
```

```

Dim instance As ISketchPicture
Dim Style As System.Integer
Dim Transparency As System.Double
Dim MatchingColor As System.Integer
Dim MatchingTolerance As System.Double
Dim value As System.Boolean
 
value = instance.SetTransparency(Style, Transparency, MatchingColor, MatchingTolerance)
```

```

System.bool SetTransparency( 
   System.int Style,
   System.double Transparency,
   System.int MatchingColor,
   System.double MatchingTolerance
)
```

```

System.bool SetTransparency( 
   System.int Style,
   System.double Transparency,
   System.int MatchingColor,
   System.double MatchingTolerance
) 
```

#### Parameters

*Style*
:   Style as defined by [swSketchPictureTransparencyStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchPictureTransparencyStyle_e.html)

*Transparency*
:   - 0 = opaque
    - 1 = transparent

    describing the relative transparency depending on the value of Style

*MatchingColor*
:   RGB color used as the transparent color when Style is swSketchPictureTransparencyUserDefined

*MatchingTolerance*
:   - 0 = exact match
    - 1 = less exact match

    indicating how closely MatchingColor must be to be considered a transparent color when Style is swSketchPictureTransparencyUserDefined

#### Return Value

True if transparency is set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)  
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.md)  
[ISketchPicture::GetOrigin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetOrigin.md)
